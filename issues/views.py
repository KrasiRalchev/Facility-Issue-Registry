from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from facilities.models import Unit
from issues.forms import IssueFormCreate, IssueFormDelete, IssueFormEdit
from issues.models import Issue


def issues_per_unit(request: HttpRequest, unit_pk: int) -> HttpResponse:
   status = request.GET.get('status')
   unit = get_object_or_404(Unit, pk=unit_pk)
   issues = Issue.objects.filter(facility__unit=unit)

   if status:
       issues = issues.filter(status=status.upper())
   context = {
        'issues': issues,
        'unit': unit,
   }
   return render(request, 'issues/unit_issues.html', context)


def issue_list(request: HttpRequest) -> HttpResponse:
    status = request.GET.get('status')
    issues = Issue.objects.all()

    if status:
        issues = issues.filter(status=status.upper())
    context = {
        'issues': issues,
    }
    return render(request, 'issues/issue_list.html', context)


def issue_detail(request: HttpRequest, pk: int) -> HttpResponse:
    issue = get_object_or_404(Issue, pk=pk)

    context = {
        'issue': issue,
    }
    return render(request, 'issues/issue_detail.html', context)


def issue_create(request: HttpRequest) -> HttpResponse:
    form = IssueFormCreate(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('issues:issue-list')

    context = {
        'form': form,
    }
    return render(request, 'issues/issue_create.html', context)


def issue_edit(request: HttpRequest, pk: int) -> HttpResponse:
    issue = get_object_or_404(Issue, pk=pk)
    form = IssueFormEdit(request.POST or None, request.FILES or None, instance=issue)

    if request.method == 'POST' and form.is_valid():
            form.save()
            return redirect('issues:issue-list')

    context = {
        'issue': issue,
        'form': form,
    }
    return render(request, 'issues/issue_edit.html', context)


def issue_delete(request: HttpRequest, pk: int) -> HttpResponse:
    issue = get_object_or_404(Issue, pk=pk)
    if request.method == 'POST':
        issue.delete()
        return redirect('issues:issue-list')
    form = IssueFormDelete(instance=issue)
    context = {
        'issue': issue,
        'form': form,
    }
    return render(request, 'issues/issue_delete.html', context)















