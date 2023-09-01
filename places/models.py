from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('Название', max_length=200)
    description_short = models.TextField('Превью', blank=True)
    description_long = HTMLField('Описание', blank=True)
    longitude = models.FloatField('Долгота')
    latitude = models.FloatField('Широта')
    place_id = models.CharField('ID места', max_length=200, null=True)

    def __str__(self):
        return self.title
    

class Image(models.Model):
    order_number = models.PositiveIntegerField(
        'Порядковый номер',
        default=0,
        db_index=True,
    )
    place = models.ForeignKey(
        Place,
        verbose_name='Место',
        related_name='images',
        on_delete=models.CASCADE
    )
    file = models.ImageField("Картинка",)

    def __str__(self):
        return f"{self.order_number} {self.place.title}"
    
    class Meta:
        ordering = ['order_number']
