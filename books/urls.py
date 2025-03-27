from django.urls import path

from . import views


app_name = "books"

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('authors/', views.author_list, name='author_list'),
    path('author/<int:pk>/', views.author_detail, name='author_detail'),
    path('my-borrows/', views.user_borrows, name='user_borrows'),
]
