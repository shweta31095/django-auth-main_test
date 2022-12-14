from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.db import models


class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class blog(models.Model):
    Title = models.CharField(max_length=100, null=False)
    Article = models.TextField(max_length=500, null=False)
    Date_Created = models.DateTimeField(default=datetime.utcnow)

    def __str__(self) -> str:
        return self.name
