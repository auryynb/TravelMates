from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import Http404
from django.shortcuts import redirect


def LoginView(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        messages.success(request, f'Selamat datang. ' + username)
        login(request, user)
        return redirect('/posts/')
    else:
        raise Http404