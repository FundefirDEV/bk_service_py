""" User models admin """

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Models
from bk_service.users.models import User, Country


class CustomUserAdmin(UserAdmin):
    """ User model admin """

    list_display = ('email', 'username', 'first_name', 'last_name',
                    'phone_number', 'is_staff', 'is_verified',)
    list_filter = ('is_staff', 'created_at', 'updated_at', 'gender')


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    """ country model admin """
    list_display = ('name', 'code', 'is_active',)
    search_fields = ('name', 'code',)
    list_filter = ('is_active', 'name', 'code',)


admin.site.register(User, CustomUserAdmin)
