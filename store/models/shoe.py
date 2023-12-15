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
    sale = models.BooleanField(default=0)

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

    def get_first_color(self):
        return self.colors.split(',')[0]

    @staticmethod
    def parse_colors(name):
        shoe = Shoe.objects.get(name=name)
        colors = shoe.colors.split(',')
        print(colors)
        return colors

    def get_absolute_url(self):
        return f"product/{self.id}"

    def compute_price_after_sale(self):
        self.price = self.price - (self.price * self.sale / 100)

    @staticmethod
    def insert_object(self):
        self.compute_price_after_sale()
        self.save()
