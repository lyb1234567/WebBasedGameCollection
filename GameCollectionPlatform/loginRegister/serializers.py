from rest_framework.serializers import ModelSerializer
from .models import Login

class LoginSerializer(ModelSerializer):
    class Meta:
        model = Login
        fields = ['email','password']