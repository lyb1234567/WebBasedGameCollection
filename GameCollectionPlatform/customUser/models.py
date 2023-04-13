from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.conf import settings
import os
class UserManger(BaseUserManager):
    print('Test:',settings.MEDIA_ROOT)
    def _create_user(self, username, email, password, firstName, lastName, userType, profilePic, userInfo, dateOfBirth,
                     is_staff,is_superuser , **extra_fields):
        if not username:
            raise ValueError("Username is not Valid")
        email = self.normalize_email(email)
        user =  self.model(username=username, email=email, firstName=firstName,lastName=lastName,
                           is_staff=is_staff, is_active=True ,is_superuser=is_superuser,
                           userType=userType, profilePic=profilePic, userInfo=userInfo,dateOfBirth=dateOfBirth,**extra_fields)
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_user(self, username, email,password,firstName,lastName,profilePic,userInfo,dateOfBirth,userType, **extra_fields):
        return self._create_user(username=username,email=email,password=password,firstName=firstName,
                                 lastName=lastName,userType=userType,profilePic=profilePic,dateOfBirth=dateOfBirth,userInfo=userInfo,
                                 is_staff=False, is_superuser=False,
                                 **extra_fields)
    

    def create_superuser(self, username, email, password, firstName=None,lastName=None, **extra_fields):
        if firstName is None:
            firstName = username
        if lastName is None:
            lastName= username
        user = self._create_user(username, email, password, firstName=firstName,
                                lastName='', userType="Admin", profilePic=None, userInfo="SuperUser",
                                dateOfBirth=timezone.now(), is_superuser=True, is_staff=True,
                                **extra_fields)
        user.is_active = True
        user.save(using=self._db)
        return user

def user_profile_pic_path(instance, filename):
    return os.path.join('profilePics', f'user_{instance.pk}', filename)
class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    firstName = models.CharField(max_length=30, blank=True, null=True)
    lastName = models.CharField(default='',max_length=30, blank= True, null=True)
    userType = models.CharField(max_length=20,default='Player',blank= True, null=True)
    profilePic = models.ImageField(upload_to='user_profile_pic_path',default=None,blank=True, null=True,max_length=1000,)
    userInfo = models.TextField(default='',max_length=500,blank=True, null=True)
    dateOfBirth = models.DateField(default=None,blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    location = models.CharField(max_length=254,blank=True, null=True)
    objects = UserManger()
    USERNAME_FIELD  = 'username'
    REQUIRED_FIELDS = ['email']