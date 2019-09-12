from django.db import models
from django.contrib.auth.models import AbstractUser
from tinymce import HTMLField


class User(AbstractUser):
    device_id = models.CharField(max_length=250)
    balance = models.FloatField(default=0)
    platform = models.CharField(max_length=250)
    user_id = models.CharField(max_length=250, unique=True)

