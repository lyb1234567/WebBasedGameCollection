from django.db import models
from Game.models import GameModel
class ReviewManager(models.Manager):
    def create_review(self, user, publisher,game, rate, content, status):
        review = self.model(
            user=user,
            publisher=publisher,
            game=game,
            rate=rate,
            content=content,
            status=status,
        )
        review.save()
        return review

    def update_review(self, reviewCode, **kwargs):
        review = self.get(reviewCode=reviewCode)
        for key, value in kwargs.items():
            setattr(review, key, value)
        review.save()
        return review

    def delete_review(self, reviewCode):
        review = self.get(reviewCode=reviewCode)
        review.delete()

# Create your models here.
class Review(models.Model):
    STATUS_CHOICES = [
        ('anonymous', 'Anonymous'),
        ('public', 'Public'),
    ]
    reviewCode = models.AutoField(primary_key=True)
    user = models.ForeignKey("customUser.User", on_delete=models.CASCADE, null=True, blank=True)
    publisher = models.ForeignKey('GamePublisher.GamePublisher', on_delete=models.CASCADE, null=True, blank=True)
    game = models.ForeignKey("Game.GameModel", on_delete=models.CASCADE,blank=True)
    rate = models.IntegerField()
    content = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='public')
    objects=ReviewManager()