from shop.models import Product, Feedback, PricePlan
from django.contrib import admin

class FeedbackInline(admin.TabularInline):
    model = Feedback
    extra = 0
    readonly_fields = ('user','rating', 'comment', 'created')
    can_delete = False


class PricePlanInline(admin.TabularInline):
    model = PricePlan
    extra = 0
    fields = ('duration', 'rental_price')
    show_change_link = True

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "is_available", 'buyout_price', 'image')
    list_filter = ('category', 'is_available')
    search_fields = ('name','description')
    list_editable = ('is_available',)
    inlines = (PricePlanInline,FeedbackInline,)

