from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class Cart(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='cart_items',
        verbose_name=_('User'),
    )
    product = models.ForeignKey(
        to = 'Product',
        on_delete=models.CASCADE,
        related_name='in_carts',
        verbose_name=_('Product'),
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Created'))

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"