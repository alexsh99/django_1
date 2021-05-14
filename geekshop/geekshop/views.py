from django.shortcuts import render
from basketapp.models import Basket
from mainapp.models import Product


def main(request):
    products = Product.objects.all()[:4]
    context = {
        'title': 'Магазин',
        'products': products,
        'basket_items': get_basket(request.user)
    }
    return render(request, 'index.html', context=context)


def contact(request):
    context = {
        'title': 'Контакты',
        'basket_items': get_basket(request.user)
    }
    return render(request, 'contact.html', context=context)


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    return []
