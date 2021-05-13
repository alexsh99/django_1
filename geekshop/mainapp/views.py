from django.shortcuts import render, get_object_or_404
from basketapp.models import get_basket
from .models import ProductCategory
from .models import Product


def products(request, index=None):
    if index is not None:
        category = get_object_or_404(ProductCategory, id=index)
        products = Product.objects.filter(category_id=index).order_by('price')
    else:
        products = Product.objects.all().order_by('price')
        category = {'name': 'все', 'id': 0}

    categories = ProductCategory.objects.all()
    context = {
        'title': 'Каталог',
        'categories': categories,
        'category': category,
        'products': products,
        'basket': get_basket(user=request.user)
    }
    return render(request, 'products_list.html', context=context)


def product(request, pk):
    context = {
        'product': Product.objects.get(id=pk),
        'categories': ProductCategory.objects.all(),
        'basket': get_basket(user=request.user)
    }
    return render(request, 'products.html', context=context)
