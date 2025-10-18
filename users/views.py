from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomUserSerializer, RegisterSerializer
from .models import CustomUser
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer


class TokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomUserSerializer

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client