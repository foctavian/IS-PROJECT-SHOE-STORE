from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils import timezone

from accounts.managers import CustomUserManager

CUSTOMER = 1
GUEST = 2
PROVIDER = 3
ADMIN = 4

ROLE_CHOICES = (
    (CUSTOMER, "customer"),
    (PROVIDER, "provider"),
    (ADMIN, "admin")
)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(("email address"), unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    date_joined = models.DateTimeField(default=timezone.now)
    role = models.IntegerField(choices=ROLE_CHOICES, default=CUSTOMER)
    password = models.CharField(max_length=128)
    phone = models.CharField(max_length=10, unique=True, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # a admin user; non super-user
    is_superuser = models.BooleanField(default=False)  # a superuser
    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ['password', 'first_name', 'last_name']

    objects = CustomUserManager()

    @staticmethod
    def validate_user_password(password1, password2):
        if len(password1) < 5 or password1 != password2:
            return False
        return True

    def __str__(self):
        return self.email

    @classmethod
    def get_user_by_email(self, email):
        try:
            return User.objects.get(email=email)
        except:
            return False

    @staticmethod
    def get_role_by_name(role):
        if role == 'customer':
            return CUSTOMER
        elif role == 'provider':
            return PROVIDER
