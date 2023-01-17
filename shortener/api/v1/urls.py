from django.urls import path

from shortener.api.v1.views import ShortenerURLCreateAPIView

urlpatterns = [
    path('api/v1/shortcode', ShortenerURLCreateAPIView.as_view()),
]
