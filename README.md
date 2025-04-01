```markdown
# Soli Music Application 🎵

[![Django](https://img.shields.io/badge/Django-3.2+-092E20?logo=django)](https://www.djangoproject.com/)
[![LocalStack](https://img.shields.io/badge/LocalStack-AWS%20Emulation-FF9900?logo=amazon-aws)](https://localstack.cloud/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

A web-based platform for uploading and managing music files, powered by **Django** (backend) and **LocalStack** (AWS emulation). Includes user authentication, S3 uploads, and a music gallery.

![Soli Music Demo](https://via.placeholder.com/800x400?text=Soli+Music+Demo) *(Replace with actual screenshot)*

---

## ✨ Features
- **🔒 User Authentication**: Secure registration/login with JWT tokens.
- **🎵 Music Upload**: Upload `.mp3`/`.wav` files to an S3 bucket (emulated via LocalStack).
- **📁 Music Gallery**: Browse and play uploaded tracks.
- **☁️ AWS Emulation**: LocalStack-powered S3, DynamoDB, and Lambda.
- **🚀 Dockerized**: Ready-to-run with `docker-compose`.

---

## 🛠 Installation

### Prerequisites
- [Docker](https://www.docker.com/) + [Docker Compose](https://docs.docker.com/compose/)
- Python 3.8+ (optional for manual setup)

### Quick Start
```bash
git clone https://github.com/your-repo/soli-music-app.git
cd soli-music-app
docker-compose up --build
```
Access:
- **Backend**: http://127.0.0.1:8000
- **Frontend**: Open `soliFrontend/*.html` in your browser.

---

## 🎮 Usage

### 1. Register a User
- Navigate to `register.html` → Enter username/password → Click **Register**.

### 2. Log In
- Visit `login.html` → Enter credentials → Token is saved in `localStorage`.

### 3. Upload Music
- Go to `upload.html` → Select `.mp3`/`.wav` → Click **Upload**.
- File is stored in S3, metadata saved in DynamoDB.

### 4. Browse Music
- Open `gallery.html` → View/play all uploaded tracks.

---

## 📚 API Examples

### Upload via `curl`
```bash
curl -X POST http://127.0.0.1:8000/upload/ \
  -H "Authorization: Bearer <your_token>" \
  -F "music=@path/to/song.mp3"
```

**Response:**
```json
{
  "statusCode": 200,
  "body": "File uploaded to bucket 'storage' as 'username_song.mp3'."
}
```

---

## 🤝 Contributing
Pull requests welcome! Follow these steps:
1. Fork the repo.
2. Create a branch (`git checkout -b feature/xyz`).
3. Commit changes (`git commit -m 'Add feature'`).
4. Push (`git push origin feature/xyz`).
5. Open a PR.

---

## 📜 License
MIT © [rasoul_soli](https://github.com/rasoul6094)

```

