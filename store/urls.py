from django.urls import path

from store.views.cart import Cart
from store.views.login import Login, logout
from .middlewares.auth import auth_middleware
from .views.checkout import CheckOut
from .views.home import store
from .views.orders import OrderView
from accounts.views.signup import signup


urlpatterns = [
    # path('', Index.as_view(), name='homepage'),
    path('store', store, name='store'),

    path('signup', signup, name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('cart', auth_middleware(Cart.as_view()), name='cart'),
    path('check-out', CheckOut.as_view(), name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
]
