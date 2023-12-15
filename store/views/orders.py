import json

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from accounts.models import User
from store.models.customer import Customer
from django.views import View
from store.models.shoe import Shoe
from store.models.order import Order
from store.middlewares.auth import auth_middleware
from store.models.cart import Cart


class OrderView(View):

    def get(self, request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        print(orders)
        return render(request, 'orders.html', {'orders': orders})


@csrf_exempt
@require_POST
def add_to_cart(request, product_id):
    try:
        data = json.loads(request.body)
        # data load ids so i have to get the objects
        item = data.get('item')
        user = data.get('user')
        quantity = data.get('quantity')
        user_ = User.objects.get(pk=user)
        item_ = Shoe.objects.get(pk=item)
        if not user or not item:
            return JsonResponse({'error': 'Invalid data...'}, status=400)
        cart_item = Cart.objects.create(
            user=user_,
            item = item_,
            quantity = quantity
        )
        cart_item.save()
        return JsonResponse({'message': 'Item added to cart successfully!', 'cart_item':cart_item.id})

    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid data...'}, status=400)
