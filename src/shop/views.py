from django.shortcuts import render
from .models import Product


def home_view(request):
    return render(request, "home.html")


def product_list_view(request):
    products = Product.objects.all()
    return render(request, "product_list.html", {"products": products})

