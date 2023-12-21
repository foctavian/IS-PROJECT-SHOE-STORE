from django import template
from store.models.shoe import Shoe

register = template.Library()


@register.simple_tag(name='total_order_price')
def total_order_price(order):
    pass


@register.simple_tag(name='product_name_by_id')
def product_name_by_id(product):
    return Shoe.objects.get(id=product).name
