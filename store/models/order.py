from django.db import models

from accounts.models import User
from .shoe import Shoe
from .customer import Customer
import datetime


class Order(models.Model):
    product = models.ForeignKey(Shoe,
                                on_delete=models.CASCADE)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE, default=None)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=200, default='', blank=True)
    phone = models.CharField(max_length=10, default='', blank=True)
    # date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(user_id):
        return Order.objects.filter(user=user_id).order_by('-date')
