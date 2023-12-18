from django.db import models
'''
TODO
    - Get rid of status field
    - Add the fields to the table manually 
'''

FAN_COURIER = 'FAN_COURIER'
CARGUS = 'CARGUS'
DHL = 'DHL'
GLS = 'GLS'
SELF_PICKUP = 'SELF_PICKUP'
SHIPMENT_CHOICES = [
    (FAN_COURIER, 'FAN_COURIER'),
    (CARGUS, 'CARGUS'),
    (DHL, 'DHL'),
    (GLS, 'GLS'),
    (SELF_PICKUP, 'SELF_PICKUP')
]


class ShipmentCompany(models.Model):
    shipment_company = models.CharField(max_length=100, choices=SHIPMENT_CHOICES, default='FAN_COURIER')
    price = models.IntegerField(default=0)
