# Generated by Django 4.1.2 on 2022-12-08 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0009_remove_destinasi_rating_destinasi_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destinasi',
            name='album',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.DeleteModel(
            name='ImageAlbum',
        ),
    ]
