from django.db import models

class Place(models.Model):
    title = models.CharField('Название', max_length=200)
    description_short = models.TextField('Превью')
    description_long = models.TextField('Описание')
    longitude = models.FloatField('Широта')
    latitude = models.FloatField('Долгота')

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
    file = models.FileField("Картинка", upload_to="media")

    def __str__(self):
        return f"{self.order_number} {self.place.title}"
    