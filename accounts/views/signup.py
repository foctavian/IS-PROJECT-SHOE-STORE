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

        if password1 ==  password2 and password1 and password2:
            user = User(email=email, password=password1, last_name='tavi')
            user.save()
            return redirect('home')
        else:
            # Display the form errors
            print("coaie.....")

    else:
        form = CustomUserCreationForm()

    return render(request, 'signup.html', {'form': form})
