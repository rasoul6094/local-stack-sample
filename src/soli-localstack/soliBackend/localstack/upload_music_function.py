import boto3
import os
import base64
from botocore.exceptions import NoCredentialsError

localstack_endpoint = os.getenv('AWS_ENDPOINT_URL', 'http://localhost:4566')

s3_client = boto3.client('s3', endpoint_url=localstack_endpoint, aws_access_key_id='test', aws_secret_access_key='test', region_name='us-east-1')

dynamodb = boto3.resource(
    'dynamodb',
    endpoint_url=os.getenv('AWS_ENDPOINT_URL', 'http://localhost:4566'),
    aws_access_key_id='test', 
    aws_secret_access_key='test', 
    region_name='us-east-1'
)

TABLE_NAME = 'users'
BUCKET_NAME ='storage'

def upload_music_handler(event, context):
    username = event.get('username', None) 
    file_content_base64 = event.get('file_content',None)   
    object_name = event.get('object_name', 'test.mp3') 
    if(not username):
        return {
            'statusCode': 400,
            'body': 'Username is required in the event.'
        }
    if not file_content_base64:
        return {
            'statusCode': 400,
            'body': 'File content is required in the event.'
        }

    try:
        file_content = base64.b64decode(file_content_base64)
        upload_file_to_bucket(BUCKET_NAME, file_content, object_name)

        file_url = generate_presigned_url(BUCKET_NAME, object_name, expiration=315360000)  

        add_music_to_user(username, file_url)

        return {
            'statusCode': 200,
            'body': f"File uploaded to bucket '{BUCKET_NAME}' as '{object_name}'. URL: {file_url}"
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': f"Error: {str(e)}"
        }

def upload_file_to_bucket(bucket_name, file_content, object_name):
    try:
        s3_client.put_object(
            Body=file_content,
            Bucket=bucket_name,
            Key=object_name,
            ContentType=f'audio/{object_name.split(".")[-1]}'  # Updated ContentType
        )
        print(f"File uploaded to bucket '{bucket_name}' as '{object_name}'!")
    except NoCredentialsError:
        print("Credentials not available!")


def generate_presigned_url(bucket_name, object_name, expiration=315360000):
    try:
        response = s3_client.generate_presigned_url('get_object',
                                                    Params={'Bucket': bucket_name, 'Key': object_name},
                                                    ExpiresIn=expiration)
    except Exception as e:
        print(f"Error generating presigned URL: {str(e)}")
        return None

    return response

def add_music_to_user(username, new_music_url):
    table = dynamodb.Table(TABLE_NAME)

    response = table.get_item(Key={'username': username})
    user = response.get('Item')

    if user:
        music_urls = user.get('music_urls', [])
        music_urls.append(new_music_url)

        table.update_item(
            Key={'username': username},
            UpdateExpression='SET music_urls = :urls',
            ExpressionAttributeValues={':urls': music_urls}
        )
        print(f"Added music URL '{new_music_url}' to existing user '{username}'.")

    else:
        table.put_item(
            Item={
                'username': username,
                'music_urls': [new_music_url]  
            }
        )
        print(f"Created new user '{username}' with music URL '{new_music_url}'.")
