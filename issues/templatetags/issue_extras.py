from django import template

from facilities.models import Facility
from issues.choices import Status_choices
from issues.models import Issue


register = template.Library()

@register.simple_tag
def open_issues_count():
    return Issue.objects.filter(
        status__in=[Status_choices.OPEN, Status_choices.IN_PROGRESS]).count()

@register.simple_tag
def total_facilities():
    return Facility.objects.all().count()