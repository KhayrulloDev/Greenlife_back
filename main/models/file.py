from django.db import models
from main.models.product import Product
from django.utils.translation import gettext_lazy as _


class File(models.Model):
    file = models.FileField(upload_to='pics')
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('File')
        verbose_name_plural = _('Files')

    def __str__(self):
        return f"{self.pk}"

