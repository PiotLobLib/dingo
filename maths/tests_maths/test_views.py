from django.test import TestCase, Client
from django.urls import reverse

from maths.models import Math, Result


class MathViewsTest(TestCase):
    fixtures = ['math', 'result']

    def setUp(self):
        self.client = Client()

    def test_get_first_3(self):
        response = self.client.get("/maths/histories/?page=3")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["maths"]), 3)

    def test_maths_list_view(self):
        math = Math.objects.create(operation="sub", a=20, b=30)
        response = self.client.get(reverse("maths:list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response, f'<td><a href="/maths/histories/{math.id}">{math.id}</a></td>')
        self.assertContains(response, f"<td>{math.a}</td>")
        self.assertContains(response, f"<td>{math.b}</td>")
        self.assertContains(response, f"<td>{math.operation}</td>")

    def test_math_details_view(self):
        math = Math.objects.create(operation="add", a=4, b=3)
        response = self.client.get(f"/maths/histories/{math.id}")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "add")

    def test_results_list_get(self):
        Result.objects.create(value=550)
        response = self.client.get("/maths/results/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "550.0")

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
