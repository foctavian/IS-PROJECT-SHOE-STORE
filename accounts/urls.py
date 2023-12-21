from django.urls import path

from .views.homepage import HomePage
from .views.login import logout, login
from .views.user_config import account

urlpatterns = [
    path('', HomePage.as_view(), name="home", ),
    path('login/', login, name="login",),
    path('logout', logout, name='logout',),
    path('account/<int:user_id>', account, name='account'),
]
