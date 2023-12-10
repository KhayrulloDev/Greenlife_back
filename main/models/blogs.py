from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='pics')
    youtube_link = models.URLField(blank=True, null=True)