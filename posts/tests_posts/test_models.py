import time

from django.test import TestCase
from posts.models import Author, Post


class AuthorModelTest(TestCase):

    def test_author_creation(self):
        author = Author.objects.create(nick="janek", email="janek@example.com")
        self.assertIsInstance(author, Author)
        self.assertEqual(str(author), "janek")

    def test_author_nick_and_email_unique(self):
        Author.objects.create(nick="janek", email="janek@example.com")

        # nick has to be unique
        with self.assertRaises(Exception):
            Author.objects.create(nick="janek", email="jan2@example.com")

        # email has to be unique
        with self.assertRaises(Exception):
            Author.objects.create(nick="jan2", email="janek@example.com")


class PostModelTest(TestCase):

    def setUp(self):
        self.author = Author.objects.create(
            nick="anna", email="anna@example.com")

    def test_post_creation_and_str(self):
        post = Post.objects.create(
            title="Hello World",
            content="Test content",
            author=self.author
        )
        self.assertIsInstance(post, Post)
        self.assertEqual(str(post), "Hello World")
        self.assertEqual(post.author, self.author)

    def test_created_and_modified_auto_fields(self):
        post = Post.objects.create(
            title="Auto Fields",
            content="Testing auto_now and auto_now_add",
            author=self.author
        )
        created_time = post.created
        modified_time = post.modified

        self.assertIsNotNone(created_time)
        self.assertIsNotNone(modified_time)
        self.assertAlmostEqual(created_time.timestamp(),
                               modified_time.timestamp(), delta=1)

        # simulate update
        time.sleep(1)
        post.title = "Updated Title"
        post.save()

        self.assertNotEqual(post.modified, modified_time)
