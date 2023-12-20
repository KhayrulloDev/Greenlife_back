from django.db import models
from main.models.product import Product
from django.utils.translation import gettext_lazy as _


class Order(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13)
    email = models.EmailField(max_length=255)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.PositiveBigIntegerField(default=1)

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    def __str__(self):
        return f"{self.name}"
