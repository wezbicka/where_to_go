# Generated by Django 4.2 on 2023-08-14 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='file',
            field=models.ImageField(upload_to='', verbose_name='Картинка'),
        ),
    ]
