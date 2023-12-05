from django import template

register = template.Library()


@register.filter(name='currency')
def currency(number):
    return "Rs " + str(number)


@register.filter(name='multiply')
def multiply(number, number1):
    return number * number1


@register.filter(name='total_price_per_multiple_products')
def total_price(amount, price):
    return amount * price

@register.filter(name = "total_order_price")
def total_order_price(order):
    sum = 0

