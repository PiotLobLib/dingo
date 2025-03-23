from django.test import TestCase
from django.urls import reverse
from posts.models import Post, Author


class PostViewsTest(TestCase):

    def setUp(self):
        self.author = Author.objects.create(
            nick="janek", email="janek@example.com")
        self.post = Post.objects.create(
            title="Test Post", content="Content here", author=self.author)

    def test_post_list_view(self):
        response = self.client.get(reverse('posts:post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Post")

    def test_post_detail_view(self):
        response = self.client.get(
            reverse('posts:post_detail', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.post.title)

    def test_post_create_view_get(self):
        response = self.client.get(reverse('posts:post_create'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<form')

    def test_post_create_view_post(self):
        data = {
            "title": "New Post",
            "content": "Some content",
            "author": self.author.id
        }
        response = self.client.post(
            reverse('posts:post_create'), data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "New Post")
        self.assertTrue(Post.objects.filter(title="New Post").exists())


class AuthorViewsTest(TestCase):

    def setUp(self):
        self.author = Author.objects.create(
            nick="ania", email="ania@example.com")

    def test_author_list_view(self):
        response = self.client.get(reverse('posts:author_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "ania")

    def test_author_detail_view(self):
        response = self.client.get(
            reverse('posts:author_detail', args=[self.author.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "ania")

    def test_author_create_view_get(self):
        response = self.client.get(reverse('posts:author_create'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<form')

    def test_author_create_view_post(self):
        data = {
            "nick": "piotr",
            "email": "piotr@example.com"
        }
        response = self.client.post(
            reverse('posts:author_create'), data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "piotr")
        self.assertTrue(Author.objects.filter(nick="piotr").exists())
