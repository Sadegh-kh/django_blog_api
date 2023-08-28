from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=11, null=True, blank=True)
    job = models.CharField(max_length=150, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
