from django.shortcuts import render, redirect
from django.views import View, generic

from tours.models import RencanaWisataDestinasi, RencanaWisata
from tours.algorithm.rencana_wisata_algorithm import rencanaWisata


class RencanaWisataController(View) :
    template_name = 'tours/tour_plan/plan_detail.html'

    def get(self, request, *args, **kwargs):
        budget = int(self.request.GET.get("budget"))
        days = int(self.request.GET.get("days"))
        city_to = self.request.GET.get("city_to")
        city_from = self.request.GET.get("city_from")
        rencana = rencanaWisata(budget, days, city_from, city_to)
        destinasi = RencanaWisataDestinasi.objects.filter(rencana_wisata_id=rencana.id).all()
        return render(request, self.template_name, {'rencana' : rencana, 'destinasi' : destinasi})

    def post(self, request, *args, **kwargs):
        rencana_id = request.POST.get("rencana_id", "")
        rencana_title = request.POST.get("rencana_title", "")
        rencana = RencanaWisata.objects.filter(id=rencana_id).first()
        rencana.user = self.request.user
        rencana.title = rencana_title
        rencana.save()
        return redirect('plan_list')


class RencanaDetail(generic.DetailView):
    model = RencanaWisata
    template_name = 'tours/tour_plan/plan_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(RencanaDetail, self).get_context_data(*args, **kwargs)
        rencana = RencanaWisata.objects.filter(id=self.kwargs['pk']).get()
        context['rencana'] = rencana
        context['destinasi'] = RencanaWisataDestinasi.objects.filter(rencana_wisata=rencana).all()
        return context


