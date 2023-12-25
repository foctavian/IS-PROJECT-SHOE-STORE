from django.shortcuts import render

from accounts.models import User
from store.models.shoe import Shoe


def search(request):
    query = request.GET.get('q')
    results = []
    try:
        user = User.objects.get(pk=request.session.get('user'))
    except User.DoesNotExist:
        user = None

    if query:
        results = Shoe.objects.filter(name__icontains=query)
    else:
        results = Shoe.objects.all()

    return render(request, 'shop/master.html', {'products': results, 'user':user})