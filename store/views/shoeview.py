from django.http import Http404
from django.shortcuts import render
from django.views import generic

from store.models.shoe import Shoe


def product_detail_view(request, product_id):
    try:
        product = Shoe.objects.get(pk=product_id)
    except Shoe.DoesNotExist:
        raise Http404("Product does not exist")

    return render(request, 'shop/shop_extended.html', context={'product': product})
