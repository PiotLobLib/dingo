from django.urls import path
from django.views.generic import ListView

from posts.models import Osoba
from .views import (
    post_list,
    post_detail,
    post_create,
    author_list,
    author_detail,
    author_create,
    PostUpdateView
)


app_name = 'posts'

urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('post/new/', post_create, name='post_create'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    # path('post_list', ListView.as_view(model=Post), name="posts_list"),
    # posts/osoba_list.html  //  'wzrost__gte' filtr po wzroście osoby
    path('wery_tall/', ListView.as_view(queryset=Osoba.objects.filter(wzrost__gte=200))),
    path('authors/', author_list, name='author_list'),
    path('author/<int:pk>/', author_detail, name='author_detail'),
    path('author/new/', author_create, name='author_create'),
]
