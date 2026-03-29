from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from issues.choices import Status_choices
from issues.models import Issue
from maintenance.forms import MaintenanceCreateForm, MaintenanceResolveForm
from maintenance.models import MaintenanceAction

from django.views.generic import CreateView
from django.shortcuts import get_object_or_404
from django.urls import reverse


class ActionCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = MaintenanceAction
    form_class = MaintenanceCreateForm
    template_name = 'maintenance/action_create.html'

    permission_required = 'maintenance.add_maintenanceaction'

    def dispatch(self, request, *args, **kwargs):
        self.issue = get_object_or_404(Issue, pk=self.kwargs['issue_pk'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.issue = self.issue
        response = super().form_valid(form)

        self.issue.status = Status_choices.IN_PROGRESS
        self.issue.save()

        return response

    def get_success_url(self):
        return reverse('issues:issue-detail', kwargs={'pk': self.issue.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issue'] = self.issue
        return context

@login_required
@permission_required('maintenance.change_maintenanceaction')
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







