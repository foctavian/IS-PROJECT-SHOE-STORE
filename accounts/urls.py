from django.urls import path

from .views.homepage import HomePage
from .views.login import logout, login
from .views.user_config import user_config

urlpatterns = [
    path('', HomePage.as_view(), name="home", ),
    path('login/', login, name="login",),
    path('logout', logout, name='logout',),
    path('user_config/<int:user_id>', user_config, name='user_config'),
]
