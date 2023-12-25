from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from accounts.models import User


def _generate_random_sequence():
    import random
    from cryptography.fernet import Fernet

    key = random.randint(10000, 99999)
    return key


def send_email_for_settings_change_approval(request, user_id):
    if request.method == 'GET':
        user = User.objects.get(pk=user_id)
        subject = 'Settings change request'
        key = _generate_random_sequence()
        message = f'User {user.first_name} {user.last_name} has requested to change his password.\n\n KEY : {key}'
        email_to = user.email

        send_mail(
            subject,
            message,
            None,
            [email_to],
            fail_silently=False, )
        return redirect('validate-email-key', key=key)


def validate_settings_change_request(request, key):
    return render(request, 'accounts/validator.html', context={'key': key})
