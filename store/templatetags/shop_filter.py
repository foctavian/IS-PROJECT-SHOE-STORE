from django import template

from store.models.shoe import Shoe
from store.models.category import Category

register = template.Library()


@register.filter(name='search')
def search(name):
    return Shoe.objects.filter(name=name)