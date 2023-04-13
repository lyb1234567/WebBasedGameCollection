from django.db import models
from Game.models import GameModel


class GameCollectionManager(models.Manager):
    def create_game_collection(self, user, game, collection_name):
        game_collection = self.create(user=user, game=game, collectionName=collection_name)
        return game_collection

    def get_game_collection_by_id(self, collection_code):
        return self.get(collectionCode=collection_code)

    def update_game_collection(self, collection_code, **kwargs):
        game_collection = self.get_game_collection_by_id(collection_code)
        for key, value in kwargs.items():
            if hasattr(game_collection, key):
                setattr(game_collection, key, value)
        game_collection.save()
        return game_collection

    def delete_game_collection(self, collection_code):
        game_collection = self.get_game_collection_by_id(collection_code)
        game_collection.delete()
# Create your models here.
class GameCollection(models.Model):
    collectionCode = models.AutoField(primary_key=True)
    collectionName = models.CharField(max_length=30,default='Default Collection',unique=True)
    game = models.ForeignKey(GameModel, on_delete=models.CASCADE)
    user = models.ForeignKey("customUser.User", on_delete=models.CASCADE, null=True, blank=True)
    publisher = models.ForeignKey('GamePublisher.GamePublisher', on_delete=models.CASCADE, null=True, blank=True)
    objects = GameCollectionManager()

    def __str__(self):
        return self.collectionName
