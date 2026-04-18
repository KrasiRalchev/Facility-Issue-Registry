from datetime import date
from unittest import TestCase

from facilities.models import Unit, Facility
from issues.models import Issue


class IssueModelTests(TestCase):

    def setUp(self):
        self.unit = Unit.objects.create(name="IT")

        self.facility = Facility.objects.create(
            name="Server Room",
            unit=self.unit,
            location="Building A",
            cost_center="CC001",
            cc_manager="Manager1",
            installed_on=date(2020, 1, 1),
        )

        self.issue = Issue.objects.create(
            location="Room 101",
            description="AC not working",
            requester="Ivan",
            facility=self.facility
        )

