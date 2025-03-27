from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    word = models.CharField(max_length=50, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.word


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name='books')
    description = models.TextField(blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    cover = models.ImageField(upload_to='book_covers/', null=True, blank=True)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def is_available(self):
        latest_borrow = self.borrows.order_by('-borrowed_at').first()
        return not latest_borrow or latest_borrow.is_returned


class Borrow(models.Model):
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name='borrows')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    borrowed_at = models.DateTimeField(auto_now_add=True)
    is_returned = models.BooleanField(default=False)
    returned_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.book.title} -> {self.user.username}"


class Comment(models.Model):
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name="comments")
    nick = models.CharField(max_length=50)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
