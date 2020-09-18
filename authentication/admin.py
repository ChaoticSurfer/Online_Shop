from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as _UserAdmin
from .models import User\
    # , Order


class UserAdmin(_UserAdmin):
    list_display = ('email', 'date_joined', 'last_login', 'is_staff', 'phone_number', 'first_name', 'last_name')
    search_fields = ('email', 'last_login', 'date_joined', 'phone_number')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ('phone_number', 'first_name', 'last_name', 'email', 'last_login')
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone_number')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone_number')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser')}),
    )


admin.site.register(User, UserAdmin)
# admin.site.register(Order)