from django.db import models
from .shoe import Shoe
from accounts.models import User


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    item = models.ForeignKey(Shoe, on_delete=models.CASCADE, default=None)
    quantity = models.IntegerField(default=1)

