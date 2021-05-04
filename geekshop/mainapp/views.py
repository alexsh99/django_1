from django.shortcuts import render
from .models import ProductCategory

# Create your views here.


def products(request):
    category = ProductCategory.objects.all()
    context = {
        'title': 'Каталог',
        'menu': category,
    }
    return render(request, 'products.html', context=context)
