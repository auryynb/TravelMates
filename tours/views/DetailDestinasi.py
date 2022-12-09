from django.views import generic

from tours.models import Destinasi


class DetailDestinasi(generic.DetailView):
    model = Destinasi
    template_name = 'tours/destination/detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DetailDestinasi, self).get_context_data(*args, **kwargs)
        return context
