from datetime import *
from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView
from django.views.generic.detail import SingleObjectMixin
from django.contrib.gis.geoip2 import GeoIP2
from .models import City, Destination, Image, ImageAlbum, RencanaWisata
from django.db.models import Q, Case, When, Value, BooleanField
from django import forms
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'tours/index.html'
    context_object_name = 'tour_list'

    def get_ip(self):
        user_ip = self.request.META.get('HTTP_X_FORWARDED_FOR')  # real ip user
        if user_ip:
            ip = user_ip.split(',')[0]
        else:
            ip = self.request.META.get('REMOTE_ADDR')  # ip komputer client
        g = GeoIP2()  # manggil library
        # city = g.city(ip) #cari kota based on ip
        city = g.city('103.165.157.4')
        return city

    def get_city_list(self):
        return City.objects.values('city', 'province')

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        user_city = self.get_ip()
        if self.request.GET.get("city") is not None:
            user_city['city'] = self.request.GET.get("city")
        context['city'] = City.objects.all()
        context['location'] = user_city
        context['city_list'] = self.get_city_list()
        return context

    def divide_chunks(self, obj):
        n = 4
        # looping till length l
        for i in range(0, len(obj), n):
            yield obj[i:i + n]

    def get_queryset(self):
        user_city = self.get_ip()
        if self.request.GET.get("city") is not None:
            user_city['city'] = self.request.GET.get("city")
        g = Destination.objects.filter(
            Q(city__city=user_city['city']) | Q(city__related_city=user_city['city'])).annotate(
            relevancy=Case(When(city=user_city['city'], then=Value(True)), output_field=BooleanField())).order_by(
            'relevancy')
        if not g:
            g = Destination.objects.all()
        return list(self.divide_chunks(g))


class DetailView(generic.DetailView):
    model = Destination
    template_name = 'tours/detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DetailView, self).get_context_data(*args, **kwargs)
        context['image'] = Image.objects.filter(
            album_id=(Destination.objects.values_list('album_id').get(id=self.kwargs['pk'])))
        return context


class IndexPlanView(generic.ListView):
    template_name = 'tours/plan_list.html'
    context_object_name = 'plan_list'

    def get_context_data(self, *args, **kwargs):
        user_city = IndexView.get_ip(self)
        if self.request.GET.get("city") is not None:
            user_city['city'] = self.request.GET.get("city")
        context = super(IndexPlanView, self).get_context_data(*args, **kwargs)
        context['location'] = user_city
        context['city'] = City.objects.all()
        return context

    def get_queryset(self):
        return RencanaWisata.objects.all()


class DetailPlanView(generic.DetailView):
    model = RencanaWisata
    template_name = 'tours/plan_detail.html'

    def getRencana(self, **kwargs):
        rencana = RencanaWisata.objects.filter(pk=self.kwargs.get('pk')).first()
        return rencana

    def rencanaDestinasi(self):
        rencana = self.getRencana()
        current_time = datetime.strptime(rencana.transportasi_pergi.get().arrive_time.strftime("%H:%M:%S"), '%H:%M:%S')
        # using dict
        destinasi = list(rencana.destination.all())
        destination_plan = {'day': [], 'start_time': [], 'end_time': [], 'destination': []}
        start_time = current_time
        end_time = start_time + timedelta(hours=4)
        days = 1
        while days <= rencana.days:
            while start_time.hour <= 19:
                end_time = start_time + timedelta(hours=4)
                res = list(filter(lambda x: x.opening_hours < start_time.time() and x.closing_hours > end_time.time(),
                                  destinasi))
                if res:
                    des = res[0]
                    destination_plan['destination'].append(des)
                    destinasi.remove(des)
                    destination_plan['day'].append(days)
                    destination_plan['start_time'].append(start_time)
                    destination_plan['end_time'].append(end_time)
                    start_time = end_time
                else:
                    break
            days += 1
            start_time = datetime(1990, 1, 1, 8, 0)
        return destination_plan

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rencana'] = RencanaWisata.objects.filter(pk=self.kwargs.get('pk')).first()
        context['plan'] = self.rencanaDestinasi()
        context['destinasi'] = self.rencanaDestinasi()['destination']
        return context


class IndexDestinationView(generic.ListView):
    template_name = 'tours/destination_list.html'
    context_object_name = 'destination_list'

    def get_context_data(self, *args, **kwargs):
        user_city = IndexView.get_ip(self)
        if self.request.GET.get("city") is not None:
            user_city['city'] = self.request.GET.get("city")
        context = super(IndexDestinationView, self).get_context_data(*args, **kwargs)
        context['location'] = user_city
        context['city'] = City.objects.all()
        return context

    def cari_destinasi(self):
        keyword = self.request.GET.get("cari_destinasi")
        if keyword:
            return Destination.objects.filter(name__istartswith=keyword)
        else:
            return

    def get_queryset(self):
        filterDest = self.cari_destinasi()
        if filterDest:
            return filterDest
        else:
            return Destination.objects.all()


class BuatRencanaWisata(CreateView):
    model = RencanaWisata
