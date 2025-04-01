#!/bin/bash

# Sleep for a few seconds to ensure everything is up
sleep 5
cd /app/localstack

# Check if the necessary function files exist before zipping them
if [[ ! -f "upload_music_function.py" ]] || [[ ! -f "getmusic_function.py" ]]; then
    echo "Error: One or more function files are missing."
    exit 1
fi

# Zip the Lambda function files
echo "Zipping Lambda function files..."
zip -r upload_music.zip upload_music_function.py 
zip -r getmusic.zip getmusic_function.py 

# Check if the Lambda functions exist and delete them if they do
echo "Checking and deleting existing Lambda functions..."
if aws --endpoint-url=$AWS_ENDPOINT_URL lambda get-function --function-name upload_music &> /dev/null; then
    echo "Deleting existing 'upload_music' function."
    aws --endpoint-url=$AWS_ENDPOINT_URL lambda delete-function --function-name upload_music
fi

if aws --endpoint-url=$AWS_ENDPOINT_URL lambda get-function --function-name getmusic &> /dev/null; then
    echo "Deleting existing 'getmusic' function."
    aws --endpoint-url=$AWS_ENDPOINT_URL lambda delete-function --function-name getmusic
fi

# Create Lambda functions
echo "Creating Lambda functions..."
aws --endpoint-url=$AWS_ENDPOINT_URL lambda create-function \
  --function-name upload_music \
  --runtime python3.8 \
  --role arn:aws:iam::000000000000:role/lambda-role \
  --handler upload_music_function.upload_music_handler \
  --zip-file fileb://upload_music.zip

aws --endpoint-url=$AWS_ENDPOINT_URL lambda create-function \
  --function-name getmusic \
  --runtime python3.8 \
  --role arn:aws:iam::000000000000:role/lambda-role \
  --handler getmusic_function.getmusic_handler \
  --zip-file fileb://getmusic.zip

# Create S3 bucket
echo "Creating S3 bucket: $BUCKET_NAME"
aws --endpoint-url=$AWS_ENDPOINT_URL s3api create-bucket --bucket $BUCKET_NAME --region $AWS_DEFAULT_REGION

# Set CORS configuration (ensure cors.json exists)
if [[ ! -f "cors.json" ]]; then
    echo "Error: cors.json file is missing."
    exit 1
fi
echo "Setting CORS configuration for S3 bucket..."
aws --endpoint-url=$AWS_ENDPOINT_URL s3api put-bucket-cors \
    --bucket $BUCKET_NAME \
    --cors-configuration file://cors.json

# Check and delete the DynamoDB table if it exists
echo "Checking and deleting existing DynamoDB table if it exists..."
if aws --endpoint-url=$AWS_ENDPOINT_URL dynamodb describe-table --table-name $TABLE_NAME &> /dev/null; then
    echo "Deleting existing DynamoDB table: $TABLE_NAME"
    aws --endpoint-url=$AWS_ENDPOINT_URL dynamodb delete-table --table-name $TABLE_NAME
fi

# Create DynamoDB table
echo "Creating DynamoDB table: $TABLE_NAME"
aws --endpoint-url=$AWS_ENDPOINT_URL dynamodb create-table \
    --table-name $TABLE_NAME \
    --attribute-definitions AttributeName=username,AttributeType=S \
    --key-schema AttributeName=username,KeyType=HASH \
    --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5

# Clean up zip files
echo "Cleaning up zip files..."
rm getmusic.zip
rm upload_music.zip

# Start Django server
echo "Starting Django server..."
if command -v python3 &> /dev/null; then
    python3 /app/manage.py runserver 0.0.0.0:8000
else
    python /app/manage.py runserver 0.0.0.0:8000
fi

