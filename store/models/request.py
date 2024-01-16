from django.db import models
from .shoe import Shoe


class Request(models.Model):
    product_id = models.ForeignKey(Shoe, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    colors = models.CharField(max_length=500, default=0)
    sizes = models.CharField(max_length=100, default=0)
    brand = models.CharField(max_length=100, default=0)

    @staticmethod
    def get_all_requests():
        return Request.objects.all()
