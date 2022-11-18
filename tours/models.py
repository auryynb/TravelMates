from datetime import datetime, date
from django.db import models


class City(models.Model):
    city = models.CharField(max_length=50, primary_key=True)
    province = models.CharField(max_length=50, null=True)
    related_city = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to='image', null=True)
    description = models.CharField(max_length=1500, null=True)

    def __str__(self):
        return self.city


class Destination(models.Model):
    CATEGORY_CHOICE = [
        ('Wisata Alam', 'Wisata Alam'),
        ('Taman Bermain', 'Taman Bermain'),
        ('Tempat Bersejarah', 'Tempat Bersejarah'),
        ('Kebun Binatang', 'Kebun Binatang'),
        ('Wisata Seni', 'Wisata Seni'),
        ('Pusat Belanja', 'Pusat Belanja'),
        ('Bangunan Unik', 'Bangunan Unik'),
    ]
    name = models.CharField(max_length=200)
    categories = models.CharField(max_length=200, choices=CATEGORY_CHOICE, null=True)
    image_path = models.ImageField(upload_to='images')
    address = models.CharField(max_length=200)
    kecamatan = models.CharField(max_length=200, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    description = models.CharField(max_length=1500)
    opening_hours = models.TimeField(null=True)
    closing_hours = models.TimeField(null=True)
    price_min = models.IntegerField()
    price_max = models.IntegerField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return str([self.name, self.price_max])


class DestinationImages(models.Model):

class Accomodation(models.Model):
    accomodation_name = models.CharField(max_length=200, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    price_per_night = models.IntegerField()
    address = models.CharField(max_length=200)
    image_path = models.ImageField(upload_to='images')


class Transportation(models.Model):
    MODA_CHOICES = [
        ('BUS', 'Bus'),
        ('TRAIN', 'Kereta Api'),
        ('PLANE', 'Pesawat'),
    ]
    name = models.CharField(max_length=200, null=True)
    moda = models.CharField(max_length=200, choices=MODA_CHOICES)
    city_from = models.ForeignKey(City, on_delete=models.CASCADE)
    city_to = models.ForeignKey(City, related_name='city_to', on_delete=models.CASCADE)
    depart_time = models.TimeField()
    arrive_time = models.TimeField()
    duration = models.DurationField(null=True, blank=True)
    price_per_person = models.IntegerField()

    def save(self, *args, **kwargs):
        self.duration = datetime.combine(date.min, self.arrive_time) - datetime.combine(date.min, self.depart_time)
        super(Transportation, self).save(*args, **kwargs)

    def __str__(self):
        return str([self.name, self.city_from, self.city_to, self.price_per_person])


class RencanaWisata(models.Model):
    title = models.CharField(max_length=200, null=True)
    budget = models.CharField(max_length=200)
    city_start = models.ForeignKey(City, on_delete=models.CASCADE)
    city_dest = models.ForeignKey(City, related_name='city_dest', on_delete=models.CASCADE)
    days = models.IntegerField()
    destination = models.ManyToManyField(Destination)
    akomodasi = models.ManyToManyField(Accomodation)
    transportasi_pergi = models.ManyToManyField(Transportation)
    transportasi_pulang = models.ManyToManyField(Transportation, related_name='transport_pulang')
    total_cost = models.IntegerField(null=True)