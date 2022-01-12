""" User models admin """

# Django
from django.contrib import admin

# Models
from bk_service.locations.models import Country, State, City


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    """ country model admin """
    list_display = ('name', 'code', 'is_active',)
    search_fields = ('name', 'code',)
    list_filter = ('is_active', 'name', 'code',)


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    """ state model admin """
    list_display = ('name', 'is_active',)
    search_fields = ('name',)
    list_filter = ('is_active', 'name',)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    """ city  model admin """
    list_display = ('name', 'id', 'is_active',)
    search_fields = ('name', )
    list_filter = ('is_active', 'name', )
