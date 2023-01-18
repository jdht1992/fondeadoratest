from django.contrib import admin

from shortener.models import ShortenerURL


class ShortenerURLAdmin(admin.ModelAdmin):
    list_display = ('url', 'shortcode', 'created_at',)


admin.site.register(ShortenerURL, ShortenerURLAdmin)
