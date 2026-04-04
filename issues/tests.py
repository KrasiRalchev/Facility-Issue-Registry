from django.contrib.auth.models import User
from accounts.models import Profile
from issues.models import Issue

class TestSetupMixin:
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username="u1", password="pass1234")
        cls.profile, created = Profile.objects.get_or_create(user=cls.user)

        cls.issue = Issue.objects.create(
            title="Elevator problem",
            creator=cls.user,
            description="The elevator is not working"
        )