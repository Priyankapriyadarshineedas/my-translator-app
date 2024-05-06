from django.urls import path
from .views import RegisterView, CustomTokenObtainPairView, TranslatorView, TranslatorhomeView, LogoutView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/register/', RegisterView.as_view(), name="sign_up"),
    path('api/home/', TranslatorhomeView.as_view(), name='translator_home'),
    path('api/translate/', TranslatorView.as_view(), name='translate'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
]
