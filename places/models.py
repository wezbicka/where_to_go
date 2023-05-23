from django.db import models

class Place(models.Model):
    title = models.CharField('Название', max_length=200)
    description_short = models.TextField('Превью')
    description_long = models.TextField('Описание')
    longitude = models.FloatField('Широта')
    latitude = models.FloatField('Долгота')

    def __str__(self):
        return self.title
