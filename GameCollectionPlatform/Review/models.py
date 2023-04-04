from django.db import models

# Create your models here.
class Review(models.Model):
    reviewCode = models.CharField(max_length=50, primary_key=True)
    user = models.ForeignKey("customUser.User", on_delete=models.CASCADE, null=True, blank=True)
    publisher = models.ForeignKey('GamePublisher.GamePublisher', on_delete=models.CASCADE, null=True, blank=True)
    rate = models.IntegerField()
    content = models.TextField()
    status = models.CharField(max_length=20)