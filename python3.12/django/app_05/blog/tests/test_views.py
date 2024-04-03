import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()
from django.test import TestCase
from django.urls import reverse


class RootPageTest(TestCase):
    """Test for views post_list, post_detail, post_share"""

    def test_url_for_root_page_correct(self):
        response = self.client.get("/blog", follow=True)
        self.assertEqual(response.status_code, 200)

    def test_url_share_post(self):
        response = self.client.get("")
