from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .models import Book, Author, Borrow, Comment


def book_list(request):
    books = Book.objects.all().order_by('-created')
    paginator = Paginator(books, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'books/book_list.html', {'books': page_obj})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        if request.POST.get("action") == "add_comment":
            Comment.objects.create(
                book=book,
                nick=request.POST['nick'],
                content=request.POST['comment']
            )
            return redirect("books:book_detail", pk=pk)

        elif request.user.is_authenticated and book.is_available():
            Borrow.objects.create(book=book, user=request.user)
            return redirect("books:book_detail", pk=pk)

    return render(request, "books/book_detail.html", {"book": book})


def author_list(request):
    authors = Author.objects.all().order_by('name')
    paginator = Paginator(authors, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'books/author_list.html', {'authors': page_obj})


def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    books = author.books.all()
    return render(
        request,
        'books/author_detail.html',
        {'author': author, 'books': books}
    )


@login_required
def user_borrows(request):
    borrows = Borrow.objects.filter(
        user=request.user).order_by('-borrowed_at')

    if request.method == "POST" and 'borrow_id' in request.POST:
        borrow = Borrow.objects.get(
            id=request.POST['borrow_id'], user=request.user)
        if not borrow.is_returned:
            borrow.is_returned = True
            borrow.date_returned = timezone.now()
            borrow.save()
        return redirect("books:user_borrows")

    return render(request, "books/borrow_list.html", {"borrows": borrows})
