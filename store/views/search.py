import copy
import json

from django.core.serializers import serialize
from django.http import HttpResponsePermanentRedirect, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from accounts.models import User
from store.models.brand import Brand
from store.models.gender import Gender
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
    print(results)
    return render(request, 'shop/master.html', {'products': results, 'user': user})


def find_by_name(name, value, class_name):
    value = [val.upper() for val in value]
    return class_name.objects.get(**{name: value[0]}).id


@csrf_exempt
@require_POST
def apply_filters(request):
    data = json.loads(request.body)
    if data:
        filters = data.get('filters')
        key = ''
        products = []
        new_filters = copy.copy(filters)
        for k in filters.keys():
            match k:
                case 'gender':
                    key = 'gender'
                    val = filters[key]
                    new_filters[key] = find_by_name(key, val, Gender)
                case 'colors':
                    key = 'colors'
                    nk = 'colors__contains'
                    val = [val.lower().strip() for val in filters[key]]
                    new_filters[nk] = val
                    new_filters.pop(key)
                case 'brand':
                    key = 'brand'
                    val = filters[key]
                    new_filters[key] = find_by_name(key, val, Brand)

        products = Shoe.objects.filter(**new_filters)
        print(new_filters)
        print(products)
        try:
            user = User.objects.get(pk=request.session.get('user'))
        except User.DoesNotExist:
            user = None

        serialized_products = serialize('json',products)

        response = {
            'message':'fut pe mata coaie',
            'url' : 'signup',
            'products': serialized_products,
        }
        return JsonResponse(response)
    else:
        return JsonResponse({'error': 'Invalid data...'}, status=400)


def filtered_products(request):
    serialized_data = request.GET.get('data', '')
    json_data = json.loads(serialized_data)
    lst = json_data.get('data',{}) #list of dictionaries
    lopks = [item.get('pk') for item in lst]
    products = Shoe.objects.filter(pk__in=lopks)
    print(products.values())
    user = User.objects.get(pk=request.session.get('user'))
    return render(request, 'shop/master.html', {'products': products, 'user': user})
