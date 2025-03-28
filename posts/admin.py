from django.contrib import admin

from .models import Post, Author, Tag


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('nick', 'email')
    search_fields = ('nick', 'email')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created', 'modified')
    search_fields = ('title', 'content', 'author__nick')
    list_filter = ('created', 'author')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
