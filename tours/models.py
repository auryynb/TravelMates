from datetime import datetime, date
from django.db import models


class City(models.Model):
    city = models.CharField(max_length=50, primary_key=True)
    province = models.CharField(max_length=50, null=True)
    related_city = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to='image', null=True)
    description = models.CharField(max_length=1500, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.city


class ImageAlbum(models.Model):
    def default(self):
        return self.images.filter(default=True).first()

    def thumbnails(self):
        return self.images.filter(width__lt=100, length_lt=100)


class Image(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    default = models.BooleanField(default=False)
    width = models.FloatField(default=100)
    length = models.FloatField(default=100)
    album = models.ForeignKey(ImageAlbum, related_name='images', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


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
    album = models.OneToOneField(ImageAlbum, related_name='model', on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=200)
    maps = models.CharField(max_length=1500, null=True)
    panorama = models.CharField(max_length=1500, null=True)
    kecamatan = models.CharField(max_length=200, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    description = models.CharField(max_length=22200, null=True)
    opening_hours = models.TimeField(null=True)
    closing_hours = models.TimeField(null=True)
    price_min = models.IntegerField()
    price_max = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return str([self.name, self.city, self.price_max])


class Accomodation(models.Model):
    accomodation_name = models.CharField(max_length=200, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    price_per_night = models.IntegerField()
    address = models.CharField(max_length=200)
    image_path = models.ImageField(upload_to='images')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    def __str__(self):
        return str([self.accomodation_name,  self.price_per_night, self.city])


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
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def save(self, *args, **kwargs):
        self.duration = datetime.combine(date.min, self.arrive_time) - datetime.combine(date.min, self.depart_time)
        super(Transportation, self).save(*args, **kwargs)

    def __str__(self):
        return str([self.name, self.city_from, self.city_to, self.price_per_person])


class RencanaWisata(models.Model):
    THEME_CHOICE = [
        ('Pantai', 'Pantai'),
        ('Gunung', 'Gunung'),
        ('Tempat Bersejarah', 'Tempat Bersejarah'),
        ('Taman Hiburan', 'Taman Hiburan'),
        ('Wisata Seni', 'Wisata Seni'),
        ('Perkotaan', 'Perkotaan'),
        ('Mixed', 'Mixed')
    ]
    title = models.CharField(max_length=200, null=True)
    theme = models.CharField(max_length=200, choices=THEME_CHOICE, null=True)
    budget = models.CharField(max_length=200)
    cover = models.ImageField(null=True)
    city_start = models.ForeignKey(City, on_delete=models.CASCADE)
    city_dest = models.ForeignKey(City, related_name='city_dest', on_delete=models.CASCADE)
    days = models.IntegerField()
    destination = models.ManyToManyField(Destination)
    akomodasi = models.ManyToManyField(Accomodation)
    transportasi_pergi = models.ManyToManyField(Transportation)
    transportasi_pulang = models.ManyToManyField(Transportation, related_name='transport_pulang')
    total_cost = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title
