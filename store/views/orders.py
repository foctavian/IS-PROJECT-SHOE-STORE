import json
from datetime import datetime

from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from accounts.models import User
from django.views import View
from store.models.shoe import Shoe
from store.models.order import Order, OrderProduct, PLACED, CANCELLED, DELIVERED, FINISHED
from store.models.cart import Cart, delete_cart_after_order
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
            return JsonResponse(
                {'message': 'Increased quantity of item in cart successfully!', 'cart_item': cart_item.id})
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid data...'}, status=400)


@csrf_exempt
@require_POST
def order(request, user_id):
    try:
        # get the user
        data = json.loads(request.body)
        user = data.get('user')
        shipment = data.get('shipment-company')
        payment = data.get('payment')
        address = data.get('address')
        phone = data.get('phone')

        if user == user_id:
            date = datetime.today()
            cart_items = get_items_by_user(user_id)

            Order.objects.create(
                user_id=user,
                address=address,
                phone=phone,
                date=date,
                status=PLACED,
                payment_method_id=1,
                shipment_company_id=1
            )
            order_id = Order.objects.get(user_id=user_id, date=date)

            for item in cart_items:
                shoe = Shoe.objects.get(id=int(item['item_id']))
                order_product = OrderProduct.objects.create(
                    product=shoe,
                    price=0,
                    quantity=item['quantity'],
                    order_id=order_id
                )
                order_product.save()
            # delete the cart after order
            delete_cart_after_order(user_id)
            return HttpResponseRedirect(reverse('store'))
        else:
            raise Exception('Invalid user')
    except json.JSONDecodeError:
        return JsonResponse({'error': 'INVALID DATA...'}, status=400)
