from django import forms
from .models import GameModel

class GameForm(forms.ModelForm):
    class Meta:
        model = GameModel
        fields = ['gameName', 'gameRate', 'gamePrice', 'gameDiscount', 'gameAge', 'gameLabel', 'gamePublishDate', 'gameDescription']