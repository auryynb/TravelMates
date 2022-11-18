from django.contrib import admin
from .models import City, Destination, Transportation, Accomodation, RencanaWisata


# Register your models here.


class DestinationInline(admin.StackedInline):
    model = Destination
    extra = 3


class CityAdmin(admin.ModelAdmin):
    inlines = [DestinationInline]


class TransportationAdmin(admin.ModelAdmin):
    model = Transportation
    extra = 1


class AccomodationAdmin(admin.ModelAdmin):
    model = Accomodation


class RencanaWisataAdmin(admin.ModelAdmin):
    model = RencanaWisata
    extra = 1


admin.site.register(City, CityAdmin)
admin.site.register(Transportation, TransportationAdmin)
admin.site.register(Accomodation, AccomodationAdmin)
admin.site.register(RencanaWisata, RencanaWisataAdmin)


