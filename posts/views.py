from django.shortcuts import render, get_object_or_404, redirect

from .models import Post, Author
from .forms import PostForm, AuthorForm


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/post_detail.html', {'post': post})


def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts:post_list')
    else:
        form = PostForm()
    return render(request, 'posts/post_form.html', {'form': form})


def author_list(request):
    authors = Author.objects.all()
    return render(request, 'posts/author_list.html', {'authors': authors})


def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, 'posts/author_detail.html', {'author': author})


def author_create(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts:author_list')
    else:
        form = AuthorForm()
    return render(request, 'posts/author_form.html', {'form': form})
