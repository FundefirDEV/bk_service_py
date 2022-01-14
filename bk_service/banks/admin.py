""" Bank models admin """

# Django
from django.contrib import admin

# Models
from bk_service.banks.models import *


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    """ Partner model admin """
    # list_display = '__all__'
    # search_fields = ('name', 'code',)
    # list_filter = ('is_active', 'name', 'code',)


@admin.register(PartnerDetail)
class PartnerDetailAdmin(admin.ModelAdmin):
    """ PartnerDetail model admin """
    # list_display = '__all__'
    # search_fields = ('name', 'code',)
    # list_filter = ('is_active', 'name', 'code',)


@admin.register(PartnerGuest)
class PartnerAdmin(admin.ModelAdmin):
    """ Partner guest model admin """
    # list_display = '__all__'
    # search_fields = ('name', 'code',)
    # list_filter = ('is_active', 'name', 'code',)


@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    """ Bank model admin """
    # list_display = '__all__'
    # search_fields = ('name', 'code',)
    # list_filter = ('is_active', 'name', 'code',)


@admin.register(BankRules)
class BankRulesAdmin(admin.ModelAdmin):
    """ BankRules model admin """
    # list_display = '__all__'
    # search_fields = ('name', 'code',)
    # list_filter = ('is_active', 'name', 'code',)
