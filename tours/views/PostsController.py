from django.shortcuts import redirect, render
from django.views import View

from tours.models import Postingan


class PostsController(View):
    initial = {'key': 'value'}
    template_name = 'tours/explore/PostsUI.html'

    def get(self, request, *args, **kwargs):
        if kwargs['username'] != request.user.username:
            return redirect('/login')
        else:
            data = Postingan.objects.filter(user=request.user.id)
            return render(request, self.template_name, {'data': data})