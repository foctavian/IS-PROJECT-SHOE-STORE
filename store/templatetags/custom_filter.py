from django import template

from store.models.shoe import Shoe
from store.models.category import Category

register = template.Library()


@register.filter(name='currency')
def currency(number):
    return "RON " + str(number)


@register.filter(name='multiply')
def multiply(number, number1):
    return number * number1


@register.filter(name='total_price_per_multiple_products')
def total_price(amount, price):
    return amount * price


@register.filter(name="total_order_price")
def total_order_price(order):
    sum = 0


@register.filter(name="size_filter")
def size_filter(*filtered_sizes):
    shoe = Shoe.objects.all()
    sizes = shoe.size.split(',')  # REFACTOR THIS
    return [shoe for size in sizes if size in filtered_sizes]


@register.filter(name="name_filter")
def name_filter(name):
    return Shoe.objects.filter(name__icontains=name)


@register.filter(name="category_name")
def get_category_name(name):
    try:
        shoe = Shoe.objects.get(name=name)
        category = shoe.category.category
        return category
    except Shoe.DoesNotExist:
        return ''
