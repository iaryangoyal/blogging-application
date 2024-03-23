from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class User_login(AbstractBaseUser):
    name = models.CharField(max_length = 50)
    email = models.EmailField(unique = True)
    password = models.CharField(max_length=128)
    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ('',)