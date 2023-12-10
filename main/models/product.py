from django.db import models

from main.models.category import Category


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    productivity = models.CharField(max_length=255)
    growth_zone = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    description = models.TextField()
    data_json = models.JSONField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f"{self.name}"
