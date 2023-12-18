import json

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from accounts.models import User
from django.views import View
from store.models.shoe import Shoe
from store.models.order import Order
from store.models.cart import Cart
from store.models.cart import get_items_by_user

class OrderView(View):

    def get(self, request):
        customer = request.session.get('user')
        orders = Order.get_orders_by_customer(customer)
        print(orders)
        return render(request, 'orders.html', {'orders': orders})


@csrf_exempt
@require_POST
def add_to_cart(request, product_id):
    response = JsonResponse({'success': True})
    response['Access-Control-Allow-Origin'] = '*'
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

        # check for presence of item in cart
        cart = Cart.objects.filter(user=user_, item=item_)
        if not cart:
            cart_item = Cart.objects.create(
                user=user_,
                item=item_,
                quantity=quantity
            )
            cart_item.save()
            return JsonResponse({'message': 'Item added to cart successfully!', 'cart_item': cart_item.id})
        else:
            cart_item = cart.first()
            cart_item.quantity += quantity
            cart_item.save()
            return JsonResponse({'message': 'Increased quantity of item in cart successfully!', 'cart_item': cart_item.id})
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid data...'}, status=400)


@csrf_exempt
@require_POST
def order(request, user_id):
    try:
        #get the user
        data = json.loads(request.body)
        user = data.get('user')
        shipment = data.get('shipment-company')
        payment = data.get('payment')
        address = data.get('address')
        phone = data.get('phone')
        print(address)
        print(phone)
        # if user == user_id:
        #     cart_items = get_items_by_user(user_id)
        #     for item in cart_items:
        #         order = Order.objects.create()
        #
        #     # order = Order.objects.create(
        #     #     user_id=user,
        #     #     shipment_company_id=shipment,
        #     #     payment_method_id=payment
        #     # )
        # else: raise Exception('Invalid user')

        return JsonResponse({'message': 'Order placed successfully!'})
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid data...'}, status=400)
