from rest_framework import serializers

from shortener.models import ShortenerURL


class ShortenerURLModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortenerURL
        fields = ["url", "shortcode"]
        extra_kwargs = {
            "url": {"write_only": True},
            "shortcode": {"read_only": True},
        }


class URLModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortenerURL
        fields = ["url"]
