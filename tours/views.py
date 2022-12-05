from datetime import *
from random import choice

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic.edit import CreateView
from django.views.generic.detail import SingleObjectMixin
from django.contrib.gis.geoip2 import GeoIP2

from .forms import CreatePostForm, CreateUserForm, UserProfileForm
from .models import City, Destination, Image, ImageAlbum, RencanaWisata, Post, User
from django.db.models import Q, Case, When, Value, BooleanField
from django import forms
from django.http import HttpResponse, Http404, HttpRequest
import logging
from django.views import View
from django.contrib import messages

logger = logging.getLogger(__name__)


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'tours/index.html'
    context_object_name = 'tour_list'

    def get_ip(self):
        user_ip = self.request.META.get('HTTP_X_FORWARDED_FOR')  # real ip user
        if user_ip:
            ip = user_ip.split(',')[0]
        else:
            ip = self.request.META.get('REMOTE_ADDR')  # ip komputer client
        g = GeoIP2()  # manggil library
        # city = g.city(ip) #cari kota based on ip
        city = g.city('103.165.157.4')
        return city

    def get_city_list(self):
        return City.objects.values('city', 'province')

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        user_city = self.get_ip()
        if self.request.GET.get("city") is not None:
            user_city['city'] = self.request.GET.get("city")
        context['city'] = City.objects.all()
        context['location'] = user_city
        context['city_list'] = self.get_city_list()
        context['post'] = Post.objects.all().order_by('-created_at')[:4]
        return context

    def divide_chunks(self, obj):
        n = 4
        # looping till length l
        for i in range(0, len(obj), n):
            yield obj[i:i + n]

    def get_queryset(self):
        user_city = self.get_ip()
        if self.request.GET.get("city") is not None:
            user_city['city'] = self.request.GET.get("city")
        g = Destination.objects.filter(
            Q(city__city=user_city['city']) | Q(city__related_city=user_city['city'])).annotate(
            relevancy=Case(When(city=user_city['city'], then=Value(True)), output_field=BooleanField())).order_by(
            'relevancy')[:12]
        if not g:
            g = Destination.objects.all()[:12]
        return list(self.divide_chunks(g))


class DetailView(generic.DetailView):
    model = Destination
    template_name = 'tours/destination/detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DetailView, self).get_context_data(*args, **kwargs)
        context['image'] = Image.objects.filter(
            album_id=(Destination.objects.values_list('album_id').get(id=self.kwargs['pk'])))
        return context


class IndexPlanView(generic.ListView):
    template_name = 'tours/tour_plan/plan_list.html'
    context_object_name = 'plan_list'

    def get_context_data(self, *args, **kwargs):
        user_city = IndexView.get_ip(self)
        if self.request.GET.get("city") is not None:
            user_city['city'] = self.request.GET.get("city")
        context = super(IndexPlanView, self).get_context_data(*args, **kwargs)
        context['location'] = user_city
        context['city'] = City.objects.all()
        return context

    def get_queryset(self):
        return RencanaWisata.objects.all()


class DetailPlanView(generic.DetailView):
    model = RencanaWisata
    template_name = 'tours/tour_plan/plan_detail.html'

    def getRencana(self, **kwargs):
        rencana = RencanaWisata.objects.filter(pk=self.kwargs.get('pk')).first()
        return rencana

    def rencanaDestinasi(self):
        rencana = self.getRencana()
        current_time = datetime.strptime(rencana.transportasi_pergi.get().arrive_time.strftime("%H:%M:%S"), '%H:%M:%S')
        # using dict
        destinasi = list(rencana.destination.all())
        destination_plan = {'day': [], 'start_time': [], 'end_time': [], 'destination': []}
        start_time = current_time
        end_time = start_time + timedelta(hours=4)
        days = 1
        while days <= rencana.days:
            while start_time.hour <= 19:
                end_time = start_time + timedelta(hours=4)
                res = list(filter(lambda x: x.opening_hours < start_time.time() and x.closing_hours > end_time.time(),
                                  destinasi))
                if res:
                    des = res[0]
                    destination_plan['destination'].append(des)
                    destinasi.remove(des)
                    destination_plan['day'].append(days)
                    destination_plan['start_time'].append(start_time)
                    destination_plan['end_time'].append(end_time)
                    start_time = end_time
                else:
                    break
            days += 1
            start_time = datetime(1990, 1, 1, 8, 0)
        return destination_plan

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rencana'] = RencanaWisata.objects.filter(pk=self.kwargs.get('pk')).first()
        context['plan'] = self.rencanaDestinasi()
        context['destinasi'] = self.rencanaDestinasi()['destination']
        return context


class IndexDestinationView(generic.ListView):
    template_name = 'tours/destination/destination_list.html'
    context_object_name = 'destination_list'

    def get_context_data(self, *args, **kwargs):
        user_city = IndexView.get_ip(self)
        if self.request.GET.get("city") is not None:
            user_city['city'] = self.request.GET.get("city")
        context = super(IndexDestinationView, self).get_context_data(*args, **kwargs)
        context['location'] = user_city
        context['city'] = City.objects.all()
        return context

    def cari_destinasi(self):
        keyword = self.request.GET.get("cari_destinasi")
        if keyword:
            return Destination.objects.filter(name__istartswith=keyword)
        else:
            return

    def get_queryset(self):
        filterDest = self.cari_destinasi()
        if filterDest:
            return filterDest
        else:
            return Destination.objects.all()


class BuatRencanaWisata(CreateView):
    model = RencanaWisata


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


class PostsController(View):
    initial = {'key': 'value'}
    template_name = 'tours/explore/PostsUI.html'

    def get(self, request, *args, **kwargs):
        if kwargs['username'] != request.user.username:
            return redirect('/login')
        else:
            data = Post.objects.filter(user=request.user.id)
            return render(request, self.template_name, {'data': data})


class PostUpdateController(View):
    form_class = CreatePostForm
    initial = {'key': 'value'}
    template_name = 'tours/explore/AddPostUI.html'

    def get(self, request, *args, **kwargs):
        p = Post.objects.get(id=kwargs['id'])
        if kwargs['username'] != request.user.username:
            raise Http404
        form = CreatePostForm(instance=p)
        return render(request, self.template_name, {'form': form, 'test': len(kwargs)})

    def post(self, request, *args, **kwargs):
        p = Post.objects.get(id=kwargs['id'])
        form = self.form_class(request.POST, request.FILES, instance=p)
        if form.is_valid():
            form.save()
            messages.success(request, f'Post was successfully updated')
            return redirect('/posts/' + request.user.username + '/')
        return render(request, self.template_name, {'form': form})


class PostDeleteController(View):
    initial = {'key': 'value'}
    template_name = 'PostsUI.html'

    def post(self, request, *args, **kwargs):
        p = Post.objects.get(id=kwargs['id'])
        if str(kwargs['username']) != str(p.user):
            raise Http404
        r = Post.objects.filter(id=kwargs['id'])
        r.delete()
        messages.success(request, f'Post was successfully deleted')
        return redirect('/posts/' + kwargs['username']+ '/')


def LoginView(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        messages.success(request, f'Selamat datang. '+ username)
        login(request, user)
        return redirect('/posts/')
    else:
        raise Http404


class IndexPostView(generic.ListView):
    template_name = "tours/explore/IndexPostUI.html"

    def get_context_data(self, *args, **kwargs):
        context = super(IndexPostView, self).get_context_data(*args, **kwargs)
        context['user_list'] = User.objects.all()[:6]
        return context

    def get_queryset(self):
        return Post.objects.all().order_by('-created_at')


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
