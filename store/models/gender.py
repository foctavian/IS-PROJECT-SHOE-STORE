from django.db import models


class Gender(models.Model):
    MALE = 'MALE'
    FEMALE = 'FEMALE'
    UNISEX = 'UNISEX'

    GENDER_CHOICES = [
        (MALE, 'MALE'),
        (FEMALE, 'FEMALE'),
        (UNISEX, 'UNISEX')
    ]
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES, default='UNISEX')
