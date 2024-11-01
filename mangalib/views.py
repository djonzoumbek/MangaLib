from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Count
from django.shortcuts import render, get_object_or_404, redirect

from mangalib.forms import BookForm, AuthorForm
from mangalib.models import Book, Author


# Create your views here.
def home(request):
    books = Book.objects.all().order_by('title')
    context = {"books": books}
    return render(request, 'mangalib/index.html', context)


def show(request, book_id):
    context = {"book": get_object_or_404(Book, pk=book_id)}
    return render(request, 'mangalib/show.html', context)


@login_required
def add(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mangalib:home')
    else:
        form = BookForm()
    return render(request, "mangalib/book_form.html", {"form": form})


#def a fonction how edit de book
@login_required
def edit(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('mangalib:home')
    else:
        form = BookForm(instance=book)
    return render(request, "mangalib/book_form.html", {"form": form})


@login_required
def delete(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    return redirect('mangalib:home')

@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mangalib:list_authors')
    else:
        form = AuthorForm()

    return render(request, 'mangalib/add_author.html', {'form': form})

def list_authors(request):
    authors = Author.objects.order_by('name').annotate(
        book_count=Count('book')
    )
    context = {"authors": authors}
    return render(request, 'mangalib/list_author.html', context)

def show_author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    context = {"author": author}
    return render(request, 'mangalib/show_author.html', context)

@login_required
@permission_required('mangalib.change_author')
def edit_author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('mangalib:list_authors')  # Redirection après sauvegarde
    else:
        form = AuthorForm(instance=author)
    return render(request, 'mangalib/add_author.html', {'form': form, 'author': author})


@permission_required('mangalib.delete_author', raise_exception=True)
def del_author(request, author_id):
    authors = get_object_or_404(Author, pk=author_id)
    authors.delete()
    return redirect('mangalib:list_authors')

