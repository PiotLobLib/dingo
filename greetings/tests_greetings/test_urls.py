from django.test import SimpleTestCase
from django.http import HttpRequest
from greetings import urls as greetings_urls


class GreetingsUrlsTest(SimpleTestCase):

    def test_root_url_returns_hello_world(self):
        request = HttpRequest()
        response = greetings_urls.urlpatterns[0].callback(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), "Hello World!")

    def test_name_url_returns_capitalized_greeting(self):
        request = HttpRequest()
        response = greetings_urls.urlpatterns[1].callback(
            request, name="piotr")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), "Hello Piotr!")
