from django.db import models
from .users import User


class Abstract(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    createat = models.DateTimeField(auto_now_add=True)
    modifiedat = models.DateTimeField(auto_now=True)


    class Meta:
        abstract = True


