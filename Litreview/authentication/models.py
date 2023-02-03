from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    pass
    # email = None
    # username = models.CharField(unique=True, max_length=30)
