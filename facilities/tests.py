from django.contrib.auth.models import User
from django.test import TestCase
from datetime import date

from django.urls import reverse

from .forms import FacilityCreateForm
from .models import Unit, Facility


class UnitFacilityTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.unit = Unit.objects.create(name="IT")

        cls.facility = Facility.objects.create(
            name="Server Room",
            unit=cls.unit,
            location="Building A",
            cost_center="CC001",
            cc_manager="Manager1",
            inventory_number="INV001",
            description="Main room",
            installed_on=date(2020, 1, 1),
            is_active=True
        )

    def test_facility_str(self):
        self.assertEqual(str(self.facility), "Server Room")

    def test_facility_optional_fields(self):
        facility = Facility.objects.create(
            name="No Inventory",
            unit=self.unit,
            location="C",
            cost_center="CC003",
            cc_manager="Manager3",
            installed_on=date(2022, 1, 1)
        )
        self.assertIsNone(facility.inventory_number)
        self.assertEqual(facility.description, "")

    def test_facility_ordering(self):
        Facility.objects.create(
            name="AAA Facility",
            unit=self.unit,
            location="Test",
            cost_center="CC004",
            cc_manager="Manager4",
            installed_on=date(2023, 1, 1)
        )

        facilities = Facility.objects.all()
        self.assertEqual(facilities[0].name, "AAA Facility")


class FacilityViewsTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username="user1", password="pass1234")

        cls.unit = Unit.objects.create(name="IT")

        cls.facility = Facility.objects.create(
            name="Server Room",
            unit=cls.unit,
            location="Building A",
            cost_center="CC001",
            cc_manager="Manager1",
            installed_on=date(2020, 1, 1),
            is_active=True
        )

    def test_facility_list_requires_login(self):
        url = reverse("facilities:facility-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_facility_list_after_login(self):
        self.client.login(username="user1", password="pass1234")
        url = reverse("facilities:facility-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class FacilityFormTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.unit = Unit.objects.create(name="IT")

    def test_valid_form(self):
        form = FacilityCreateForm(data={
            "name": "Server Room",
            "unit": self.unit.id,
            "location": "Building A",
            "cost_center": "CC001",
            "cc_manager": "Manager1",
            "installed_on": date(2020, 1, 1)
        })
        self.assertTrue(form.is_valid())

    def test_name_validation_min_length(self):
        form = FacilityCreateForm(data={
            "name": "AB",  # < 3 символа
            "unit": self.unit.id,
            "location": "Building A",
            "cost_center": "CC001",
            "cc_manager": "Manager1",
            "installed_on": date(2020, 1, 1)
        })
        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors)