from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class Duration(models.TextChoices):
    DAY = 'D', _('Day')
    WEEK = 'W', _('Week')
    MONTH = 'M', _('Month')

class PricePlan(models.Model):
    product = models.ForeignKey(
        to='Product',
        on_delete = models.CASCADE,
        related_name = 'price_plans',
        verbose_name = _('Product')
    )
    duration = models.CharField(
        max_length=10,
        choices=Duration.choices,
        verbose_name = _('Duration'),
    )
    rental_price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name = _('Rental price')
    )

    def __str__(self):
        return f"{self.product.name} - {self.get_duration_display()}: {self.rental_price}"

    def clean(self):
        super().clean()
        if self.rental_price <= 0:
            raise ValidationError({"rental_price": _("Rental price must be greater than 0.")})
