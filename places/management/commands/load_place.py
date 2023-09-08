import logging
import requests
import json

from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from django.core.exceptions import MultipleObjectsReturned

from places.models import Image, Place


class Command(BaseCommand):
    help = 'Add place and images to db from json.'

    def add_arguments(self, parser):
        parser.add_argument(
            '-p',
            '--path',
            help='Импортировать данные в формате JSON из локального файла. '
                 'Пример: python3 manage.py load_place -p FILE_PATH'
        )
        parser.add_argument(
            '-u',
            '--url',
            action='store',
            help='Импортировать данные в формате JSON по ссылке. '
                 'Пример: python3 manage.py load_place -u URL'
        )
        parser.add_argument(
            '-b',
            '--batch',
            action='store',
            help='Импортировать данные в формате JSON из локального файла batch.json. '
                 'Пример: python3 manage.py load_place -b batch.json'
        )

    def handle(self, *args, **options):
        if options['url']:
            import_place(options['url'], url=True)
        if options['path']:
            import_place(options['path'])
        if options['batch']:
            import_batch_places(options['batch'])


def import_batch_places(batch_path: str):
    with open(batch_path, 'r') as file:
        places_json_urls = json.load(file)
        for json_url in places_json_urls['places']:
            try:
                import_place(json_path=json_url, url=True)
            except (
                    requests.exceptions.HTTPError,
                    requests.exceptions.ReadTimeout,
            ):
                logging.exception(f'Не удалось загрузить файл {json_url}:')


def import_place(json_path: str, url=False):
    if url:
        response = requests.get(json_path)
        response.raise_for_status()
        imported_place = response.json()
    else:
        with open(json_path, 'r', encoding='utf-8') as file:
            imported_place = json.load(file)
    try:
        place, created = Place.objects.update_or_create(
            title=imported_place['title'],
            latitude=imported_place['coordinates']['lat'],
            longitude=imported_place['coordinates']['lng'],
            defaults={
                'description_long': imported_place.get('description_long', ''),
                'description_short': imported_place.get('description_short', ''),
            },
        )
        if not created:
            return
    except MultipleObjectsReturned:
        logging.exception(f'Найдены дубликаты места {imported_place["title"]}')
        return

    for number, image_url in enumerate(imported_place['imgs'], start=1):
        image_name = f'{imported_place["title"]}_{number}.jpg'
        try:
            fetch_image(place, image_url, image_name, number)
        except (
            requests.exceptions.HTTPError,
            requests.exceptions.ReadTimeout,
        ):
            logging.exception(
                f"Не получилось загрузить {number} фотографию для {imported_place['title']}"
            )


def fetch_image(place, image_url, image_name, number):
    image = requests.get(image_url)
    image.raise_for_status()
    Image.objects.create(
        place=place,
        order_number=number,
        file=ContentFile(
            image.content,
            name=image_name
        )
    )
