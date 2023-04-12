from django import forms
from .models import GamePublisher

class GamePublisherForm(forms.ModelForm):
    class Meta:
        model = GamePublisher
        fields = ['pubPassword', 'pubEmail', 'profilePicture', 'publisherDescription', 'publisherInfo']
