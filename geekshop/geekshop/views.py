from django.shortcuts import render
from basketapp.models import get_basket
from mainapp.models import Product


def main(request):
    products = Product.objects.all()[:4]
    context = {
        'title': 'Магазин',
        'products': products,
        'basket': get_basket(user=request.user)
    }
    return render(request, 'index.html', context=context)


def contact(request):
    context = {
        'title': 'Контакты',
        'basket': get_basket(user=request.user)
    }
    return render(request, 'contact.html', context=context)
