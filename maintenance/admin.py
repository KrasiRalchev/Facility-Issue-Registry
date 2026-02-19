from django.contrib import admin

from maintenance.models import MaintenanceAction


@admin.register(MaintenanceAction)
class MaintenanceActionAdmin(admin.ModelAdmin):
    list_display = ['action_description', 'started_on', 'resolved_on', 'issue']