from datetime import datetime
from django.db import models


class Review(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    text_review = models.TextField()
    reviewed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return f"{self.name}"

