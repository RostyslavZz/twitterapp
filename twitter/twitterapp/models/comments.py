from django.db import models
from .abstract import Abstract
from .post import Post


class Comment(Abstract):
    text = models.CharField(max_length=255)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)