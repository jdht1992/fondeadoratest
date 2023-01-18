from django.urls import path

from shortener.api.v1.views import ShortenerURLCreateAPIView, ShortenerURLGetAPIView

urlpatterns = [
    path("api/v1/shortcode", ShortenerURLCreateAPIView.as_view()),
    path("api/v1/shortcode/<slug:slug>/", ShortenerURLGetAPIView.as_view()),
]
