from django.db import models


# Create your models here.
class GamePublisher(models.Model):
    publisherCode = models.AutoField(primary_key=True)
    pubPassword = models.CharField(max_length=255)
    pubEmail = models.EmailField(unique=True)
    profilePicture = models.ImageField(upload_to='publisher_pictures/', blank=True, null=True)
    publisherDescription = models.TextField()
    publisherInfo = models.TextField()