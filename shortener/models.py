from django.db import models


class ShortenerURL(models.Model):
    url = models.CharField(max_length=120)
    shortcode = models.CharField(max_length=15, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url
