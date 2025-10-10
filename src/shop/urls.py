from django.urls import path
from shop.views import home_view, product_list_view

urlpatterns = [
    path('home', home_view, name='home'),
    path('products/', product_list_view, name='product_list')
]