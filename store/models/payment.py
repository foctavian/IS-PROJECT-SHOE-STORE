from django.db import models


class Payment(models.Model):
    CASH = 'CASH'
    CARD = 'CARD'

    payment_choices = [
        (CASH, 'CASH'),
        (CARD, 'CARD')
        ]

    payment_method = models.CharField(max_length=100, choices=payment_choices, default='CASH')
    status = models.BooleanField(default=False)