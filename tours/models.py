from datetime import datetime, date
from django.db import models
from django.contrib.auth.models import User, AbstractUser


# Create your models here.
class User(AbstractUser):
    profile_pic = models.ImageField(upload_to='images/user_profile', default='images/user_profile/default12998.png')
    tanggal_lahir = models.DateField(null=True)


class Kota(models.Model):
    city = models.CharField(max_length=50, primary_key=True)
    province = models.CharField(max_length=50, null=True)
    related_city = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to='images/city', null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.city


class Destinasi(models.Model):
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
    maps = models.CharField(max_length=1500, null=True)
    panorama = models.CharField(max_length=1500, null=True)
    kecamatan = models.CharField(max_length=200, null=True)
    city = models.ForeignKey(Kota, on_delete=models.CASCADE)
    description = models.CharField(max_length=22200, null=True)
    opening_hours = models.TimeField(null=True)
    closing_hours = models.TimeField(null=True)
    price_min = models.IntegerField()
    price_max = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    rating = models.FloatField(null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return str([self.name, self.city, self.price_max])


class Akomodasi(models.Model):
    accomodation_name = models.CharField(max_length=200, null=True)
    city = models.ForeignKey(Kota, on_delete=models.CASCADE)
    price_per_night = models.IntegerField()
    address = models.CharField(max_length=200)
    image_path = models.ImageField(upload_to='images')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str([self.accomodation_name, self.price_per_night, self.city])


class Transportasi(models.Model):
    MODA_CHOICES = [
        ('BUS', 'Bus'),
        ('TRAIN', 'Kereta Api'),
        ('PLANE', 'Pesawat'),
    ]
    name = models.CharField(max_length=200, null=True)
    moda = models.CharField(max_length=200, choices=MODA_CHOICES)
    city_from = models.ForeignKey(Kota, on_delete=models.CASCADE)
    city_to = models.ForeignKey(Kota, related_name='city_to', on_delete=models.CASCADE)
    depart_time = models.TimeField()
    arrive_time = models.TimeField()
    duration = models.DurationField(null=True, blank=True)
    price_per_person = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def save(self, *args, **kwargs):
        self.duration = datetime.combine(date.min, self.arrive_time) - datetime.combine(date.min, self.depart_time)
        super(Transportasi, self).save(*args, **kwargs)

    def __str__(self):
        return str([self.name, self.city_from, self.city_to, self.price_per_person])


class RencanaWisata(models.Model):
    title = models.CharField(max_length=200, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    budget = models.FloatField()
    city_start = models.ForeignKey(Kota, on_delete=models.CASCADE)
    city_dest = models.ForeignKey(Kota, related_name='user_city_dest', on_delete=models.CASCADE)
    days = models.IntegerField()
    transportasi_pergi = models.ForeignKey(Transportasi, on_delete=models.CASCADE, null=True)
    transportasi_pulang = models.ForeignKey(Transportasi, related_name='tp_pulang', on_delete=models.CASCADE,
                                            null=True)
    akomodasi = models.ForeignKey(Akomodasi, on_delete=models.CASCADE, null=True)
    destination = models.ManyToManyField(Destinasi, related_name='user_rencana_destinasi',
                                         through='RencanaWisataDestinasi')
    real_cost = models.FloatField(null=True)


class RencanaWisataDestinasi(models.Model):
    destinasi = models.ForeignKey(Destinasi, on_delete=models.CASCADE)
    rencana_wisata = models.ForeignKey(RencanaWisata, on_delete=models.CASCADE)
    day = models.IntegerField()
    start_time = models.TimeField()
    end_time = models.TimeField(null=True)


class Postingan(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, default='Judul')
    image_path = models.ImageField(upload_to='images/post')
    caption = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    destinasi = models.ForeignKey(Destinasi, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

