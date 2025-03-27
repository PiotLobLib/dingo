from django.urls import path

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
    path('authors/', author_list, name='author_list'),
    path('author/<int:pk>/', author_detail, name='author_detail'),
    path('author/new/', author_create, name='author_create'),
]
