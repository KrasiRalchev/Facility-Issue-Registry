from django.urls import path
from django.views.generic import TemplateView

from facilities.views import FacilityDashboardView, FacilityListView, FacilityCreateView, \
    FacilityEditView, FacilityDeleteView, FacilityDetailView

app_name = 'facilities'

urlpatterns = [
    path('dashboard/', FacilityDashboardView.as_view(), name='dashboard'),
    path('list/', FacilityListView.as_view(), name='facility-list'),
    path('create/', FacilityCreateView.as_view(), name='facility-create'),
    path('<int:pk>/edit/', FacilityEditView.as_view(), name='facility-edit'),
    path('<int:pk>/delete/', FacilityDeleteView.as_view(), name='facility-delete'),
    path('<int:pk>/', FacilityDetailView.as_view(), name='facility-detail'),
    path('error/invalid_issue/', TemplateView.as_view(template_name='404.html'), name='error'),
]