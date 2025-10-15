from django.utils.translation import gettext_lazy as _
from django.db import models
from django.conf import settings



class CartRental(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="rental_cart",
        verbose_name=_("User")
    )
    product = models.ForeignKey(
        to = "Product",
        on_delete=models.CASCADE,
        related_name="rental_items",
        verbose_name=_("Product")
    )
    price_plan = models.ForeignKey(
        to = "PricePlan",
        on_delete=models.CASCADE,
        related_name="rental_cart_items",
        verbose_name=_("Rental plan")
    )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.product.name} ({self.price_plan.get_duration_display()})"