from django.core.exceptions import ValidationError

from core import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from .base import TimeConfig

class Order(TimeConfig):
    product = models.ForeignKey(
        to = 'Product',
        on_delete=models.CASCADE,
        verbose_name = _('Product'),
        related_name = 'products'
    )
    user = models.ForeignKey(
        to = settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name = _('User'),
        related_name = 'orders'
    )
    price_plan = models.ForeignKey(
        to = 'PricePlan',
        on_delete=models.PROTECT,
        related_name = 'orders',
        verbose_name = _('Price plan'),
    )
    start_date = models.DateField(verbose_name=_("Start date"))
    end_date = models.DateField(verbose_name=_("End date"))

    def __str__(self):
        return f"{self.user} rented {self.product.name} ({self.price_plan.get_duration_display()})"

    # Валидация даты
    def clean(self):
        super().clean()
        if self.end_date <= self.start_date:
            raise ValidationError({"end_date": _("End date must be later than start date.")})
