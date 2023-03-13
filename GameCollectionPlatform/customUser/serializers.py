
from rest_framework import serializers
from allauth.account.adapter import get_adapter
from GameCollectionPlatform import settings
from .models import User
from allauth.account.utils import setup_user_email


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(required=settings.ACCOUNT_EMAIL_REQUIRED)
    firstName = serializers.CharField(required=False, write_only=True)
    lastName = serializers.CharField(required=False, write_only=True)
    userInfo = serializers.CharField(required=False, write_only=True)

    password1 = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)

    def validate_password1(self, password):
        return get_adapter().clean_password(password)

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError(
                ("The two password fields didn't match."))
        return data

    def custom_signup(self, request, user):
        pass

    def get_cleaned_data(self):
        return {
            'first_name': self.validated_data.get('firstName', ''),
            'last_name': self.validated_data.get('lastName', ''),
            'userInfo': self.validated_data.get('userInfo', ''),
            'userType': self.validated_data.get('user_type', ''),
            'password': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        setup_user_email(request, user, [])
        return user

        user.save()
        return user


class UserDetailsSerializer(serializers.ModelSerializer):
    """
    User model w/o password
    """
    class Meta:
        model = User
        fields = ('pk', 'username', 'email', 'firstName','lastName',
                   'userType','profilePic','userInfo','dateOfBirth','isSuperUser','location')
        read_only_fields = ('email', )