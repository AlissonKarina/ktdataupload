from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView

from .views import AuthTokenObtainPairView

urlpatterns = [
    path('token/', AuthTokenObtainPairView.as_view(), name='token_obtain'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]