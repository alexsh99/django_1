from django.shortcuts import render


# Create your views here.

def products(request):
    context = {
        'title': 'Каталог',
        'menu': ['все', 'дом', 'офис', 'модерн', 'классика']
    }
    return render(request, 'products.html', context=context)
