from django.contrib import messages
from django.shortcuts import redirect, render
from django.views import View
from tours.forms import CreatePostForm
from tours.models import User


class CreatePostController(View):
    form_class = CreatePostForm
    initial = {'key': 'value'}
    template_name = 'tours/explore/AddPostUI.html'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form, 'test': len(kwargs)})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = User.objects.get(pk=request.user.id)
            obj.save()
            messages.success(request, f'Post was successfully added')
            return redirect('/posts/' + request.user.username + '/')
        return render(request, self.template_name, {'form': form})
