from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    age = models.IntegerField(default=0)
    refresh_token = models.TextField(default="")

    def __str__(self):
        return "{}".format(self.username)
