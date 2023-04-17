from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
import os
# Create your models here.

class GameManger():
    def create_game(self, gameName, gameRate, gamePrice, gameDiscount, gameAge, gameLabel, gamePublishDate, gameDescription,publisher):
        game = GameModel(
            gameName=gameName,
            gameRate=gameRate,
            gamePrice=gamePrice,
            gameDiscount=gameDiscount,
            gameAge=gameAge,
            gameLabel=gameLabel,
            gamePublishDate=gamePublishDate,
            gameDescription=gameDescription,
            publisher=publisher
        )
        game.save()
        return game
def game_icon_path(instance, filename):
    return os.path.join('gameIcons', f'user_{instance.pk}', filename)
class GameModel(models.Model):
    gameCode = models.AutoField(primary_key=True)
    publisher = models.ForeignKey('GamePublisher.GamePublisher', on_delete=models.CASCADE,null=True, blank=True)
    gameName = models.CharField(max_length=255)
    gameRate = models.FloatField()
    gamePrice = models.DecimalField(max_digits=10, decimal_places=2)
    gameDiscount = models.FloatField()
    gameAge = models.IntegerField()
    gameLabel = models.CharField(max_length=255)
    gamePublishDate = models.DateField(default=timezone.now)
    gameDescription = models.TextField()
    collection=models.ManyToManyField("Collection.GameCollection",blank=True)
    gameicon=models.ImageField(upload_to='game_icon_path',default=None,blank=True, null=True,max_length=1000,)
    objects=GameManger()
    