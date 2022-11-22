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
        user_ip = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if user_ip:
            ip = user_ip.split(',')[0]
        else:
            ip = self.request.META.get('REMOTE_ADDR')
        g = GeoIP2()
        # city = g.city(ip)
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


# g = Destination.objects.filter(Q(city__city='Malang') | Q(city__related_city='Malang')).annotate(relevancy=Case(When(city__city='Malang', then=Value(True)),output_field=BooleanField())).order_by('-relevancy')
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
    template_name = 'tours/detail.html'


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

    def get_queryset(self):
        return Destination.objects.all()


class BuatRencanaWisata(CreateView):
    model = RencanaWisata


