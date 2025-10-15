from os import remove

from django.urls import path
from shop.views import home_view, product_list_view, cart_view,remove_from_cart

urlpatterns = [
    path('home', home_view, name='home'),
    path('products/', product_list_view, name='product_list'),
    path('cart/', cart_view, name='cart_view'),
    path("cart/remove/<int:product_id>/", remove_from_cart, name="remove_from_cart")
]