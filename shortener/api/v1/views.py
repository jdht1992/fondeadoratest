from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.http import Http404

from shortener.api.v1.serializers import ShortenerURLModelSerializer, URLModelSerializer
from shortener.models import ShortenerURL


class ShortenerURLCreateAPIView(APIView):
    def post(self, request):
        serializer = ShortenerURLModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShortenerURLGetAPIView(APIView):
    def get_object(self, slug):
        try:
            return ShortenerURL.objects.filter(shortcode=slug).first()
        except ShortenerURL.DoesNotExist:
            raise Http404

    def get(self, request, slug):
        obj = self.get_object(slug)
        serializer = URLModelSerializer(obj)
        return Response(serializer.data)
