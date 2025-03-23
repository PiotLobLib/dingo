from unittest import TestCase
from django.urls import resolve, reverse
from django.urls.exceptions import Resolver404
from maths.views import Calculator, maths_list, math_details, results_list


class TestUrls(TestCase):
    def test_resolution_for_add(self):
        resolver = resolve('/maths/add/1/2')
        self.assertEqual(resolver.func, Calculator.add)

    def test_resolution_for_sub(self):
        resolver = resolve('/maths/sub/1/2')
        self.assertEqual(resolver.func, Calculator.sub)

    def test_resolution_for_mul(self):
        resolver = resolve('/maths/mul/5/6')
        self.assertEqual(resolver.func, Calculator.mul)

    def test_resolution_for_div(self):
        resolver = resolve('/maths/div/8/2')
        self.assertEqual(resolver.func, Calculator.div)

    def test_resolution_for_math_main(self):
        resolver = resolve('/maths/')
        self.assertEqual(resolver.func, Calculator.math)

    def test_resolution_for_histories_list(self):
        url = reverse('maths:list')
        resolver = resolve(url)
        self.assertEqual(resolver.func, maths_list)

    def test_resolution_for_math_details(self):
        url = reverse('maths:details', args=[42])
        resolver = resolve(url)
        self.assertEqual(resolver.func, math_details)

    def test_resolution_for_results_list(self):
        url = reverse('maths:results')
        resolver = resolve(url)
        self.assertEqual(resolver.func, results_list)

    def test_arguments_should_be_integers_or_404(self):
        with self.assertRaises(Resolver404):
            resolve('maths/sub/a/b')
