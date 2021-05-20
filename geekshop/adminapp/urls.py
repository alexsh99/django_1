import adminapp.views as adminapp
from django.urls import path

app_name = 'adminapp'

urlpatterns = [
    path('user/create/', adminapp.user_create, name='user_create'),
    path('user/read/', adminapp.users, name='users'),
    path('user/update/<int:user_id>/', adminapp.user_update, name='user_update'),
    path('user/delete/<int:user_id>/', adminapp.user_delete, name='user_delete'),

    path('categories/create/', adminapp.category_create, name='category_create'),
    path('categories/read/', adminapp.categories, name='categories'),
    path('categories/update/<int:cat_id>/', adminapp.category_update, name='category_update'),
    path('categories/delete/<int:cat_id>/', adminapp.category_delete, name='category_delete'),

    path('products/create/category/<int:product_id>', adminapp.product_create, name='product_create'),
    path('products/read/category/<int:product_id>', adminapp.products, name='products'),
    path('products/read/<int:product_id>', adminapp.product_read, name='product_read'),
    path('products/update/<int:product_id>/', adminapp.product_update, name='product_update'),
    path('products/delete/<int:product_id>/', adminapp.product_delete, name='product_delete'),
]
