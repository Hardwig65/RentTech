from django.contrib import admin
from shop.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("product", "user", "price_plan")
