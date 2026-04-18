from django.urls import path
from django.views.generic import TemplateView

from issues.views import UnitIssuesView, IssueListView, IssueDetailView, IssueCreateView,\
                         IssueEditView, IssueDeleteView

app_name = 'issues'

urlpatterns = [
    path('', IssueListView.as_view(), name='issue-list'),
    path('<int:unit_pk>/issues/', UnitIssuesView.as_view(), name='unit-issues'),
    path('<int:pk>/detail', IssueDetailView.as_view(), name='issue-detail'),
    path('create/', IssueCreateView.as_view(), name='issue-create'),
    path('<int:pk>/edit/', IssueEditView.as_view(), name='issue-edit'),
    path('<int:pk>/delete/', IssueDeleteView.as_view(), name='issue-delete'),
    path('error/invalid_issue/', TemplateView.as_view(template_name='404.html'), name='error'),
    ]