from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Kota, Destinasi, Transportasi, Akomodasi, RencanaWisata, ImageAlbum, Image, Postingan, User
from tinymce.widgets import TinyMCE
from django.db import models
# Register your models here.


class CustomUserAdmin(UserAdmin):
    model = User


class DestinationInline(admin.StackedInline):
    model = Destinasi
    extra = 3


class CityAdmin(admin.ModelAdmin):
    inlines = [DestinationInline]


class ImageAlbumAdmin(admin.ModelAdmin):
    model = ImageAlbum


class ImageAdmin(admin.ModelAdmin):
    model = Image


class TransportationAdmin(admin.ModelAdmin):
    model = Transportasi
    extra = 1


class AccomodationAdmin(admin.ModelAdmin):
    model = Akomodasi


class RencanaWisataAdmin(admin.ModelAdmin):
    model = RencanaWisata
    filter_horizontal = ['destination']
    extra = 1


class PostAdmin(admin.ModelAdmin):
    model = Postingan


admin.site.register(Kota, CityAdmin)
admin.site.register(Transportasi, TransportationAdmin)
admin.site.register(Akomodasi, AccomodationAdmin)
admin.site.register(RencanaWisata, RencanaWisataAdmin)
admin.site.register(ImageAlbum, ImageAlbumAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Postingan, PostAdmin)
admin.site.register(User, CustomUserAdmin)
