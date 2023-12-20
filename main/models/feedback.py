from django.db import models


class Feedback(models.Model):
    phone_number = models.CharField(max_length=255)
    message = models.TextField()
    status = models.BooleanField(default=0)

    class Meta:
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedbacks'

    def __str__(self):
        return f"{self.phone_number}"
