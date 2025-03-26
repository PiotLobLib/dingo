from django.urls import reverse
from django.test import TestCase


class GreetingsUrlsTest(TestCase):

    def test_about_url(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
