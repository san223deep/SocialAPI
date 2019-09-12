from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'user_id', 'balance', 'device_id', 'platform')

admin.site.register(User, UserAdmin)

