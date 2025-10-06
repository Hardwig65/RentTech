from shop.models import PricePlan
from django.contrib import admin

@admin.register(PricePlan)
class PricePlanAdmin(admin.ModelAdmin):
    list_display = ('product', 'duration', 'rental_price')
    list_filter = ('product',)
    search_fields = ('product',)
    ordering = ('duration',)


