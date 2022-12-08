from django.views import generic

from tours.models import User, Postingan


class IndexPostView(generic.ListView):
    template_name = "tours/explore/IndexPostUI.html"

    def get_context_data(self, *args, **kwargs):
        context = super(IndexPostView, self).get_context_data(*args, **kwargs)
        context['user_list'] = User.objects.all()[:6]
        return context

    def get_queryset(self):
        return Postingan.objects.all().order_by('-created_at')