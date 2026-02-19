from django.urls import path

from maintenance.views import action_create, resolve_action

app_name = "maintenance"

urlpatterns = [
    path('<int:issue_pk>/create/', action_create, name='action-create'),
    path('<int:issue_pk>/resolve/', resolve_action, name='action-resolve'),
]