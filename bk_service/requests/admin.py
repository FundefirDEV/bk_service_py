""" Requests models admin """

# Django
from django.contrib import admin

# Models
from bk_service.requests.models import *


@admin.register(ShareRequest)
class ShareRequestAdmin(admin.ModelAdmin):
    """ ShareRequest model admin """
    # list_display = '__all__'
    # search_fields = ('name', 'code',)
    # list_filter = ('is_active', 'name', 'code',)


@admin.register(CreditRequest)
class CreditRequestAdmin(admin.ModelAdmin):
    """ CreditRequest model admin """
    # list_display = '__all__'
    # search_fields = ('name', 'code',)
    # list_filter = ('is_active', 'name', 'code',)
