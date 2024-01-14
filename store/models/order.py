from django.db import models

from accounts.models import User
from .shoe import Shoe
from .customer import Customer
import datetime
from .payment import Payment
from .shipment import ShipmentCompany

PLACED = 0
CANCELLED = -1
DELIVERED = 1
FINISHED = 2


class Order(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE, default=None)
    address = models.CharField(max_length=200, default='', blank=True)
    phone = models.CharField(max_length=10, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.IntegerField(default=PLACED)
    payment_method = models.ForeignKey(Payment,
                                       on_delete=models.CASCADE, default=None)
    shipment_company = models.ForeignKey(ShipmentCompany,
                                         on_delete=models.CASCADE, default=None)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(user_id):
        return Order.objects.filter(user=user_id).order_by('-date')


class OrderProduct(models.Model):
    product = models.ForeignKey(Shoe,
                                on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
