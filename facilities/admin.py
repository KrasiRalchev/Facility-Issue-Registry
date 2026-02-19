from django.contrib import admin

from facilities.models import Facility, Unit


@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'unit']
    list_filter = ['unit']
    search_fields = ['name', 'location']
    ordering = ['name']

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']



