from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from store.models.shoe import Shoe
from store.models.cart import Cart
from collections import Counter
from store.models.shipment import ShipmentCompany, SHIPMENT_CHOICES


class CartView(View):
    def get(self, request):
        user = request.session.get('user')
        cart_items = Cart.objects.filter(user_id=user)
        products = Shoe.objects.filter(id__in=cart_items.values_list('item_id'))

        return render(request, 'cart.html', {'products': products,
                                             'cart': cart_items.values_list('item_id', 'quantity'),
                                             'shipment': SHIPMENT_CHOICES})
