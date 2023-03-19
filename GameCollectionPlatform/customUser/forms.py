from django import forms
from customUser.models import User


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['profilePic', 'userInfo']