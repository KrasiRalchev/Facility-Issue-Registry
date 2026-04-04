from django.test import TestCase
from facilities.models import Unit, Facility

class FacilityModelTests(TestCase):
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

    def test_unit_str(self):
        self.assertEqual(str(self.unit), "UnitA")

    def test_facility_str(self):
        self.assertEqual(str(self.facility), "Fac1")