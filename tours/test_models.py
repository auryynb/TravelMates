from django.test import TestCase

from tours.models import Kota


class KotaModelTest(TestCase):
    def setUpTestData(cls):
        Destinasi.objects.create(name="Candi Borobudur", categories="Tempat Bersejarah", image_path="/image/borobudur.jpg",
                            address="Magelang, Jawa Tengah", maps='xxx', panorama='xxx', kecamatan='xxx',
                            city='Yogyakarta', description='xxx', opening_hours='09:00:00', closing_hours='21:00:00',
                            price_min=60000, price_max=100000, rating=4.0)

        pass
