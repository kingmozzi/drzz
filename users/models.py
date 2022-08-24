from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager

class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    birth = models.CharField(max_length=100, default="")
    age = models.IntegerField(default=0)
    sex = models.CharField(max_length=100, default="")

    taste = models.FloatField(default=0.5)
    atmosphere = models.FloatField(default=0.5)
    service = models.FloatField(default=0.5)
    price = models.FloatField(default=0.5)

    #star_rating = models.FloatField(default=0)

    mucket = models.CharField(max_length=1000, default="", blank=True)
    friend = models.CharField(max_length=1000, default="", blank=True)
    
    def __str__(self):
        return self.email


#from django.contrib.auth.models import BaseUserManager, PermissionsMixin, AbstractBaseUser

# from django.db import models

# class UserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password=password)
#         user.save(using=self._db)

#         return user

# class User(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(max_length=255, unique=True)
#     name = models.CharField(max_length=255)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     uid = models.CharField(max_length=200)
#     age = models.IntegerField(default=0)
#     sex = models.CharField(max_length=100)
#     taste = models.FloatField(default=0.0)
#     waiting = models.FloatField(default=0.0)
#     service = models.FloatField(default=0.0)
#     price = models.FloatField(default=0.0)
#     feeling = models.FloatField(default=0.0)
#     mucket = models.CharField(max_length=1000)
#     object = UserManager()

#     USERNAME_FIELD = 'email'

# class User(models.Model, AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(max_length=255, unique=True)
#     name = models.CharField(max_length=200)
#     uid = models.CharField(max_length=200)
#     age = models.IntegerField(default=0)
#     sex = models.CharField(max_length=100)
#     taste = models.FloatField(default=0.0)
#     waiting = models.FloatField(default=0.0)
#     service = models.FloatField(default=0.0)
#     price = models.FloatField(default=0.0)
#     feeling = models.FloatField(default=0.0)
#     mucket = models.CharField(max_length=1000)
#     course = models.CharField(max_length=1000)

#     object = UserManager()


#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ('user',)