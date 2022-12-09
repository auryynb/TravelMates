from django.db.models import *
from django.views import generic

from tours.models import Kota, Destinasi
from tours.views.IndexController import IndexView


class IndexDestinasiController(generic.ListView):
    template_name = 'tours/destination/destination_list.html'
    context_object_name = 'destination_list'
    paginate_by = 20
    def get_context_data(self, *args, **kwargs):
        context = super(IndexDestinasiController, self).get_context_data(*args, **kwargs)
        user_city = IndexView.get_ip(self)
        if self.request.GET.get("location") is not None:
            user_city['city'] = self.request.GET.get("location")
        if self.request.GET.get("cari_destinasi"):
            filtered = self.search_by_name()
            context['searched'] = filtered
        context['location'] = user_city
        context['city'] = Kota.objects.all()

        return context

    def search_by_name(self):
        keyword = self.request.GET.get("cari_destinasi")
        city = self.request.GET.get("location")
        if city in ['Semua', '']:
            q = Destinasi.objects.filter(name__icontains=keyword)
        elif keyword:
            q = Destinasi.objects.filter(name__icontains=keyword, city__city=city)
        if q:
            return q
        else:
            return 'Tidak ditemukan'

    def search(self, keyword):
        if keyword:
            q = Destinasi.objects.filter(name__icontains=keyword)
            if q:
                return q
            else:
                return 'Tidak ditemukan'
        else:
            return False



    def get_queryset(self):
        user_city = IndexView.get_ip(self)
        if self.request.GET.get("location") is not None or Empty:
            user_city['city'] = self.request.GET.get("location")
        g = Destinasi.objects.filter(
            Q(city__city=user_city['city']) | Q(city__related_city=user_city['city'])).annotate(
            relevancy=Case(When(city=user_city['city'], then=Value(True)), output_field=BooleanField())).order_by(
            'relevancy')
        if not g:
            g = Destinasi.objects.all()
        return g
