from django.contrib import messages
from django.http import Http404
from django.shortcuts import redirect
from django.views import View

from tours.models import Postingan


class PostDeleteController(View):
    initial = {'key': 'value'}
    template_name = 'PostsUI.html'

    def post(self, request, *args, **kwargs):
        p = Postingan.objects.get(id=kwargs['id'])
        if str(kwargs['username']) != str(p.user):
            raise Http404
        r = Postingan.objects.filter(id=kwargs['id'])
        r.delete()
        messages.success(request, f'Post was successfully deleted')
        return redirect('/posts/' + kwargs['username'] + '/')