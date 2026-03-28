from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, Q
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from facilities.forms import FacilityCreateForm, FacilityEditForm, FacilityDeleteForm
from facilities.models import Facility, Unit
from issues.choices import Status_choices


class FacilityDashboardView(LoginRequiredMixin ,ListView):
    model = Unit
    template_name = 'facilities/facility_dashboard.html'
    context_object_name = 'units'

    def get_queryset(self):
        return Unit.objects.annotate(
            open_issues_count=Count(
                'facilities__issues',
                filter=Q(
                    facilities__is_active=True,
                    facilities__issues__status__in=[Status_choices.OPEN]
                ),
                distinct=True
            ),
            in_progress_issues_count=Count(
                'facilities__issues',
                filter=Q(
                    facilities__is_active=True,
                    facilities__issues__status__in=[Status_choices.IN_PROGRESS]
                ),
                distinct=True
            ),
            resolved_issues_count=Count(
                'facilities__issues',
                filter=Q(
                    facilities__is_active=True,
                    facilities__issues__status__in=[Status_choices.RESOLVED]
                ),
                distinct=True
            )
        )


class FacilityListView(LoginRequiredMixin, ListView):
    model = Facility
    template_name = 'facilities/facility_list.html'
    context_object_name = 'facilities'

    def get_queryset(self):
        return Facility.objects.filter(is_active=True)


class FacilityCreateView(LoginRequiredMixin, CreateView):
    model = Facility
    form_class = FacilityCreateForm
    template_name = 'facilities/facility_create.html'
    success_url = reverse_lazy('facilities:facility-list')


class FacilityEditView(LoginRequiredMixin, UpdateView):
    model = Facility
    form_class = FacilityEditForm
    template_name = 'facilities/facility_edit.html'
    success_url = reverse_lazy('facilities:facility-list')


class FacilityDeleteView(LoginRequiredMixin, DeleteView):
    model = Facility
    template_name = 'facilities/facility_delete.html'
    success_url = reverse_lazy('facilities:facility-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = FacilityDeleteForm(instance=self.object)
        return context


class FacilityDetailView(LoginRequiredMixin, DetailView):
    model = Facility
    template_name = 'facilities/facility_detail.html'
    context_object_name = 'facility'





