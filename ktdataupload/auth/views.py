from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import AuthTokenObtainPairSerializer

class AuthTokenObtainPairView(TokenObtainPairView):
    serializer_class = AuthTokenObtainPairSerializer