# Generated by Django 4.1.2 on 2022-11-03 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0007_alter_transportation_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='categories',
            field=models.CharField(choices=[('1', 'Wisata Alam'), ('2', 'Taman Bermain'), ('3', 'Tempat Bersejarah'), ('4', 'Kebun Binatang'), ('5', 'Wisata Seni'), ('6', 'Pusat Belanja'), ('7', 'Bangunan Unik')], max_length=200, null=True),
        ),
    ]