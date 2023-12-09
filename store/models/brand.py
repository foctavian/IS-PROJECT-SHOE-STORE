from django.db import models


class Brand(models.Model):
    VANS = 'VANS'
    NIKE = 'NIKE'
    ADIDAS = 'ADIDAS'
    PUMA = 'PUMA'
    REEBOK = 'REEBOK'
    CONVERSE = 'CONVERSE'
    NEW_BALANCE = 'NEW BALANCE'
    ASICS = 'ASICS'
    UNDER_ARMOUR = 'UNDER ARMOUR'
    TIMBERLAND = 'TIMBERLAND'
    SALOMON = 'SALOMON'
    OTHER = 'OTHER'
    BRAND_CHOICES = [
        (VANS, 'VANS'),
        (NIKE, 'NIKE'),
        (ADIDAS, 'ADIDAS'),
        (PUMA, 'PUMA'),
        (REEBOK, 'REEBOK'),
        (CONVERSE, 'CONVERSE'),
        (NEW_BALANCE, 'NEW BALANCE'),
        (ASICS, 'ASICS'),
        (UNDER_ARMOUR, 'UNDER ARMOUR'),
        (TIMBERLAND, 'TIMBERLAND'),
        (SALOMON, 'SALOMON'),
    ]

    brand = models.CharField(max_length=100, choices=BRAND_CHOICES, default='OTHER')
