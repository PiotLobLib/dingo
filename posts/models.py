from django.db import models

# Create your models here.


class Author(models.Model):
    nick = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nick


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='photos/%Y/%m/%d', null=True, blank=True)
    tags = models.ManyToManyField("posts.Tag", related_name="posts")

    def __str__(self):
        return self.title


class Tag(models.Model):
    word = models.CharField(max_length=50, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.word
