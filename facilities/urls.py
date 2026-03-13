from django.urls import path

from facilities.views import facility_dashboard, FacilityListView, FacilityCreateView, \
    FacilityEditView, FacilityDeleteView, FacilityDetailView

app_name = 'facilities'

urlpatterns = [
    path('', facility_dashboard, name='facility-dashboard'),
    path('list/', FacilityListView.as_view(), name='facility-list'),
    path('create/', FacilityCreateView.as_view(), name='facility-create'),
    path('<int:pk>/edit/', FacilityEditView.as_view(), name='facility-edit'),
    path('<int:pk>/delete/', FacilityDeleteView.as_view(), name='facility-delete'),
    path('<int:pk>/', FacilityDetailView.as_view(), name='facility-detail'),
]