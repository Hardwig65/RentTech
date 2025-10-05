from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db import models
from shop.models.base import TimeConfig

class ProductCategory(models.TextChoices):
    LAPTOP = 'LP', _('Laptop')
    PHONE = 'PN', _('Phone')
    CONSOLE = 'CNS', _('Console')
    WATCH = 'WCH', _('Watch')
    HOME = 'HM', _('Home')
    OTHER = 'OT', _('Other')
    DEFAULT = 'DF', _('Default')

class Product(TimeConfig):
    name = models.CharField(max_length=25, verbose_name=_('Name'))
    description = models.CharField(max_length=200,null=True, blank = True, verbose_name=_('Description'))
    image = models.ImageField(upload_to = 'products/', null=True, blank=True, verbose_name=_('Image'))
    is_available = models.BooleanField(default=True, verbose_name=_('Is available'))
    category = models.CharField(choices = ProductCategory,default = ProductCategory.DEFAULT, verbose_name=_('Category'))
    buyout_price = (models.DecimalField(
        max_digits = 8,
        decimal_places = 2
        ,null=True,
        blank=True,
        verbose_name=_('Buyout price')))

    def __str__(self):
        return self.name

    # Цена аренды по ключу day week и т д
    def get_rental_price_for(self, duration: str):
        plan = self.price_plans.filter(duration=duration).first()
        return plan.rental_price if plan else None

    # Все тарифы аренды
    def get_all_prices(self):
        return {plan.duration: plan.rental_price for plan in self.price_plans.all()}

    def clean(self):
        super().clean()
        if self.buyout_price is not None and self.buyout_price <= 0:
            raise ValidationError({"buyout_price": _("Buyout price must be greater than 0.")})