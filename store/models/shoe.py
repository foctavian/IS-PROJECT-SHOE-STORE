from django.db import models
from .category import Category
from .brand import Brand
from .gender import Gender
from django import template

class Shoe(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    images = models.ImageField(upload_to='shoes', default='')
    sizes = models.CharField(max_length=100, default=0)
    quantity = models.IntegerField(default=0)
    colors = models.CharField(max_length=500, default=0)
    description = models.CharField(max_length=500, default=0)
    brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING)
    gender = models.ForeignKey(Gender, on_delete=models.DO_NOTHING, default='UNISEX')

    @staticmethod
    def get_products_by_ids(ids):
        return Shoe.objects.filter(id__in=ids)

    @staticmethod
    def get_all_products():
        return Shoe.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(categoryid):
        if categoryid:
            return Shoe.objects.filter(category=categoryid)
        else:
            return Shoe.get_all_products()

    @staticmethod
    def parse_sizes(name):
        shoe = Shoe.objects.get(name=name)
        sizes = shoe.size.split(',')
        return sizes

    @staticmethod
    def parse_colors(name):
        shoe = Shoe.objects.get(name=name)
        colors = shoe.colors.split(',')
        return colors



    def get_absolute_url(self):
        return f"product/{self.id}"
