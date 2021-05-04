from django.shortcuts import render


# Create your views here.

def main(request):
    context = {
        'title': 'Магазин'
    }
    return render(request, 'index.html', context=context)


def contact(request):
    context = {
        'title': 'Контакты'
    }
    return render(request, 'contact.html', context=context)
