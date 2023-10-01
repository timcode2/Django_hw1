from django.contrib.auth.models import AbstractUser
from django.db import models

from catalog.models import NULLABLE


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='email')

    phone = models.CharField(max_length=255, verbose_name='номер телефона', **NULLABLE)
    country = models.CharField(max_length=255, verbose_name='страна', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватара', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
