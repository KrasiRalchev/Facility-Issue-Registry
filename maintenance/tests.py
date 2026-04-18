from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User, Permission
from unittest.mock import patch
from datetime import date

from facilities.models import Facility, Unit
from issues.models import Issue
from issues.choices import Status_choices, Priority_choices
from maintenance.models import MaintenanceAction


@patch("issues.signals.send_issue_email.delay")
class MaintenanceViewsTests(TestCase):

    def setUp(self):
        self.client = Client()

        self.unit = Unit.objects.create(name="Main Unit")

        self.facility = Facility.objects.create(
            name="Main Building",
            unit=self.unit,
            location="Campus A",
            cost_center="12345",
            cc_manager="Manager Name",
            installed_on=date.today(),
        )

        self.issue = Issue.objects.create(
            location="Room 101",
            description="Water leak",
            requester="Ivan",
            requester_email="ivan@example.com",
            priority=Priority_choices.MEDIUM,
            status=Status_choices.OPEN,
            facility=self.facility,
        )

        self.user = User.objects.create_user(username="u", password="p")

    def test_resolve_action_post_creates_action_and_sets_resolved(self, mock_delay):
        """resolve_action (POST) трябва да създаде действие и да смени статуса на RESOLVED."""
        perm = Permission.objects.get(codename="change_maintenanceaction")
        self.user.user_permissions.add(perm)
        self.client.login(username="u", password="p")

        MaintenanceAction.objects.create(
            issue=self.issue,
            action_description="Initial",
        )

        url = reverse("maintenance:action-resolve", kwargs={"issue_pk": self.issue.pk})
        response = self.client.post(url, {
            "performer": "Tech",
            "performer_name": "John",
            "cost": 10,
            "action_description": "Fixed",
            "resolved_on": "2024-01-01",
        })

        self.issue.refresh_from_db()

        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.issue.status, Status_choices.RESOLVED)
        self.assertEqual(MaintenanceAction.objects.count(), 2)

    def test_resolve_action_get_returns_last_action_instance(self, mock_delay):
        """resolve_action (GET) трябва да върне форма с последното действие като instance."""
        perm = Permission.objects.get(codename="change_maintenanceaction")
        self.user.user_permissions.add(perm)
        self.client.login(username="u", password="p")

        last_action = MaintenanceAction.objects.create(
            issue=self.issue,
            action_description="Initial",
        )

        url = reverse("maintenance:action-resolve", kwargs={"issue_pk": self.issue.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        form = response.context["form"]
        self.assertEqual(form.instance, last_action)
