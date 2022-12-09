from django.contrib.gis.geoip2 import GeoIP2
from django.db.models import Q, Case, When, Value, BooleanField
from django.views import generic

from tours.models import Kota, Postingan, Destinasi


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
        if ip == '127.0.0.1':
            city = g.city('103.165.157.4')
        else:
            city = g.city(ip) #cari kota based on ip
        return city

    def get_city_from_ip(self, ip):
        g = GeoIP2()  # manggil library
        if ip == '' :
            return False
        if ip == '127.0.0.1':
            city = g.city('103.165.157.4')
        else:
            city = g.city(ip)  # cari kota based on ip
        return city

    def get_city_list(self):
        return Kota.objects.values('city', 'province')

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        user_city = self.get_ip()
        if self.request.GET.get("city") is not None:
            user_city['city'] = self.request.GET.get("city")
        context['city'] = Kota.objects.all()
        context['location'] = user_city
        context['city_list'] = self.get_city_list()
        context['post'] = Postingan.objects.all().order_by('-created_at')[:4]
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
        g = Destinasi.objects.filter(
            Q(city__city=user_city['city']) | Q(city__related_city=user_city['city'])).annotate(
            relevancy=Case(When(city=user_city['city'], then=Value(True)), output_field=BooleanField())).order_by(
            'relevancy')[:12]
        if not g:
            g = Destinasi.objects.all()[:12]
        return list(self.divide_chunks(g))
