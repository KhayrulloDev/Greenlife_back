from django.db import models
from main.models.product import Product


class Order(models.Model):
    user_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13)
    email = models.EmailField(max_length=255)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.PositiveBigIntegerField(default=1)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f"{self.user_name}"