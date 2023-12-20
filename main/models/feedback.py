from django.db import models
from django.utils.translation import gettext_lazy as _


class Feedback(models.Model):
    email = models.EmailField(max_length=255)
    message = models.TextField()

    class Meta:
        verbose_name = _('Feedback')
        verbose_name_plural = _('Feedbacks')

    def __str__(self):
        return f"{self.email}"
