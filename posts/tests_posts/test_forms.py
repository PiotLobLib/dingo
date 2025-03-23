from django.test import TestCase
from posts.forms import PostForm, AuthorForm
from posts.models import Post, Author


class AuthorFormTest(TestCase):

    def test_author_form_valid_data(self):
        form = AuthorForm(data={'nick': 'janek', 'email': 'janek@example.com'})
        self.assertTrue(form.is_valid())
        author = form.save()
        self.assertIsInstance(author, Author)
        self.assertEqual(author.nick, 'janek')
        self.assertEqual(author.email, 'janek@example.com')

    def test_author_form_missing_email(self):
        form = AuthorForm(data={'nick': 'janek'})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_author_form_invalid_email(self):
        form = AuthorForm(data={'nick': 'janek', 'email': 'not-an-email'})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)


class PostFormTest(TestCase):

    def setUp(self):
        self.author = Author.objects.create(
            nick='anna', email='anna@example.com')

    def test_post_form_valid_data(self):
        form = PostForm(data={
            'title': 'My Title',
            'content': 'This is a long post content.',
            'author': self.author.id
        })
        self.assertTrue(form.is_valid())
        post = form.save()
        self.assertIsInstance(post, Post)
        self.assertEqual(post.title, 'My Title')
        self.assertEqual(post.author, self.author)

    def test_post_form_missing_title(self):
        form = PostForm(data={
            'content': 'Missing title!',
            'author': self.author.id
        })
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)

    def test_post_form_missing_author(self):
        form = PostForm(data={
            'title': 'Lonely Post',
            'content': 'No author assigned.'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('author', form.errors)
