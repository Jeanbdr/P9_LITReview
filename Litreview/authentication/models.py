from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.


class User(AbstractUser):
    following = models.ManyToManyField(
        "self", symmetrical=False, related_name="followed_by"
    )
