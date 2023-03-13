from django.db import models

# Create your models here.
class Login(models.Model):
    email = models.EmailField(max_length= 254)
    password = models.CharField(max_length=254)
    
    def __str__(self):
        return self.email


    class Meta:
        ordering = ['email']