from django.shortcuts import render, redirect


def RequestView(View):
    def get(self, request):
        return render(request, 'shop/requests.html')
