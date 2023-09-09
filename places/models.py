from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('Название', max_length=200)
    short_description = models.TextField('Превью', blank=True)
    long_description = HTMLField('Описание', blank=True)
    longitude = models.FloatField('Долгота')
    latitude = models.FloatField('Широта')

    def __str__(self):
        return self.title
    

class Image(models.Model):
    order_number = models.PositiveIntegerField(
        'Порядковый номер',
        default=0,
        db_index=True,
        blank=True,
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
