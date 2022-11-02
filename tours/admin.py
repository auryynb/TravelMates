from django.contrib import admin
from .models import City, Destination


# Register your models here.


class DestinationInline(admin.StackedInline):
    model = Destination
    extra = 3


class CityAdmin(admin.ModelAdmin):
    inlines = [DestinationInline]


admin.site.register(City, CityAdmin)
