from rest_framework import serializers
from .models import GameCollection

class GameCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameCollection
        fields = '__all__'
