from django.db import models


# Create your models here.
class City(models.Model):
    city = models.CharField(max_length=50, primary_key=True)
    related_city = models.CharField(max_length=50, blank=True)


class Destination(models.Model):
    name = models.CharField(max_length=200)
    image_path = models.ImageField(upload_to='images')
    address = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    # related_cities = models.ForeignKey(City, to_field='related_city', related_name='related_cities', on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    opening_hours = models.TimeField(null=True)
    closing_hours = models.TimeField(null=True)
    price_min = models.IntegerField()
    price_max = models.IntegerField()
