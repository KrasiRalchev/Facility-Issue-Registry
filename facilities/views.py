from django.db.models import Count, Q
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from facilities.forms import FacilityCreateForm, FacilityEditForm, FacilityDeleteForm
from facilities.models import Facility, Unit
from issues.choices import Status_choices


def facility_dashboard(request):

    units = Unit.objects.annotate(
       open_issues_count=Count(
            'facilities__issues',
            filter=Q(
                facilities__is_active=True,
                facilities__issues__status__in=[Status_choices.OPEN]
            ),
            distinct=True
        ),
        in_progress_issues_count=Count('facilities__issues', filter=Q(
            facilities__is_active=True,
            facilities__issues__status__in=[Status_choices.IN_PROGRESS]
            ),
            distinct=True
        ),
        resolved_issues_count=Count('facilities__issues', filter=Q(
            facilities__is_active=True,
            facilities__issues__status__in=[Status_choices.RESOLVED]
            ),
            distinct=True
        )
    )

    context = {
        'units': units,
    }
    return render(request, 'facilities/facility_dashboard.html', context)


def facility_list(request):
    facilities = Facility.objects.filter(is_active=True)

    context = {
        'facilities': facilities,
    }
    return render(request, 'facilities/facility_list.html', context)


def facility_create(request: HttpRequest) -> HttpResponse:
    form = FacilityCreateForm(request.POST or None, request.FILES or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('facilities:facility-list')

    context = {
        'form': form,
    }
    return render(request, 'facilities/facility_create.html', context)


def facility_edit(request: HttpRequest, pk: int) -> HttpResponse:
    facility = get_object_or_404(Facility, pk=pk)
    form = FacilityEditForm(request.POST or None, request.FILES or None, instance=facility)

    if form.is_valid():
        form.save()
        return redirect('facilities:facility-list')

    context = {
        'form': form,
    }
    return render(request, 'facilities/facility_edit.html', context)


def facility_delete(request: HttpRequest, pk: int) -> HttpResponse:
    facility = get_object_or_404(Facility, pk=pk)

    if request.method == 'POST':
        facility.delete()
        return redirect('facilities:facility-list')

    form = FacilityDeleteForm(instance=facility)

    context = {
        'form': form,
    }

    return render(request, 'facilities/facility_delete.html', context)


def facility_detail(request: HttpRequest, pk: int) -> HttpResponse:
    facility = get_object_or_404(Facility, pk=pk)

    context = {
        'facility': facility,
    }
    return render(request, 'facilities/facility_detail.html', context)






