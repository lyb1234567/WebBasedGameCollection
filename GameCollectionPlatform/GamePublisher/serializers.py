from rest_framework import serializers
from .models import GamePublisher

class GamePublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = GamePublisher
        fields = ['publisherCode', 'pubEmail', 'profilePicture', 'publisherDescription', 'publisherInfo']
