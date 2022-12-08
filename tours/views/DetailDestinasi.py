from django.views import generic

from tours.models import Destinasi, Image


class DetailDestinasi(generic.DetailView):
    model = Destinasi
    template_name = 'tours/destination/detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DetailDestinasi, self).get_context_data(*args, **kwargs)
        context['image'] = Image.objects.filter(
            album_id=(Destinasi.objects.values_list('album_id').get(id=self.kwargs['pk'])))
        return context