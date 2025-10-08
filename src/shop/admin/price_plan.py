from shop.models import PricePlan
from django.contrib import admin

@admin.register(PricePlan)
class PricePlanAdmin(admin.ModelAdmin):
    list_display = ('product', 'duration', 'rental_price')
    list_filter = ('product','duration')
    search_fields = ('product__name',)
    ordering = ('product', 'duration',)


