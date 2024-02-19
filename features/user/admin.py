from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User
# Register your models here.


class UserAdmin(BaseUserAdmin):
    actions = ['reset-passwords']
    list_display = ('first_name', 'is_staff', 'is_superuser', 'is_active')
    readonly_fields = ('date_updated', 'date_joined')
    fieldsets = ((None, {'fields': ('username', 'password')}),
                 ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'photo_profile', 'phone_number')}),
                 ('Permissions', {'fields': ('is_client', 'is_active', 'is_staff', 'is_superuser')}),
                 ('Important Dates', {'fields': ('last_login', 'date_updated', 'date_joined')}),)
    add_fieldsets = (None, {'classes': ('wide',),
                            'fields': ('username', 'first_name', 'last_name', 'password1', 'password2', 'is_client',
                                       'is_staff', 'is_superuser')}),


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
