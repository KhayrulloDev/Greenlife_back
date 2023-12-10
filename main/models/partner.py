from django.db import models


class Partner(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='pics')
    youtube_link = models.URLField()

    class Meta:
        verbose_name = 'Partner'
        verbose_name_plural = 'Partners'

    def __str__(self):
        return f"{self.name}"
