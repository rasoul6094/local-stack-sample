# Soli Music Application 🎵

[![Django](https://img.shields.io/badge/Django-3.2+-092E20?logo=django)](https://www.djangoproject.com/)
[![LocalStack](https://img.shields.io/badge/LocalStack-AWS%20Emulation-FF9900?logo=amazon-aws)](https://localstack.cloud/)
[![Docker](https://img.shields.io/badge/Docker-2.0+-2496ED?logo=docker)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

A full-stack music management platform with secure user authentication, cloud storage emulation, and seamless audio playback.



## ✨ Key Features

- **🔐 Secure Authentication**  
  JWT-based user registration and login system
- **🎶 Music Management**  
  Upload, store, and organize MP3/WAV files
- **☁️ Cloud Storage Emulation**  
  LocalStack-powered S3 bucket for file storage
- **📊 Data Persistence**  
  DynamoDB integration for metadata management
- **🎧 Instant Playback**  
  Built-in audio player in the music gallery
- **🐳 Containerized Deployment**  
  Dockerized environment for easy setup

## 🚀 Quick Start

### Prerequisites
- Docker 20.10+
- Docker Compose 2.0+
- Modern web browser

### Installation
```bash
# Clone the repository
git clone https://github.com/rasoul6094/soli-music-app.git
cd soli-music-app

# Start all services
docker-compose up --build
```

### Access Points
- **Backend API**: `http://localhost:8000`
- **Frontend**: Open `soliFrontend/index.html` in your browser

## 🖥️ User Guide

### Account Management
1. **Registration**  
   Visit `register.html` and create your account
2. **Login**  
   Access `login.html` to authenticate (token stored in localStorage)

### Music Operations
1. **Upload Tracks**  
   - Navigate to `upload.html`  
   - Select audio files (MP3/WAV)  
   - Submit to upload to your personal storage

2. **Browse Library**  
   - Access `gallery.html`  
   - View all available tracks  
   - Click to play any song

## 🔌 API Documentation

### Upload Endpoint
```bash
curl -X POST http://localhost:8000/upload/ \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -F "music=@./path/to/your/track.mp3"
```

### Successful Response
```json
{
  "status": "success",
  "message": "File uploaded successfully",
  "data": {
    "filename": "username_track.mp3",
    "url": "http://localhost:4566/storage/username_track.mp3",
    "timestamp": "2023-11-15T12:34:56Z"
  }
}
```

## 🛠 Development

### Project Structure
```
soli-music-app/
├── soliBackend/       # Django application
├── soliFrontend/      # HTML/CSS/JS interface
├── docker-compose.yml # Container configuration
└── README.md          # Project documentation
```

### Building Locally
```bash
# Set up Python environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Run development server
python manage.py runserver
```

## 🤝 Contribution Guidelines

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

## 📧 Contact

Rasoul Soli - [@rasoul_soli](https://github.com/rasoul6094)


