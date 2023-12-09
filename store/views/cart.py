from django.shortcuts import render , redirect

from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from django.views import  View
from store.models.shoe import Shoe

class Cart(View):
    def get(self , request):
        ids = list(request.session.get('cart').keys())
        products = Shoe.get_products_by_ids(ids)
        print(products)
        return render(request , 'cart.html' , {'products' : products} )