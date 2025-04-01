# views.py

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import boto3
import json
import base64
from django.conf import settings
from rest_framework.views import APIView
import time
from django.contrib.auth.models import User
from rest_framework import status


class UploadMusic(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Check if the file is present in the request
        if 'music' not in request.FILES:
            return Response({"message": "No music file provided"}, status=400)

        music = request.FILES['music']
        user = request.user.username

        # Validate file type
        if music.name.split(".")[-1].lower() not in ["mp3", "wav"]:
            return Response({"message": "Invalid file type. Only .mp3 and .wav are allowed."}, status=400)

        # Encode the music file
        encoded_music = base64.b64encode(music.read()).decode('utf-8')

        # Invoke Lambda function
        lambda_client = boto3.client(
            'lambda', region_name=settings.REGION_NAME, endpoint_url=settings.END_POINT_URL)
        payload = {
            "username": user,
            "object_name": f"{user}_{music.name}_{int(time.time())}.{music.name.split('.')[-1]}",
            "file_content": encoded_music
        }
        response = lambda_client.invoke(
            FunctionName='upload_music', 
            InvocationType='RequestResponse',
            Payload=json.dumps(payload)
        )
        
        print(response)  # Debug the response from Lambda
        
        if 'Payload' not in response:
            return Response({"message": "Invalid response from Lambda"}, status=500)

        try:
            text = response['Payload'].read().decode('utf-8')
            response_data = json.loads(text)
        except json.JSONDecodeError:
            return Response({"message": "Error decoding the response from Lambda"}, status=500)

        return Response(response_data)


class GetMusic(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Invoke Lambda function to retrieve music
        lambda_client = boto3.client(
            'lambda', region_name=settings.REGION_NAME, endpoint_url=settings.END_POINT_URL)
        response = lambda_client.invoke(
            FunctionName='getmusic',  # Updated Lambda function name
            InvocationType='RequestResponse',
        )

        return Response(json.loads(response['Payload'].read().decode('utf-8')))


class RegisterUser(APIView):
    permission_classes = []

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if not username or not password:
            return Response({"message": "Username and password required"}, status=400)
        if User.objects.filter(username=username).exists():
            return Response({"message": "User already exists"}, status=400)

        User.objects.create_user(username=username, password=password)
        return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
