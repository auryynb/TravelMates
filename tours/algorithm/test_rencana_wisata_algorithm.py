from django.test import TestCase
import datetime
from tours.algorithm.rencana_wisata_algorithm import *


class Test(TestCase):
    def setUp(self):
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
        Destinasi.objects.create(id=4, name="Jawa Timur Park 2", categories="Taman Bermain",
                                 image_path="/image/borobudur.jpg",
                                 address="Magelang, Jawa Tengah", maps='xxx', panorama='xxx', kecamatan='xxx',
                                 city=k2, description='xxx', opening_hours='09:00:00',
                                 closing_hours='21:00:00',
                                 price_min=60000, price_max=100000, rating=4.0)
        Destinasi.objects.create(id=5, name="Jawa Timur Park 3", categories="Taman Bermain",
                                 image_path="/image/borobudur.jpg",
                                 address="Magelang, Jawa Tengah", maps='xxx', panorama='xxx', kecamatan='xxx',
                                 city=k2, description='xxx', opening_hours='09:00:00',
                                 closing_hours='21:00:00',
                                 price_min=60000, price_max=100000, rating=4.0)
        Transportasi.objects.create(id=1, name='KA Malioboro', city_from=k1, city_to=k2, depart_time=time(23, 0), arrive_time=time(7, 0), price_per_person=90000)
        Transportasi.objects.create(id=2, name='KA Kertanegara', city_from=k2, city_to=k1, depart_time=time(21, 0), arrive_time=time(4, 0), price_per_person=90000)

    def test_split_budget(self):
        x, y = splitBudget(7)
        self.assertAlmostEqual(x, 0.63)
        self.assertAlmostEqual(y, 0.09)

    def test_closest_sum(self):
        res = closestSum([100, 200, 300], 300)
        self.assertLess(sum(res), 300)

    def test_closest_sum_2(self):
        res = closestSum([], 410)
        self.assertLess(sum(res), 410)

    def test_closest_sum_3(self):
        res = closestSum([300], 0)
        self.assertLess(sum(res), 410)

    def test_destination_budget_mapping(self):
        res = destinationBudgetMapping(0, 'Malang')
        self.assertFalse(res)

    def test_destination_budget_mapping_2(self):
        res = destinationBudgetMapping(510000, 'Malang')
        self.assertGreater(len(res), 2)

    def test_destination_budget_mapping_3(self):
        res = destinationBudgetMapping(510000, 'Surabaya')
        self.assertFalse(res)

    def test_rencana_transportasi(self):
        r = rencanaWisata(1000000, 2, 'Malang', 'Yogyakarta')
        res = rencanaTransportasi(r, 100000, 'Malang', 'Yogyakarta')
        # exp result false, tidak ada transportasi yg memenuhi
        self.assertFalse(res)

    def test_rencana_transportasi_2(self):
        r = rencanaWisata(1000000, 2, 'Malang', 'Yogyakarta')
        res = rencanaTransportasi(r, 300000, 'Malang', 'Yogyakarta')
        self.assertEqual(res[0], datetime(1900, 1, 1, 4, 0)) #jam tiba
        self.assertEqual(res[1], datetime(1900, 1, 1, 23, 0)) #jam pulang
        self.assertLessEqual(res[2], 300000)
        self.assertIsNotNone(r.transportasi_pergi)

    def test_rencana_transportasi_3(self):
        r = rencanaWisata(1000000, 2, 'Malang', 'Yogyakarta')
        res = rencanaTransportasi(r, 100000, 'New York', 'Yogyakarta')
        self.assertFalse(res)

    def test_rencana_transportasi_4(self):
        r = rencanaWisata(1000000, 2, 'Malang', 'Yogyakarta')
        res = rencanaTransportasi(r, 100000, 'Malang', 'Tokyo')
        self.assertFalse(res)

    def test_rencana_transportasi_5(self):
        r = rencanaWisata(1000000, 2, 'Malang', 'Yogyakarta')
        res = rencanaTransportasi(r, 100000, 'Malang', 'Tokyo')
        self.assertFalse(res)

    def test_rencana_destinasi(self):
        r = rencanaWisata(1000000, 2, 'Malang', 'Yogyakarta')
        destinasi = list(Destinasi.objects.filter(city=r.city_dest).all())
        # rencanaDestinasi(r, destinasi, r.days, datetime.strptime(r.transportasi_pergi.arrive_time.strftime("%H:%M:%S"), '%H:%M:%S'), datetime.strptime(r.transportasi_pulang.depart_time.strftime("%H:%M:%S"), '%H:%M:%S'))
        result = r.destination.all()
        self.assertGreater(len(result), 1)
        self.fail()

    # def test_rencana_destinasi(self):
    #     self.fail()
    #
    # def test_rencana_destinasi(self):
    #     self.fail()

    # def test_rencana_destinasi(self):
    #     self.fail()
    #
    # # def test_rencana_akomodasi(self):
    #     self.fail()
    #
    # def test_rencana_wisata(self):
    #     self.fail()
