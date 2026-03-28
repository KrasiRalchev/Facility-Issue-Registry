from django.urls import path

from maintenance.views import resolve_action, ActionCreateView
app_name = "maintenance"

urlpatterns = [
    path('<int:issue_pk>/create/', ActionCreateView.as_view(), name='action-create'),
    path('<int:issue_pk>/resolve/', resolve_action, name='action-resolve'),
]