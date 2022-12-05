from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import City, Destination, Transportation, Accomodation, RencanaWisata, ImageAlbum, Image, Post, User
from tinymce.widgets import TinyMCE
from django.db import models
# Register your models here.


class CustomUserAdmin(UserAdmin):
    model = User


class DestinationInline(admin.StackedInline):
    model = Destination
    extra = 3


class CityAdmin(admin.ModelAdmin):
    inlines = [DestinationInline]


class ImageAlbumAdmin(admin.ModelAdmin):
    model = ImageAlbum


class ImageAdmin(admin.ModelAdmin):
    model = Image


class TransportationAdmin(admin.ModelAdmin):
    model = Transportation
    extra = 1


class AccomodationAdmin(admin.ModelAdmin):
    model = Accomodation


class RencanaWisataAdmin(admin.ModelAdmin):
    model = RencanaWisata
    filter_horizontal = ['destination']
    extra = 1


class PostAdmin(admin.ModelAdmin):
    model = Post


admin.site.register(City, CityAdmin)
admin.site.register(Transportation, TransportationAdmin)
admin.site.register(Accomodation, AccomodationAdmin)
admin.site.register(RencanaWisata, RencanaWisataAdmin)
admin.site.register(ImageAlbum, ImageAlbumAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(User, CustomUserAdmin)
