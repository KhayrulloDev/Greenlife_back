from django.db import models
from main.models.product import Product


class File(models.Model):
    file = models.FileField(upload_to='pics')
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'File'
        verbose_name_plural = 'Files'

    def __str__(self):
        return f"{self.pk}"

