from django.urls import path, re_path

from shortener.api.v1.views import ShortenerURLCreateAPIView, ShortenerURLGetAPIView

urlpatterns = [
    path("api/v1/shortcode", ShortenerURLCreateAPIView.as_view()),
    re_path("^api/v1/shortcode/(?P<slug>[\w-]+)/$", ShortenerURLGetAPIView.as_view()),
]
