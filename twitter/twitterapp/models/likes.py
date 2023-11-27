from django.db import models
from .abstract import Abstract
from .post import Post


class Like(Abstract):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
