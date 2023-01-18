import pytest

from rest_framework.test import APIClient

from shortener.models import ShortenerURL

client = APIClient()


@pytest.mark.django_db
def test_create_shortcode():
    expected_json = {
        "url": "https://www.youtube.com/watch?v=_pyYJCsCka0",
    }

    response = client.post(
        "/shortener/api/v1/shortcode", data=expected_json, format="json"
    )

    data = response.data

    assert response.status_code == 201
    assert isinstance(response.data, dict)
    assert isinstance(data["shortcode"], str)


@pytest.mark.django_db
def test_get_shortcode():
    shortener_url = ShortenerURL.objects.create(
        url="https://www.youtube.com/watch?v=_pyYJCsCka0"
    )
    response = client.get(f"/shortener/api/v1/shortcode/{shortener_url.shortcode}/")

    assert response.status_code == 200
    assert isinstance(response.data, dict)
    assert response.data["url"], "https://www.youtube.com/watch?v=_pyYJCsCka0"
