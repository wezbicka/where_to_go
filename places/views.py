from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.urls import reverse

from .models import Place


def index(request):
    places = Place.objects.all()
    context = {
        "places": {
            "type": "FeatureCollection",
            "features": [
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [place.longitude, place.latitude]
                    },
                    "properties": {
                        "title": place.title,
                        "placeId": place.place_id,
                        "detailsUrl": reverse("place-detail", args=[place.id])
                    }
                } for place in places
            ]
        }
    }
    return render(request, 'index.html', context)


def place_detail(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    return JsonResponse(
        {
            "title": place.title,
            "imgs": [image.file.url for image in place.images.all()],
            "description_short": place.description_short,
            "description_long": place.description_long,
            "coordinates": {
                "lng": place.longitude,
                "lat": place.latitude
            }
        },
        safe=False,
        json_dumps_params={'ensure_ascii': False, 'indent': 2}
    )