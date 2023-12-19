from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.forms import CustomUserChangeForm
from accounts.models import User
from accounts.serializers import UserSerializer


def user_config(request, user_id):
    if request.method == 'GET':
        try:
            user = User.objects.get(pk=user_id)
            return render(request, 'accounts/userconfig.html', context={'user': user})
        except User.DoesNotExist:
            raise Http404("User does not exist")
    else:
        pass


