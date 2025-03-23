from django.test import TestCase
from maths.models import Result
from maths.forms import ResultForm


class ResultFormTest(TestCase):

    def test_result_save_correct_data(self):
        data = {"value": 200}
        self.assertEqual(len(Result.objects.all()), 0)

        form = ResultForm(data=data)
        self.assertTrue(form.is_valid())

        r = form.save()
        self.assertIsInstance(r, Result)
        self.assertEqual(r.value, 200)
        self.assertIsNotNone(r.id)
        self.assertIsNone(r.error)

    def test_form_valid_with_only_error(self):
        form = ResultForm(data={"error": "ZeroDivisionError"})
        self.assertTrue(form.is_valid())
        result = form.save()
        self.assertIsNone(result.value)
        self.assertEqual(result.error, "ZeroDivisionError")

    def test_form_invalid_with_both_fields(self):
        form = ResultForm(data={"value": 123, "error": "Some error"})
        self.assertFalse(form.is_valid())
        self.assertIn(
            "Podaj tylko jedną z wartości",
            form.non_field_errors()[0]
        )

    def test_form_invalid_with_neither_field(self):
        form = ResultForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn(
            "Nie podano żadnej wartości!",
            form.non_field_errors()[0]
        )
