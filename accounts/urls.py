from django.urls import path

from .views.homepage import HomePage
from .views.login import logout, login

urlpatterns = [
    path('', HomePage.as_view(), name="home", ),
    path('login/', login, name="login",),
    path('logout', logout, name='logout',),
]
