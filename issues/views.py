from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from facilities.models import Unit
from issues.forms import IssueFormCreate, IssueFormDelete, IssueFormEdit
from issues.models import Issue


class UnitIssuesView(LoginRequiredMixin, ListView):
    model = Issue
    template_name = 'issues/unit_issues.html'
    context_object_name = 'issues'

    def get_queryset(self):
        unit_pk = self.kwargs['unit_pk']
        self.unit = get_object_or_404(Unit, pk=unit_pk)
        queryset =  Issue.objects.filter(facility__unit=self.unit)

        status = self.request.GET.get('status')

        if status:
            queryset = queryset.filter(status=status.upper())
        return queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['unit'] = self.unit
        return context


class IssueListView(LoginRequiredMixin, ListView):
    model = Issue
    template_name = 'issues/issue_list.html'
    context_object_name = 'issues'

    def get_queryset(self):
        queryset = Issue.objects.all()

        status = self.request.GET.get('status')

        if status:
            queryset = queryset.filter(status__iexact=status)
        return queryset


class IssueDetailView(LoginRequiredMixin, DetailView):
    model = Issue
    template_name = 'issues/issue_detail.html'
    context_object_name = 'issue'


class IssueCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Issue
    form_class = IssueFormCreate
    template_name = 'issues/issue_create.html'
    success_url = reverse_lazy('facilities:dashboard')

    permission_required = 'issues.add_issue'


class IssueEditView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Issue
    form_class = IssueFormEdit
    template_name = 'issues/issue_edit.html'
    success_url = reverse_lazy('facilities:dashboard')

    permission_required = 'issues.change_issue'


class IssueDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Issue
    class_form = IssueFormDelete
    template_name = 'issues/issue_delete.html'
    success_url = reverse_lazy('facilities:dashboard')

    permission_required = 'issues.delete_issue'

