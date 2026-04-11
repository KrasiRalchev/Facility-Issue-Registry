from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from common.mixins import NotFoundRedirectMixin
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

        if self.request.user.is_staff:
            queryset = Issue.objects.all()
        else:
            queryset = Issue.objects.filter(requester=self.request.user.get_full_name())

        status = self.request.GET.get('status')

        if status:
            queryset = queryset.filter(status__iexact=status)
        return queryset


class IssueDetailView(LoginRequiredMixin, NotFoundRedirectMixin, DetailView):
    model = Issue
    template_name = 'issues/issue_detail.html'
    context_object_name = 'issue'

    error_url = 'issues:error'


class IssueCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Issue
    form_class = IssueFormCreate
    template_name = 'issues/issue_create.html'
    success_url = reverse_lazy('facilities:dashboard')

    permission_required = 'issues.add_issue'

    def form_valid(self, form):
        form.instance.requester = self.request.user.get_full_name()
        form.instance.requester_email = self.request.user.email
        return super().form_valid(form)   # send signal to send_new_issue_notification()


class IssueEditView(LoginRequiredMixin, PermissionRequiredMixin, NotFoundRedirectMixin, UpdateView):
    model = Issue
    form_class = IssueFormEdit
    template_name = 'issues/issue_edit.html'
    success_url = reverse_lazy('facilities:dashboard')

    permission_required = 'issues.change_issue'
    error_url = 'issues:error'

class IssueDeleteView(LoginRequiredMixin, PermissionRequiredMixin, NotFoundRedirectMixin, DeleteView):
    model = Issue
    class_form = IssueFormDelete
    template_name = 'issues/issue_delete.html'
    success_url = reverse_lazy('facilities:dashboard')

    permission_required = 'issues.delete_issue'
    error_url = 'issues:error'
