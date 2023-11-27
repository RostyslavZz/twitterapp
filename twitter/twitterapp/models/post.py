from django.db import models
from .abstract import Abstract


class Post(Abstract):
    text = models.TextField()
    image = models.ImageField(upload_to='media/postimages/', null=True, blank=True)