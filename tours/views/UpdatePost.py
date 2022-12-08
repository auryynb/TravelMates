from django.contrib import messages
from django.http import Http404
from django.shortcuts import render, redirect
from django.views import View

from tours.forms import CreatePostForm
from tours.models import Postingan


class PostUpdateController(View):
    form_class = CreatePostForm
    initial = {'key': 'value'}
    template_name = 'tours/explore/AddPostUI.html'

    def get(self, request, *args, **kwargs):
        p = Postingan.objects.get(id=kwargs['id'])
        if p.user != request.user:
            raise Http404
        form = CreatePostForm(instance=p)
        return render(request, self.template_name, {'form': form, 'test': len(kwargs)})

    def post(self, request, *args, **kwargs):
        p = Postingan.objects.get(id=kwargs['id'])
        form = self.form_class(request.POST, request.FILES, instance=p)
        if form.is_valid():
            form.save()
            messages.success(request, f'Post was successfully updated')
            return redirect('/posts/' + request.user.username + '/')
        return render(request, self.template_name, {'form': form})