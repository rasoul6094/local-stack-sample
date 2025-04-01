import boto3
import os
from botocore.exceptions import NoCredentialsError

localstack_endpoint = os.getenv('AWS_ENDPOINT_URL', 'http://localhost:4566')

dynamodb = boto3.resource(
    'dynamodb',
    endpoint_url=localstack_endpoint,
    aws_access_key_id='test',
    aws_secret_access_key='test',
    region_name='us-east-1'
)

TABLE_NAME = 'users'

def getmusic_handler(event, context):
    try:
        table = dynamodb.Table(TABLE_NAME)

        response = table.scan()
        users = response.get('Items', [])

        all_music = {}
        for user in users:
            username = user.get('username')
            music_urls = user.get('music_urls', [])
            all_music[username] = music_urls

        return {
            'statusCode': 200,
            'body': all_music
        }

    except NoCredentialsError:
        return {
            'statusCode': 500,
            'body': 'Credentials not available.'
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error: {str(e)}'
        }
