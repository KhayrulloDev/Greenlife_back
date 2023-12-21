from django.db import models
from django.utils.translation import gettext_lazy as _


class Review(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    email = models.EmailField(max_length=255, verbose_name=_('Email'))
    text_review = models.TextField(verbose_name=_('Text for Review'))
    reviewed_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Reviewed at'))

    class Meta:
        verbose_name = _('Review')
        verbose_name_plural = _('Reviews')

    def __str__(self):
        return f"{self.name}"

