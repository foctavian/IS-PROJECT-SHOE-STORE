from django.http import Http404
from django.shortcuts import render, redirect
from django.views import generic

from accounts.models import User
from store.models.shoe import Shoe


def product_detail_view(request, product_id):
    try:
        user = request.session.get('user')
        product = Shoe.objects.get(pk=product_id)
    except Shoe.DoesNotExist:
        raise Http404("Product does not exist")
    except User.DoesNotExist:
        return redirect('login')
    return render(request, 'shop/shop_extended.html', context={'product': product, 'user': user})
