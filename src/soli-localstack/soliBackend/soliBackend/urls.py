# urls.py

from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import UploadMusic, GetMusic, RegisterUser  # Updated view names

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('upload/', UploadMusic.as_view()),  # Updated path for music upload
    path('get/', GetMusic.as_view()),  # Updated path for retrieving music
    path('register/', RegisterUser.as_view(), name='register_user'),
]
