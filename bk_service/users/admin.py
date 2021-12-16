""" User models admin """

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Models
from bk_service.users.models import User


class CustomUserAdmin(UserAdmin):
    """ User model admin """

    list_display = ('email', 'username', 'first_name', 'last_name',
                    'phone_number', 'is_staff', 'is_verified',)
    list_filter = ('is_staff', 'created_at', 'updated_at', 'gender')


admin.site.register(User, CustomUserAdmin)
