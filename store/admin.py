from django.contrib import admin

from .models import Request
from .models.shoe import Shoe
from .models.category import Category
from .models.customer import Customer
from .models.order import Order


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


# Register your models here.
admin.site.register(Shoe, AdminProduct)
# admin.site.register(Category)
# admin.site.register(Order)
admin.site.register(Request)

