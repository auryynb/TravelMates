from django.contrib import messages
from django.shortcuts import redirect, render
from django.views import View

from tours.forms import CreateUserForm


class RegisterController(View):
    form_class = CreateUserForm
    initial = {'key': 'value'}
    template_name = 'users/register.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was successfully created')
            return redirect('index')
        return render(request, self.template_name, {'form': form})