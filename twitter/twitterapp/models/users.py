from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(upload_to='media/avatar/', default='media/avatar/base.png')
    status = models.CharField(max_length=255)
    fon = models.ImageField(upload_to='media/avatar/', default='media/avatar/basefon.png')