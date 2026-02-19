from django.urls import path

from issues.views import issue_list, issue_detail, issue_create, issue_edit, issue_delete, issues_per_unit

app_name = 'issues'

urlpatterns = [

    path('', issue_list, name='issue-list'),
    path('<int:unit_pk>/issues/', issues_per_unit, name='unit-issues'),
    path('<int:pk>/', issue_detail, name='issue-detail'),
    path('create/', issue_create, name='issue-create'),
    path('<int:pk>/edit/', issue_edit, name='issue-edit'),
    path('<int:pk>/delete/', issue_delete, name='issue-delete'),
    ]