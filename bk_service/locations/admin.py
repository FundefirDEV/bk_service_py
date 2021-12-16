""" User models admin """

# Django
from django.contrib import admin

# Models
from bk_service.locations.models import Country


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    """ country model admin """
    list_display = ('name', 'code', 'is_active',)
    search_fields = ('name', 'code',)
    list_filter = ('is_active', 'name', 'code',)
