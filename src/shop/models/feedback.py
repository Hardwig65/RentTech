from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from shop.models.base import TimeConfig


class Feedback(TimeConfig):
    user = models.ForeignKey(
        to = settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="feedbacks",
        verbose_name=_("User"),
    )
    product = models.ForeignKey(
        to = 'Product',
        on_delete=models.CASCADE,
        related_name='feedbacks',
        verbose_name=_("Product"),
    )
    rating = models.PositiveSmallIntegerField(
        verbose_name=_("Rating"),
        help_text=_('Rating beetween 1 and 5')
    )
    comment = models.TextField(
        max_length=250,
        blank=True,
        null=True,
        verbose_name=_("Comment"),
    )
    def __str__(self):
        return f"{self.user} → {self.product.name}: {self.rating}/5"

    #Валидация рейтинга
    def clean(self):
        super().clean()
        if not (1 <= self.rating <= 5):
            raise ValidationError({"rating": _("Rating must be between 1 and 5.")})

