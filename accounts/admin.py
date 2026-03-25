from django.contrib import admin

from accounts.models import Profile
from django.apps import AppConfig

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone_number', 'birth_date', 'company_position']
    search_fields = ['user__username', 'phone_number', 'company_position']






