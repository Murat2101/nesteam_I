from django.contrib.auth.models import AbstractUser
from django.db import models


class Player(models.Model):
    nick = models.CharField(max_length=55)


class UserFactory:
    pass
