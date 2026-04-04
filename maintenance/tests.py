from django.test import TestCase
from issues.models import Issue, Status_choices
from facilities.models import Facility, Unit
from maintenance.models import MaintenanceAction

class MaintenanceModelTests(TestCase):
    def setUp(self):
        self.unit = Unit.objects.create(name="UnitA")
        self.facility = Facility.objects.create(
            name="Fac1",
            unit=self.unit,
            location="Loc1",
            cost_center="001",
            cc_manager="Mgr",
            inventory_number="INV1",
            installed_on="2020-01-01"
        )
        self.issue = Issue.objects.create(
            location="Room 101",
            description="Light broken",
            requester="UserA",
            priority="Medium",
            status=Status_choices.OPEN,
            facility=self.facility
        )
        self.action = MaintenanceAction.objects.create(
            action_description="Fix light",
            performer_name="Tech1",
            issue=self.issue,
            cost=10
        )

    def test_maintenance_action_str(self):
        self.assertIn("Room 101", str(self.action))

    def test_issue_multiple_actions(self):
        another = MaintenanceAction.objects.create(
            action_description="Check",
            performer_name="Tech2",
            issue=self.issue,
            cost=5
        )
        self.assertEqual(self.issue.actions.count(), 2)

    def test_maintenance_cost_non_negative(self):
        self.assertGreaterEqual(self.action.cost, 0)