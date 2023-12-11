from django.db import models


class Feedback(models.Model):
    email = models.EmailField(max_length=255)
    message = models.TextField()

    class Meta:
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedbacks'

    def __str__(self):
        return f"{self.email}"
