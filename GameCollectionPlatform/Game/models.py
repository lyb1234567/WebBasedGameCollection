from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
# Create your models here.

class GameManger():
    def create(self, gameName, gameRate, gamePrice, gameDiscount, gameAge, gameLabel, gamePublishDate, gameDescription):
        game = GameModel(
            gameName=gameName,
            gameRate=gameRate,
            gamePrice=gamePrice,
            gameDiscount=gameDiscount,
            gameAge=gameAge,
            gameLabel=gameLabel,
            gamePublishDate=gamePublishDate,
            gameDescription=gameDescription,
        )
        game.save()
        return game
class GameModel(models.Model):
    gameCode = models.AutoField(primary_key=True)
    # pubName = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    gameName = models.CharField(max_length=255)
    gameRate = models.FloatField()
    gamePrice = models.DecimalField(max_digits=10, decimal_places=2)
    gameDiscount = models.FloatField()
    gameAge = models.IntegerField()
    gameLabel = models.CharField(max_length=255)
    gamePublishDate = models.DateField(default=timezone.now)
    gameDescription = models.TextField()
    objects=GameManger()
    