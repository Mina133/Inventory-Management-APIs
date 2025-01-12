from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Role(models.Model):
    name = models.CharField(max_length=100, unique=True, default='user')
    description = models.CharField(max_length=100, unique=True, default='Normal User')

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100, unique=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name="users_role")

    def __str__(self):
        return self.username
