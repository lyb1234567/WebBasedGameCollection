from django.db import models
from django.contrib.auth.hashers import make_password
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import re
import os
class PublisherManager(models.Manager):
    
    def is_password_complex(self,password):
        if len(password) < 8:
            return False
        if not re.search(r'[A-Z]', password):
            return False
        if not re.search(r'[a-z]', password):
            return False
        if not re.search(r'[0-9]', password):
            return False
        if not re.search(r'\d', password):
            return False
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            return False
        return True
    
    def create(self, pubPassword, pubEmail, profilePicture=None, publisherDescription='', publisherInfo=''):
        try:
            validate_email(pubEmail)
        except ValidationError:
            raise ValueError("Invalid email address")
        
        if not self.is_password_complex(pubPassword):
                raise ValueError("Password does not meet complexity requirements")
        
        hashed_password = make_password(pubPassword)

        # Create the new publisher instance
        publisher = GamePublisher(
            pubPassword=hashed_password,
            pubEmail=pubEmail,
            profilePicture=profilePicture,
            publisherDescription=publisherDescription,
            publisherInfo=publisherInfo
        )
        
        # Save the instance to the database
        publisher.save(using=self._db)
        return publisher

def publisher_profile_pic_path(instance, filename):
    return os.path.join('publisherProfilePics', f'user_{instance.pk}', filename)
# Create your models here.
class GamePublisher(models.Model):
    publisherCode = models.AutoField(primary_key=True)
    pubPassword = models.CharField(max_length=255)
    pubEmail = models.EmailField(unique=True)
    profilePicture = models.ImageField(upload_to='publisher_profile_pic_path',default=None,blank=True, null=True,max_length=1000,)
    publisherDescription = models.TextField()
    publisherInfo = models.TextField()
    objects = PublisherManager()