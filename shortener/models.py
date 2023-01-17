import random
import string

from django.db import models


def code_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class ShortenerURL(models.Model):
    url = models.CharField(max_length=120)
    shortcode = models.CharField(max_length=15, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url

    def save(self, *args, **kwargs):
        self.shortcode = code_generator()
        super(ShortenerURL, self).save(*args, **kwargs)
