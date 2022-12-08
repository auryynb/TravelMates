# from datetime import *
#
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.decorators import login_required
# from django.shortcuts import render, redirect
# from django.views import generic
# from django.views.generic.edit import CreateView
# from django.views.generic.detail import SingleObjectMixin
# from django.contrib.gis.geoip2 import GeoIP2
# from .forms import CreatePostForm, CreateUserForm, UserProfileForm
# from .models import Kota, Destinasi, Image, ImageAlbum, RencanaWisata, Postingan, User, RencanaWisata, \
#     RencanaWisataDestinasi
# from django.db.models import Q, Case, When, Value, BooleanField
# from django import forms
# from django.http import HttpResponse, Http404, HttpRequest
# import logging
# from django.views import View
# from django.contrib import messages
# from .rencanaWisata import rencanaWisata
#
# logger = logging.getLogger(__name__)
#
#
# # Create your views here.
# class IndexView(generic.ListView):
#     template_name = 'tours/index.html'
#     context_object_name = 'tour_list'
#
#     def get_ip(self):
#         user_ip = self.request.META.get('HTTP_X_FORWARDED_FOR')  # real ip user
#         if user_ip:
#             ip = user_ip.split(',')[0]
#         else:
#             ip = self.request.META.get('REMOTE_ADDR')  # ip komputer client
#         g = GeoIP2()  # manggil library
#         # city = g.city(ip) #cari kota based on ip
#         city = g.city('103.165.157.4')
#         return city
#
#     def get_city_list(self):
#         return Kota.objects.values('city', 'province')
#
#     def get_context_data(self, *args, **kwargs):
#         context = super(IndexView, self).get_context_data(*args, **kwargs)
#         user_city = self.get_ip()
#         if self.request.GET.get("city") is not None:
#             user_city['city'] = self.request.GET.get("city")
#         context['city'] = Kota.objects.all()
#         context['location'] = user_city
#         context['city_list'] = self.get_city_list()
#         context['post'] = Postingan.objects.all().order_by('-created_at')[:4]
#         return context
#
#     def divide_chunks(self, obj):
#         n = 4
#         # looping till length l
#         for i in range(0, len(obj), n):
#             yield obj[i:i + n]
#
#     def get_queryset(self):
#         user_city = self.get_ip()
#         if self.request.GET.get("city") is not None:
#             user_city['city'] = self.request.GET.get("city")
#         g = Destinasi.objects.filter(
#             Q(city__city=user_city['city']) | Q(city__related_city=user_city['city'])).annotate(
#             relevancy=Case(When(city=user_city['city'], then=Value(True)), output_field=BooleanField())).order_by(
#             'relevancy')[:12]
#         if not g:
#             g = Destinasi.objects.all()[:12]
#         return list(self.divide_chunks(g))
#
#
# class DetailView(generic.DetailView):
#     model = Destinasi
#     template_name = 'tours/destination/detail.html'
#
#     def get_context_data(self, *args, **kwargs):
#         context = super(DetailView, self).get_context_data(*args, **kwargs)
#         context['image'] = Image.objects.filter(
#             album_id=(Destinasi.objects.values_list('album_id').get(id=self.kwargs['pk'])))
#         return context
#
#
# class IndexPlanView(generic.ListView):
#     template_name = 'tours/tour_plan/plan_list.html'
#     context_object_name = 'plan_list'
#
#     def get_context_data(self, *args, **kwargs):
#         user_city = IndexView.get_ip(self)
#         if self.request.GET.get("city") is not None:
#             user_city['city'] = self.request.GET.get("city")
#         context = super(IndexPlanView, self).get_context_data(*args, **kwargs)
#         context['location'] = user_city
#         context['city'] = Kota.objects.all()
#         if self.request.user.is_authenticated :
#             context['user_plan'] = RencanaWisata.objects.filter(user=self.request.user)
#         return context
#
#     def get_queryset(self):
#         return RencanaWisata.objects.all()
#
#
# # class DetailPlanView(generic.DetailView):
# #     model = RencanaWisata
# #     template_name = 'tours/tour_plan/plan_detail.html'
# #
# #     def getRencana(self, **kwargs):
# #         rencana = RencanaWisata.objects.filter(pk=self.kwargs.get('pk')).first()
# #         return rencana
# #
# #     def rencanaDestinasi(self):
# #         rencana = self.getRencana()
# #         current_time = datetime.strptime(rencana.transportasi_pergi.get().arrive_time.strftime("%H:%M:%S"), '%H:%M:%S')
# #         # using dict
# #         destinasi = list(rencana.destination.all())
# #         start_time = current_time
# #         end_time = start_time + timedelta(hours=4)
# #         days = 1
# #         r = RencanaWisataUser(title='test', budget='650000', city_start_id='Malang', city_dest_id='Yogyakarta')
# #         r.save()
# #         while days <= rencana.days:
# #             while start_time.hour <= 19:
# #                 end_time = start_time + timedelta(hours=4)
# #                 res = list(filter(lambda x: x.opening_hours < start_time.time() and x.closing_hours > end_time.time(),
# #                                   destinasi))
# #                 if res:
# #                     des = res[0]
# #                     # destination_plan['destination'].append(des)
# #                     d= RencanaWisataUser
# #                     destinasi.remove(des)
# #                     # destination_plan['day'].append(days)
# #                     # destination_plan['start_time'].append(start_time)
# #                     # destination_plan['end_time'].append(end_time)
# #                     start_time = end_time
# #                 else:
# #                     break
# #             days += 1
# #             start_time = datetime(1990, 1, 1, 8, 0)
# #
# #     def get_context_data(self, **kwargs):
# #         context = super().get_context_data(**kwargs)
# #         context['rencana'] = RencanaWisata.objects.filter(pk=self.kwargs.get('pk')).first()
# #         context['plan'] = self.rencanaDestinasi()
# #         context['destinasi'] = self.rencanaDestinasi()['destination']
# #         return context
#
#
# class RencanaWisataController(View) :
#     template_name = 'tours/tour_plan/plan_detail.html'
#
#     def get(self, request, *args, **kwargs):
#         budget = int(self.request.GET.get("budget"))
#         days = int(self.request.GET.get("days"))
#         city_to = self.request.GET.get("city_to")
#         city_from = self.request.GET.get("city_from")
#         # rencana = RencanaWisataUser.objects.filter(id=169).first()
#         rencana = rencanaWisata(budget, days, city_from, city_to)
#         destinasi = RencanaWisataDestinasi.objects.filter(rencana_wisata_id=rencana.id).all()
#         return render(request, self.template_name, {'rencana' : rencana, 'destinasi' : destinasi})
#
#     def post(self, request, *args, **kwargs):
#         rencana_id = request.POST.get("rencana_id", "")
#         rencana_title = request.POST.get("rencana_title", "")
#         rencana = RencanaWisata.objects.filter(id=rencana_id).first()
#         rencana.user = self.request.user
#         rencana.title = rencana_title
#         rencana.save()
#         return redirect('plan_list')
#
#
#     #
#     # def splitBudget(days):
#     #     per = 0.15
#     #     res = 0
#     #     for i in range(days):
#     #         res += per
#     #         per -= 0.02
#     #     each = res / days
#     #     return res, each
#     #
#     #
#     # def closestSum(arr, k):
#     #     # create a dp dictionary to grow. key is closest sum so far, value is the list of numbers that add up to key
#     #     dp_dict = {0: []}
#     #     for num in arr:
#     #         dict_copy = dict(dp_dict)
#     #         # grow or update the dp dict with the closest sum so far
#     #         for sum in dp_dict:
#     #             if sum + num < k:
#     #                 dict_copy[sum + num] = dp_dict[sum] + [num]
#     #         dp_dict = dict_copy
#     #     # traceback - find the item in dp dict that is closest to k
#     #     result = (k, [])
#     #     for sum, number_list in dp_dict.items():
#     #         distance = abs(k - sum)
#     #         if distance < result[0]:
#     #             result = (distance, number_list)
#     #     return result[1]
#     #
#     #
#     # def destinationBudgetMapping(budget_destinasi):
#     #     destination = Destination.objects.filter(city='Yogyakarta')
#     #     sample_list = list(destination.values_list('price_max', flat=True))
#     #     target_value = budget_destinasi
#     #     sum_dest = closestSum(sample_list, target_value)
#     #     # print(sum_dest)
#     #     destination_list = list(destination)
#     #     destinasi = []
#     #     for price in sum_dest:
#     #         res = list(filter(lambda x: x.price_max == price, destination_list))
#     #         destinasi.append(res[0])
#     #         destination_list.remove(res[0])
#     #     if len(destinasi) > 2:
#     #         print(len(destinasi))
#     #         return destinasi
#     #     else:
#     #         print(len(destinasi))
#     #         print('Destinasi tidak memenuhi')
#     #         return False
#     #
#     #
#     # def rencanaTransportasi(r, budget_transportasi, city_from, city_to):
#     #     budget = 0.5 * budget_transportasi
#     #     transportasi_pergi = Transportation.objects.order_by('-price_per_person').filter(city_from=city_from, city_to=city_to, price_per_person__lte=budget).first()
#     #     transportasi_pulang = Transportation.objects.order_by('-price_per_person').filter(city_from=city_to, city_to=city_from, price_per_person__lte=budget).first()
#     #     if transportasi_pulang and transportasi_pergi:
#     #         cost = transportasi_pergi.price_per_person + transportasi_pulang.price_per_person
#     #         current_time = datetime.strptime(transportasi_pergi.arrive_time.strftime("%H:%M:%S"), '%H:%M:%S')
#     #         return_time = datetime.strptime(transportasi_pulang.depart_time.strftime("%H:%M:%S"), '%H:%M:%S')
#     #         r.transportasi_pergi = transportasi_pergi
#     #         r.transportasi_pulang = transportasi_pulang
#     #         print('sukses')
#     #         r.save()
#     #         return current_time, return_time, cost
#     #     else:
#     #         print(transportasi_pulang)
#     #         print('Transportasi tidak sesuai budget')
#     #         return False
#     #
#     #
#     # def rencanaDestinasi(r, destinasi, plan_days, current_time, return_time):
#     #     rencana = RencanaWisata.objects.filter(pk=1).first()
#     #     start_time = current_time
#     #     end_time = start_time + timedelta(hours=4)
#     #     days = 1
#     #     cost = 0
#     #     while days <= plan_days:
#     #         while start_time.hour <= 19:
#     #             end_time = start_time + timedelta(hours=4)
#     #             res = list(
#     #                 filter(lambda x: x.opening_hours < start_time.time() and x.closing_hours > end_time.time(), destinasi))
#     #             if res:
#     #                 des = res[0]
#     #                 d = RencanaDestinasiUser(destinasi=des, rencana_wisata=r, day=days, start_time=start_time, end_time=end_time)
#     #                 destinasi.remove(des)
#     #                 d.save()
#     #                 start_time = end_time
#     #                 cost += des.price_max
#     #                 if end_time.hour >= return_time.hour and days == rencana.days:
#     #                     print('waktunya pulang')
#     #                     break
#     #                 else:
#     #                     continue
#     #             else:
#     #                 break
#     #         days += 1
#     #         start_time = datetime(1900, 1, 1, 8, 0)
#     #         end_time = datetime(1900, 1, 1, 12, 0)
#     #     return cost
#     #
#     #
#     # def rencanaAkomodasi(r, budget):
#     #     akomodasi = Accomodation.objects.order_by('-price_per_night').filter(price_per_night__lte=budget).first()
#     #     cost = akomodasi.price_per_night
#     #     if (akomodasi):
#     #         print(akomodasi)
#     #         r.akomodasi = akomodasi
#     #         r.save()
#     #         print('sukses')
#     #         return True, cost
#     #     else:
#     #         print('akomodasi tidak cocok')
#     #         return False
#     #
#     #
#     # def rencanaWisata(budget, days, city_from, city_to):
#     #     split = splitBudget(days)
#     #     total_cost = 0
#     #     r = RencanaWisataUser(title='test', budget=budget, days=days, city_start_id=city_from, city_dest_id=city_to)
#     #     r.save()
#     #     tot_akomodasi = split[0] * budget
#     #     budget_akomodasi = split[1] * budget
#     #     if city_from == city_to:
#     #         budget_destinasi = budget - tot_akomodasi
#     #         akom = rencanaAkomodasi(r, budget_akomodasi)
#     #         destinasi = destinationBudgetMapping(budget_destinasi)
#     #         if akom is not False and destinasi is not False:
#     #             start_time = datetime(1900, 1, 1, 8, 0)
#     #             end_time = datetime(1900, 1, 1, 21, 0)
#     #             dest = rencanaDestinasi(r, destinasi, days, start_time, end_time)
#     #             print('Berhasil direncanakan')
#     #         else:
#     #             print('Wisata Gagal')
#     #             r.delete()
#     #         return r
#     #     else:
#     #         print('akomodasi', budget_akomodasi)
#     #         budget_transportasi = (0.6 * (1 - split[0])) * budget
#     #         budget_destinasi = (0.4 * (1 - split[0])) * budget
#     #         print('transport', budget_transportasi)
#     #         print('destinasi', budget_destinasi)
#     #         print(budget_destinasi + tot_akomodasi+budget_transportasi)
#     #         akom = rencanaAkomodasi(r, budget_akomodasi)
#     #         rt = rencanaTransportasi(r, budget_transportasi, city_from, city_to)
#     #         destinasi = destinationBudgetMapping(budget_destinasi)
#     #         if akom is not False and rt is not False :
#     #             dest = rencanaDestinasi(r, destinasi, days, rt[0], rt[1])
#     #             total_cost = akom[1] + dest + rt[2]
#     #             print('Rencana Sukses, total cost = ', total_cost)
#     #         else:
#     #             print('Rencana Gagal')
#     #             r.delete()
#     #         return r
#
#
#
# class IndexDestinationView(generic.ListView):
#     template_name = 'tours/destination/destination_list.html'
#     context_object_name = 'destination_list'
#
#     def get_context_data(self, *args, **kwargs):
#         user_city = IndexView.get_ip(self)
#         if self.request.GET.get("city") is not None:
#             user_city['city'] = self.request.GET.get("city")
#         context = super(IndexDestinationView, self).get_context_data(*args, **kwargs)
#         context['location'] = user_city
#         context['city'] = Kota.objects.all()
#         return context
#
#     def cari_destinasi(self):
#         keyword = self.request.GET.get("cari_destinasi")
#         if keyword:
#             return Destinasi.objects.filter(name__istartswith=keyword)
#         else:
#             return
#
#     def get_queryset(self):
#         filterDest = self.cari_destinasi()
#         if filterDest:
#             return filterDest
#         else:
#             return Destinasi.objects.all()
#
#
# # class BuatRencanaWisata(CreateView):
# #     model = RencanaWisata
#
#
# class RegisterController(View):
#     form_class = CreateUserForm
#     initial = {'key': 'value'}
#     template_name = 'users/register.html'
#
#     def get(self, request, *args, **kwargs):
#         if request.user.is_authenticated:
#             return redirect('index')
#         form = self.form_class(initial=self.initial)
#         return render(request, self.template_name, {'form': form})
#
#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Hi {username}, your account was successfully created')
#             return redirect('index')
#         return render(request, self.template_name, {'form': form})
#
#
# class CreatePostController(View):
#     form_class = CreatePostForm
#     initial = {'key': 'value'}
#     template_name = 'tours/explore/AddPostUI.html'
#
#     def get(self, request, *args, **kwargs):
#         if not request.user.is_authenticated:
#             return redirect('login')
#         form = self.form_class(initial=self.initial)
#         return render(request, self.template_name, {'form': form, 'test': len(kwargs)})
#
#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST, request.FILES)
#         if form.is_valid():
#             obj = form.save(commit=False)
#             obj.user = User.objects.get(pk=request.user.id)
#             obj.save()
#             messages.success(request, f'Post was successfully added')
#             return redirect('/posts/' + request.user.username + '/')
#         return render(request, self.template_name, {'form': form})
#
#
# class PostsController(View):
#     initial = {'key': 'value'}
#     template_name = 'tours/explore/PostsUI.html'
#
#     def get(self, request, *args, **kwargs):
#         if kwargs['username'] != request.user.username:
#             return redirect('/login')
#         else:
#             data = Postingan.objects.filter(user=request.user.id)
#             return render(request, self.template_name, {'data': data})
#
#
# class PostUpdateController(View):
#     form_class = CreatePostForm
#     initial = {'key': 'value'}
#     template_name = 'tours/explore/AddPostUI.html'
#
#     def get(self, request, *args, **kwargs):
#         p = Postingan.objects.get(id=kwargs['id'])
#         if kwargs['username'] != request.user.username:
#             raise Http404
#         form = CreatePostForm(instance=p)
#         return render(request, self.template_name, {'form': form, 'test': len(kwargs)})
#
#     def post(self, request, *args, **kwargs):
#         p = Postingan.objects.get(id=kwargs['id'])
#         form = self.form_class(request.POST, request.FILES, instance=p)
#         if form.is_valid():
#             form.save()
#             messages.success(request, f'Post was successfully updated')
#             return redirect('/posts/' + request.user.username + '/')
#         return render(request, self.template_name, {'form': form})
#
#
# class PostDeleteController(View):
#     initial = {'key': 'value'}
#     template_name = 'PostsUI.html'
#
#     def post(self, request, *args, **kwargs):
#         p = Postingan.objects.get(id=kwargs['id'])
#         if str(kwargs['username']) != str(p.user):
#             raise Http404
#         r = Postingan.objects.filter(id=kwargs['id'])
#         r.delete()
#         messages.success(request, f'Post was successfully deleted')
#         return redirect('/posts/' + kwargs['username'] + '/')
#
#
# def LoginView(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         messages.success(request, f'Selamat datang. ' + username)
#         login(request, user)
#         return redirect('/posts/')
#     else:
#         raise Http404
#
#
# class IndexPostView(generic.ListView):
#     template_name = "tours/explore/IndexPostUI.html"
#
#     def get_context_data(self, *args, **kwargs):
#         context = super(IndexPostView, self).get_context_data(*args, **kwargs)
#         context['user_list'] = User.objects.all()[:6]
#         return context
#
#     def get_queryset(self):
#         return Postingan.objects.all().order_by('-created_at')
#
#
# class UserProfile(View):
#     form_class = UserProfileForm
#     initial = {'key': 'value'}
#     template_name = 'users/profile.html'
#
#     def get(self, request, *args, **kwargs):
#         if not request.user.is_authenticated:
#             return redirect('/login')
#         p = User.objects.get(username=request.user.username)
#
#         form = UserProfileForm(instance=p)
#         return render(request, self.template_name, {'form': form, 'test': len(kwargs)})
#
#     def post(self, request, *args, **kwargs):
#         p = User.objects.get(username=request.user.username)
#         form = self.form_class(request.POST, request.FILES, instance=p)
#         if form.is_valid():
#             form.save()
#             messages.success(request, f'User was successfully updated')
#             return redirect('/profile/' + request.user.username + '/')
#         return render(request, self.template_name, {'form': form})
