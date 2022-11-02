from django.shortcuts import render
from django.views import generic
from django.views.generic.detail import SingleObjectMixin
from django.contrib.gis.geoip2 import GeoIP2
from .models import City, Destination
from django.db.models import Q


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
        city = g.city('140.213.219.184')
        return city

    def get_city_list(self):
        return City.objects.values('city')

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        user_city = self.get_ip()
        context['city'] = City.objects.all()
        context['location'] = user_city
        context['city_list'] = self.get_city_list()
        return context

    def get_queryset(self):
        user_city = self.get_ip()
        return Destination.objects.filter(Q(city__related_city=user_city['city']) | Q(city__city=user_city['city']))


class DetailView(generic.DetailView):
    model = Destination
    template_name = 'tours/detail.html'
