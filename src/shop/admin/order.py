from django.contrib import admin
from shop.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("user", "product", "price_plan", "start_date", "end_date",)
    list_filter = ("price_plan__duration", "user", "product", "start_date",)
    search_fields = ("user__username", "product__name", "price_plan__duration",)
