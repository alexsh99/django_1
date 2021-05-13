from django.db import models
from geekshop import settings
from mainapp.models import Product
from authapp.models import ShopUser


def get_basket(user: ShopUser):
    result = {
        'count': 0,
        'price': 0,
    }
    if user.is_authenticated:
        basket = Basket.objects.filter(user=user)
        for item in basket:
            result["price"] += item.product.price * item.quantity
            result["count"] += item.quantity
    return result


class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)
    add_datetime = models.DateTimeField(verbose_name='время', auto_now_add=True)
