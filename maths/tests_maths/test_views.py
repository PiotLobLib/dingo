from django.test import TestCase, Client
from django.urls import reverse
from maths.models import Math, Result


class MathViewsTest(TestCase):

    def setUp(self):
        Math.objects.create(operation="sub", a=20, b=30)
        self.client = Client()

    def test_maths_list_view(self):
        response = self.client.get("/maths/histories/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["maths"]), 1)
        self.assertIn(
            '<li><a href="/maths/histories/1">id:1, a=20, b=30, op=sub</a></li>',
            response.content.decode()
        )

    def test_math_details_view(self):
        math = Math.objects.create(operation="add", a=4, b=3)
        response = self.client.get(f"/maths/histories/{math.id}")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "add")

    def test_results_list_get(self):
        Result.objects.create(value=10)
        response = self.client.get("/maths/results/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "10.0")

    def test_results_list_post_valid(self):
        data = {"value": 99.9}
        response = self.client.post("/maths/results/", data=data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Utworzono nowy Result")
        self.assertTrue(Result.objects.filter(value=99.9).exists())

    def test_results_list_post_invalid(self):
        # Invalid: both fields empty
        response = self.client.post("/maths/results/", data={}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Nie podano żadnej wartości!")

    def test_add_view_creates_math_and_result(self):
        response = self.client.get("/maths/add/2/3")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Math.objects.filter(
            operation="add", a=2, b=3).exists())
        self.assertTrue(Result.objects.filter(value=5).exists())
