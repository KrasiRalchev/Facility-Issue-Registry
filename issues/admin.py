from django.contrib import admin

from issues.models import Issue, Tag


@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ['description', 'requester', 'status', 'priority', 'facility']
    search_fields = ['description', 'requester']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']