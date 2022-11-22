from django.db import models

from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_restoran = models.BooleanField(default=False)
    is_kurir = models.BooleanField(default=False)
    is_pelanggan = models.BooleanField(default=False)