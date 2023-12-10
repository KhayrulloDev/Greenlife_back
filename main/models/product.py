from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50, db_index=True, blank=True, null=True)
    price = models.PositiveIntegerField(null=True, blank=True)
    description = models.TextField()
