from django.urls import path

from .views.homepage import HomePage

urlpatterns = [
    path('', HomePage.as_view(), name="home",),
]
