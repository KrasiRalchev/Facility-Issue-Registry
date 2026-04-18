from django.test import TestCase
from django.contrib.auth.models import User
from accounts.models import Profile
from django.urls import reverse


class AccountsAppTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username="u1", password="pass1234")
        cls.profile, created = Profile.objects.get_or_create(
            user=cls.user,
            defaults={"manager": "Manager1"}
        )

    def test_profile_detail_requires_login(self):
        url = reverse("accounts:profile", args=[self.user.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_profile_detail_when_logged_in(self):
        self.client.login(username="u1", password="pass1234")
        url = reverse("accounts:profile", args=[self.user.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_profile_str(self):
        self.assertEqual(str(self.profile), "u1 Profile")

    def test_profile_user_relation(self):
        self.assertEqual(self.profile.user, self.user)

    def test_optional_fields_are_empty_by_default(self):
        self.assertIsNone(self.profile.phone_number)
        self.assertIsNone(self.profile.birth_date)
        self.assertIsNone(self.profile.photo)