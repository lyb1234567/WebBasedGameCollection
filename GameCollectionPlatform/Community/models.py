from django.db import models
from Game.models import GameModel
from GamePublisher.models import GamePublisher
# Create your models here.
class Community(models.Model):
    communityCode = models.AutoField(primary_key=True)
    game = models.ForeignKey(GameModel, on_delete=models.CASCADE, blank=True)
    gamePublisher = models.ForeignKey(GamePublisher, on_delete=models.CASCADE)
    review = models.ManyToManyField('Review.Review',blank=True) 
