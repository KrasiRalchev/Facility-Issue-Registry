from django.urls import path

from facilities.views import facility_list, facility_create, facility_edit, facility_delete, facility_detail, \
    facility_dashboard

app_name = 'facilities'

urlpatterns = [
    path('', facility_dashboard, name='facility-dashboard'),
    path('list/', facility_list, name='facility-list'),
    path('create/', facility_create, name='facility-create'),
    path('<int:pk>/edit/', facility_edit, name='facility-edit'),
    path('<int:pk>/delete/', facility_delete, name='facility-delete'),
    path('<int:pk>/', facility_detail, name='facility-detail'),
]