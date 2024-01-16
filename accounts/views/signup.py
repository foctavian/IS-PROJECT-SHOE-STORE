from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

from accounts.forms import CustomUserCreationForm
from accounts.managers import CustomUserManager
from accounts.models import User


def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        role = request.POST.get('role')
        role = User.get_role_by_name(role)
        if password1 ==  password2 and password1 and password2:
            user = User(email=email, password=password1, last_name=last_name, first_name=first_name, role=role)
            user.save()
            return redirect('home')
        else:
            # Display the form errors
            print("error")

    else:
        form = CustomUserCreationForm()

    return render(request, 'signup.html', {'form': form})
