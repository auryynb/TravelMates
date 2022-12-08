from django.views import generic

from tours.models import Kota, RencanaWisata
from tours.views.IndexController import IndexView


class IndexPlanView(generic.ListView):
    template_name = 'tours/tour_plan/plan_list.html'
    context_object_name = 'plan_list'

    def get_context_data(self, *args, **kwargs):
        user_city = IndexView.get_ip(self)
        if self.request.GET.get("city") is not None:
            user_city['city'] = self.request.GET.get("city")
        context = super(IndexPlanView, self).get_context_data(*args, **kwargs)
        context['location'] = user_city
        context['city'] = Kota.objects.all()
        if self.request.user.is_authenticated :
            context['user_plan'] = RencanaWisata.objects.filter(user=self.request.user)
        return context

    def get_queryset(self):
        return RencanaWisata.objects.all()