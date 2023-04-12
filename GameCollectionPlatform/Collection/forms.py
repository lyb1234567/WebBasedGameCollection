from django import forms
from .models import GameCollection

class GameCollectionForm(forms.ModelForm):
    class Meta:
        model = GameCollection
        fields = ['user', 'game', 'collectionName']
