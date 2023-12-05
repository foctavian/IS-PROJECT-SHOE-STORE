from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils import timezone

from accounts.managers import CustomUserManager

CUSTOMER = 1
GUEST = 2
SELLER = 3
ADMIN = 4

ROLE_CHOICES = (
    (CUSTOMER, "customer"),
    (GUEST, "guest"),
    (SELLER, "seller"),
    (ADMIN, "admin")
)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(("email address"), unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=ADMIN)
    password = models.CharField(max_length=128)
    phone = models.CharField(max_length=10, unique=True, null=True, blank=True)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ['password']

    objects = CustomUserManager()

    @staticmethod
    def validate_user_password(password1, password2):
        if len(password1) < 5 or password1 != password2:
            return False
        return True

    def __str__(self):
        return self.email
