from django.shortcuts import render
from mainapp.models import Product, ProductCategory


# Create your views here.

def main(request):
    products = Product.objects.all()[:4]
    context = {
        'title': 'Магазин',
        'products': products,
    }
    return render(request, 'index.html', context=context)


def contact(request):
    context = {
        'title': 'Контакты'
    }
    return render(request, 'contact.html', context=context)
