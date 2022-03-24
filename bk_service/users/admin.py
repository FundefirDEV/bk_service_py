""" User models admin """

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Models
from bk_service.users.models import User
from django.contrib.auth.forms import (
    AdminPasswordChangeForm, UserChangeForm, UserCreationForm,
)

# UserAdmin.list_display += ('email',)  # don't forget the commas


class CustomUserAdmin(UserAdmin):
    """ User model admin """

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name',
                       'phone_region_code', 'phone_number', 'is_staff', 'is_active')}
         ),
    )

    list_display = ('email', 'username', 'first_name', 'last_name',
                    'phone_region_code', 'phone_number', 'is_staff', 'is_verified', 'city',)
    list_filter = ('is_staff', 'created_at', 'updated_at', 'gender',)


admin.site.register(User, CustomUserAdmin)
