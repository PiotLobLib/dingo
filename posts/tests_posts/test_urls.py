from django.test import SimpleTestCase
from django.urls import reverse, resolve
from posts import views


class PostUrlsTest(SimpleTestCase):

    def test_post_list_url_resolves(self):
        url = reverse('posts:post_list')
        self.assertEqual(resolve(url).func, views.post_list)

    def test_post_detail_url_resolves(self):
        url = reverse('posts:post_detail', args=[1])
        self.assertEqual(resolve(url).func, views.post_detail)

    def test_post_create_url_resolves(self):
        url = reverse('posts:post_create')
        self.assertEqual(resolve(url).func, views.post_create)


class AuthorUrlsTest(SimpleTestCase):

    def test_author_list_url_resolves(self):
        url = reverse('posts:author_list')
        self.assertEqual(resolve(url).func, views.author_list)

    def test_author_detail_url_resolves(self):
        url = reverse('posts:author_detail', args=[1])
        self.assertEqual(resolve(url).func, views.author_detail)

    def test_author_create_url_resolves(self):
        url = reverse('posts:author_create')
        self.assertEqual(resolve(url).func, views.author_create)
