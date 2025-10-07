from shop.models import Feedback
from django.contrib import admin

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("user", "product", "comment", 'rating')
    list_filter = ("user",'product','rating')
    search_fields = ("rating",'product',)