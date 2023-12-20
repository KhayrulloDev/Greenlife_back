from django.db import models
from django.utils.translation import gettext_lazy as _

class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='pics')
    youtube_link = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = _('Blog')
        verbose_name_plural = _('Blogs')

    def __str__(self):
        return f"{self.title}"
