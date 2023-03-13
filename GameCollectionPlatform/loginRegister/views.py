from django.shortcuts import render
from django.http import  JsonResponse
from .models import Login
from rest_framework.viewsets import ModelViewSet
from .serializers import LoginSerializer

class LoginViewSet(ModelViewSet):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer

