from django.contrib.auth import logout
from django.shortcuts import redirect, render
from rest_framework.views import APIView
from .serializers import UserSerializer

from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import LoginSerializer

from translate import Translator

from rest_framework import status
from .serializers import TranslationSerializer
from django.http import JsonResponse


class RegisterView(APIView):
    """
        This class is created for user registration if you want to use the translator app then
        you have to register yourself
    """
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return redirect('http://127.0.0.1:8000/api/token/')

    def get(self, request):
        serializer = UserSerializer()
        return render(request, 'app/register.html', {'serializer': serializer})


class CustomTokenObtainPairView(TokenObtainPairView):
    """
        This class is created if you have already registered then for use the translator you can login
        and use the translator app
    """
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        response_data = serializer.validated_data

        return redirect('http://127.0.0.1:8000/api/home/')

    def get(self, request):
        serializer = UserSerializer()
        return render(request, 'app/login.html', {'serializer': serializer})


import logging

logger = logging.getLogger(__name__)


class TranslatorView(APIView):
    """
        This class use for home page of translator app
    """
    def post(self, request):
        serializer = TranslationSerializer(data=request.data)

        if serializer.is_valid():
            text = serializer.validated_data['text']
            target_language = serializer.validated_data.get('target_language', 'en')

            translator = Translator(to_lang=target_language)
            try:
                translation = translator.translate(text)
            except Exception as e:
                logger.error(f"Translation error: {e}")
                return JsonResponse({'error': 'Translation error occurred.'},
                                    status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            response_data = {'translation': translation}
            return JsonResponse(response_data)

        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TranslatorhomeView(APIView):
    """
        This class is used for get the home page
    """
    def get(self, request):
        return render(request, 'app/home.html')


class LogoutView(APIView):
    """
        This class used for logout from the tranlator app page
    """
    def get(self, request):
        logout(request)
        return redirect('http://127.0.0.1:8000/api/register/')
