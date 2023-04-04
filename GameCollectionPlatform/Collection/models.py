from django.db import models
from Game.models import GameModel
# Create your models here.
class GameCollection(models.Model):
    collectionCode = models.AutoField(primary_key=True)
    user = models.ForeignKey('customUser.User', on_delete=models.CASCADE)
    game = models.ForeignKey(GameModel, on_delete=models.CASCADE)
    collectionName = models.CharField(max_length=255)