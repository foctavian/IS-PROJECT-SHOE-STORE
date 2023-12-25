from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render

from accounts.forms import CustomUserChangeForm
from accounts.models import User
from store.models.order import Order,OrderProduct


def account(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
        orders = Order.objects.filter(user_id=user_id).values_list('id', 'status', 'date')
        list_of_orders=[]
        for order in orders:
            products = OrderProduct.objects.get(order_id=order[0])
            list_of_orders.append(products)
        print(list_of_orders)
        return render(request, 'accounts/userconfig.html', context={'user': user, 'orders': list_of_orders})
    except User.DoesNotExist:
        raise Http404("User does not exist")


def settings(request, setting,user_id):
    try:
        user = User.objects.get(pk=user_id)
        form = CustomUserChangeForm()
        set_val = "" #used for dynamically rendering the html page
        if setting == 'password':
            set_val = "password"
        elif setting == 'email':
            set_val = "email"
        return render(request, 'accounts/settings.html', context={'user': user, 'form': form, 'setting':set_val})

    except User.DoesNotExist:
        raise Http404("User does not exist")

