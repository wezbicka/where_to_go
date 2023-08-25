from django.shortcuts import render
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
                        "detailsUrl": "static/places/moscow_legends.json"
                    }
                } for place in places
            ]
        }
    }
    return render(request, 'index.html', context)
