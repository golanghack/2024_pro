from django.test import TestCase
from account.models import Profile
from account.models import Contact


class TestProfile(TestCase):
    """Model Profile unit test."""

    def setUpTestData(cls):
        Profile.objects.create()
