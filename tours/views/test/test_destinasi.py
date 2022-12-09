from django.test import TestCase

from tours.models import Destinasi, Kota
from tours.views import IndexView, IndexDestinasi, IndexDestinasiController
from django.test.client import RequestFactory, Client


class DestinasiTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        k1 = Kota.objects.create(city='Yogyakarta', province='DIY', image='xxx')
        k2 = Kota.objects.create(city='Malang', province='Jawa Timur', image='xxx')
        Destinasi.objects.create(id=1, name="Candi Borobudur", categories="Tempat Bersejarah",
                                 image_path="/image/borobudur.jpg",
                                 address="Magelang, Jawa Tengah", maps='xxx', panorama='xxx', kecamatan='xxx',
                                 city=k1, description='xxx', opening_hours='09:00:00',
                                 closing_hours='21:00:00',
                                 price_min=60000, price_max=100000, rating=4.0)
        Destinasi.objects.create(id=2, name="Candi Prambanan", categories="Tempat Bersejarah",
                                 image_path="/image/borobudur.jpg",
                                 address="Magelang, Jawa Tengah", maps='xxx', panorama='xxx', kecamatan='xxx',
                                 city=k1, description='xxx', opening_hours='09:00:00',
                                 closing_hours='21:00:00',
                                 price_min=50000, price_max=100000, rating=4.0)
        Destinasi.objects.create(id=3, name="Jawa Timur Park 1", categories="Taman Bermain",
                                 image_path="/image/borobudur.jpg",
                                 address="Magelang, Jawa Tengah", maps='xxx', panorama='xxx', kecamatan='xxx',
                                 city=k2, description='xxx', opening_hours='09:00:00',
                                 closing_hours='21:00:00',
                                 price_min=60000, price_max=100000, rating=4.0)
        self.factory = RequestFactory

    def test_destinasi_city(self):
        destinasi = Destinasi.objects.get(id=1)
        self.assertEqual(destinasi.city.city, 'Yogyakarta')

    def test_get_ip(self):
        result = IndexView.get_city_from_ip(self, '114.6.31.174')
        self.assertEqual(result['city'], 'Malang')

    def test_get_ip_2(self):
        result = IndexView.get_city_from_ip(self, '')
        self.assertFalse(result)

    def test_search_destinasi(self):
        result = IndexDestinasiController.search(self, 'Candi')
        filt = result[0].name
        self.assertIn('Candi', filt)

    def test_search_destinasi_2(self):
        result = IndexDestinasiController.search(self, '')
        self.assertFalse(result)

    def test_search_destinasi_3(self):
        result = IndexDestinasiController.search(self, 'Buaya')
        self.assertEqual('Tidak ditemukan', result)

    def test_search_destinasi_4(self):
        result = IndexDestinasiController.search(self, 'Park')
        filt = result[0].name
        self.assertIn('Park', filt)
