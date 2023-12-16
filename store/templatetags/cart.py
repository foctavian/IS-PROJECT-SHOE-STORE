from django import template

register = template.Library()


@register.filter(name='is_in_cart')
def is_in_cart(product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return True
    return False;


@register.filter(name='cart_quantity')
def cart_quantity(product, cart):
    for id, q in cart:
        if int(id) == product:
            return q


@register.simple_tag(name='price_total')
def price_total( price,product_id,cart):
    for id,q in cart:
        if id == product_id:
            return price * q


@register.filter(name='total_cart_price')
def total_cart_price(products, cart):
    return 0
