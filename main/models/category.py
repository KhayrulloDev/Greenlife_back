from mptt.models import MPTTModel, TreeForeignKey
from django.db import models


class Category(MPTTModel):
    name = models.CharField(max_length=50, blank=True, null=True)
    parent = TreeForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

