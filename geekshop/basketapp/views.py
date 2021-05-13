from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from basketapp.models import Basket, get_basket
from mainapp.models import Product


def basket(request):
    if request.user.is_authenticated:
        context = {
            'basket': get_basket(user=request.user),
            'basket_list': Basket.objects.filter(user=request.user)
        }
        return render(request, 'basket.html', context=context)
    return HttpResponseRedirect(reverse('authapp:login'))


def basket_add(request, pk):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, id=pk)
        basket = Basket.objects.filter(user=request.user, product=product).first()

        if not basket:
            basket = Basket(user=request.user, product=product)

        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def basket_remove(request, pk):
    pass
