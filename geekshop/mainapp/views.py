import random
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from basketapp.models import Basket
from .models import ProductCategory
from .models import Product


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    return []


def get_hot_product():
    return random.sample(list(Product.objects.all()), 1)


def get_related(select_product):
    return Product.objects.filter(category=select_product.category).exclude(id=select_product.id)[:3]


@login_required
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
        'basket_items': get_basket(request.user),
    }
    return render(request, 'products_list.html', context=context)


@login_required
def product(request, pk):
    product = Product.objects.get(id=pk)
    context = {
        'product': product,
        'categories': ProductCategory.objects.all(),
        'basket_items': get_basket(request.user),
        'related': get_related(product),
        'hot': get_hot_product()
    }
    return render(request, 'products.html', context=context)
