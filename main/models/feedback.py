from django.db import models
from django.utils.translation import gettext_lazy as _


class Feedback(models.Model):
    email = models.EmailField(max_length=255, verbose_name=_('Email'))
    message = models.TextField(verbose_name=_('Message'))

    class Meta:
        verbose_name = _('Feedback')
        verbose_name_plural = _('Feedbacks')

    def __str__(self):
        return f"{self.email}"
