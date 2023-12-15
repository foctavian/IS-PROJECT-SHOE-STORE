from django.shortcuts import render, redirect, HttpResponseRedirect

from accounts.models import User
from store.models.shoe import Shoe
from store.models.category import Category
from django.views import View


# Create your views here.
class Index(View):

    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1

            else:
                cart[product] = 1
        else:
            cart = {product: 1}

        request.session['cart'] = cart
        print('cart', request.session['cart'])
        return redirect('homepage')

    def get(self, request):
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')


def store(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    try:
        user = User.objects.get(pk=request.session.get('user'))
    except User.DoesNotExist:
        user = None
    if categoryID:
        products = Shoe.get_all_products_by_categoryid(categoryID)
    else:
        products = Shoe.get_all_products()
    print("You are: ", user)
    request.session['user'] = user
    data = {'products': products, 'user': user}

    return render(request, 'shop/master.html', data)


def men_store(request):
    products = Shoe.get_all_products()
    return render(request, 'shop/shop_extended.html', {'products': products})
