from django.db import models
from main.models.partner import Partner
from main.models.category import Category


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    productivity = models.CharField(max_length=255)
    growth_zone = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    data_json = models.JSONField(null=True, blank=True)
    partner_id = models.ForeignKey(Partner, on_delete=models.CASCADE, null=True, blank=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f"{self.name}"
