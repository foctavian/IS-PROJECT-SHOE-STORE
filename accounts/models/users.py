from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.models.role import Role


class User(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
