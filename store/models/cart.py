from django.db import models
from .shoe import Shoe
from accounts.models import User


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    item = models.ForeignKey(Shoe, on_delete=models.CASCADE, default=None)
    quantity = models.IntegerField(default=1)


def get_items_by_user(user_id):
    return Cart.objects.filter(user_id=user_id)


def delete_cart_after_order(user_id):
    Cart.objects.filter(user_id=user_id).delete()

