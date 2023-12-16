from django.template.defaulttags import url
from django.urls import path

from store.views.cart import CartView
from .middlewares.auth import auth_middleware
from .views.checkout import CheckOut
from .views.home import store, men_store
from .views.orders import add_to_cart, OrderView
from accounts.views.signup import signup
from store.views.shoeview import product_detail_view


urlpatterns = [
    path('store', store, name='store'),
    path('signup', signup, name='signup'),
    path('cart',CartView.as_view(), name='cart'),
    path('check-out', CheckOut.as_view(), name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
    path('product/<int:product_id>', product_detail_view, name='products_details'),
    path('product/<int:product_id>/add_to_cart', add_to_cart, name='add_to_cart'),
]
