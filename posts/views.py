from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import UpdateView
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator

from .models import Post, Author
from .forms import PostForm, AuthorForm


@method_decorator(login_required, name='dispatch')
@method_decorator(permission_required('posts.change_post', raise_exception=True), name='dispatch')
class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_form.html'
    success_url = '/posts/'


def post_list(request):
    posts = Post.objects.order_by('-created')
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    posts_page = paginator.get_page(page_number)

    if request.method == "POST":
        form = PostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:post_list')
    else:
        form = PostForm()

    return render(request, "posts/post_list.html", {
        "posts": posts_page,
        "form": form
    })


# def posts_list(request):
#     posts = Post.objects.all()
#     form = PostForm()
#     if request.method == "POST":
#         form = PostForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.add_message(
#                 request,
#                 messages.SUCCESS,
#                 "Dodano nowy Post!!"
#             )


# """
# Tylko zalogowani użytkownicy będą mogli dodawać nowe posty.
# Usuniemy wtedy z naszego formularza pole author (poprzez odpowiednie ustawienie fields),
# ale model wymagać będzie nadal podania autora.
# Wtedy będziemy mogli wskazać, że to zalogowany użytkownik jest autorem w następujący sposób:
# """
# if form.is_valid():
#        post = form.save(commit=False)
#        post.author = request.user
#        post.save()


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/post_detail.html', {'post': post})


def post_create(request):
    if request.method == "POST":
        # form = PostForm(request.POST)
        # form = ResultForm(data=request.POST, files=request.FILES)
        form = PostForm(data=request.POST, files=request.FILES)
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
