from django.contrib.auth.base_user import BaseUserManager
from rest_framework import serializers


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        print(f"DEBUG: Before normalize_email, self.model: {self.model}")
        email = self.normalize_email(email)
        print(f"DEBUG: After normalize_email, self.model: {self.model}")

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extras):
        extras.setdefault("is_staff", True)
        extras.setdefault("is_superuser", True)
        extras.setdefault("is_active", True)
        if extras.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True")
        if extras.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True")
        return self.create_user(email, password, **extras)
