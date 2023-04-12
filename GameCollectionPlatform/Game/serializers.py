from rest_framework import serializers
from .models import GameModel

class GameSerializers(serializers.ModelSerializer):
    class Meta:
        model = GameModel
        fields = ['gameName','gameRate','gamePrice','gameDiscount','gameAge','gameLabel','gamePublishDate','gameDescription','gameicon']
