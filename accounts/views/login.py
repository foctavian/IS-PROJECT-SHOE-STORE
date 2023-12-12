from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from django.urls import reverse

from accounts.forms import CustomUserLoginForm
from accounts.models import User
from store.models.customer import Customer
from django.views import View


def login(request):
    form = None
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.get_user_by_email(email)
        if user:
            if password == user.password:
                request.session['user'] = user.id
                # return render(request, 'shop/master.html', {'user': user})
                return  redirect('store')
    else:
        form = CustomUserLoginForm()
    return render(request, 'login.html', {'form': form})


def logout(request):
    request.session.clear()
    return redirect('login')
