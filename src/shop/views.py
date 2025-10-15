from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Cart, CartRental,PricePlan


def home_view(request):
    return render(request, "home.html")

@login_required(login_url="/auth/login/")
def product_list_view(request):
    products = Product.objects.all()
    return render(request, "product_list.html", {"products": products})

@login_required(login_url="/auth/login/")
def cart_view(request):
    product_id = request.GET.get("product_id")
    plan_id = request.GET.get("plan")


    if product_id:
        product = get_object_or_404(Product, id=product_id)

        if plan_id:
            price_plan = get_object_or_404(PricePlan, id=plan_id)
            CartRental.objects.get_or_create(
                user=request.user,
                product=product,
                price_plan=price_plan
            )
        else:
            Cart.objects.get_or_create(
                user=request.user,
                product=product
            )

        return redirect("cart_view")

    buyout_items = Cart.objects.filter(user=request.user)
    rental_items = CartRental.objects.filter(user=request.user)

    return render(request, "cart.html", {
        "buyout_items": buyout_items,
        "rental_items": rental_items,
    })

@login_required(login_url="/auth/login/")
def remove_from_cart(request, product_id):
    type_ = request.GET.get("type")
    plan_id = request.GET.get("plan")

    if type_ == "buyout":
        Cart.objects.filter(user=request.user, product_id=product_id).delete()
    elif type_ == "rental" and plan_id:
        CartRental.objects.filter(user=request.user, product_id=product_id, price_plan_id=plan_id).delete()

    return redirect("cart_view")




