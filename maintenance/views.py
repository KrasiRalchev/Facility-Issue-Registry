from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from issues.choices import Status_choices
from issues.models import Issue
from maintenance.forms import MaintenanceCreateForm, MaintenanceResolveForm


def action_create(request: HttpRequest, issue_pk: int) -> HttpResponse:
    issue = get_object_or_404(Issue, pk=issue_pk)

    form = MaintenanceCreateForm(request.POST or None)

    if request.POST and form.is_valid():
        action = form.save(commit=False)
        action.issue = issue
        action.save()
        issue.status = Status_choices.IN_PROGRESS
        issue.save()

        return redirect('issues:issue-detail', issue_pk)

    context = {
        'form': form,
        'issue': issue,
    }
    return render(request, 'maintenance/action_create.html', context)

def resolve_action(request: HttpRequest, issue_pk: int) -> HttpResponse:
    issue = get_object_or_404(Issue, pk=issue_pk)
    last_action = issue.actions.last()

    if request.method == 'POST':
        form = MaintenanceResolveForm(request.POST)
        if form.is_valid():
            action = form.save(commit=False)
            action.issue = issue
            action.save()

            issue.status = Status_choices.RESOLVED
            issue.save()

            return redirect('issues:issue-detail', issue_pk)
    else:
        form = MaintenanceResolveForm(instance=last_action)

    context = {
        'form': form,
        'issue': issue,
    }

    return render(request, 'maintenance/action_resolve.html', context)












