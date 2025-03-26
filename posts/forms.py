from django import forms

from .models import Post, Author


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        fields = ["title", "content", "author", "image"]


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['nick', 'email']
