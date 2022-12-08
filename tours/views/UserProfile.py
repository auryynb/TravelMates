from django.contrib import messages
from django.shortcuts import redirect, render
from django.views import View

from tours.forms import UserProfileForm
from tours.models import User


class UserProfile(View):
    form_class = UserProfileForm
    initial = {'key': 'value'}
    template_name = 'users/profile.html'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/login')
        p = User.objects.get(username=request.user.username)

        form = UserProfileForm(instance=p)
        return render(request, self.template_name, {'form': form, 'test': len(kwargs)})

    def post(self, request, *args, **kwargs):
        p = User.objects.get(username=request.user.username)
        form = self.form_class(request.POST, request.FILES, instance=p)
        if form.is_valid():
            form.save()
            messages.success(request, f'User was successfully updated')
            return redirect('/profile/' + request.user.username + '/')
        return render(request, self.template_name, {'form': form})
