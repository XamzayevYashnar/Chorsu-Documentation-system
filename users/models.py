from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class MainUser(AbstractUser):
    avatar = models.ImageField(upload_to="user/avatars", blank=True, null=True)