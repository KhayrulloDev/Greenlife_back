from datetime import datetime

from django.db import models


class Review(models.Model):
    user_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    text_review = models.TextField()
    reviewed_at = models.DateTimeField(auto_now_add=True, default=datetime.utcnow)

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return f"{self.user_name}"

