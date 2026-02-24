from django.contrib import admin

from maintenance.models import MaintenanceAction


@admin.register(MaintenanceAction)
class MaintenanceActionAdmin(admin.ModelAdmin):
    list_display = ['issue', 'started_on', 'resolved_on', 'action_description', 'performer_name']
    filter_list = ['performer']