from django.db import models
from main.models.product import Product
from django.utils.translation import gettext_lazy as _


class Order(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    phone_number = models.CharField(max_length=13, verbose_name=_('Phone Number'))
    email = models.EmailField(max_length=255, verbose_name=_('Email'))
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_('Product ID'))
    count = models.PositiveBigIntegerField(default=1, verbose_name=_('Count'))

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    def __str__(self):
        return f"{self.name}"
