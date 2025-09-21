from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from .models import Book

def safe_search(request):
    query = request.GET.get('q', '')  # user input
    # ❌ DANGEROUS: SQL injection risk
    # results = ExampleModel.objects.raw(f"SELECT * FROM bookshelf_examplemodel WHERE title = '{query}'")

    # ✅ SAFE: ORM auto-escapes input
    results = Book.objects.filter(title__icontains=query)

    return render(request, "bookshelf/search.html", {"results": results})

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    return render(request, "bookshelf/book_list.html, {'books': books}")

@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    return render(request, "bookshelf/book_create.html")

@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, pk):
    return render(request, "bookshelf/book_edit.html")

@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, pk):
    return render(request, "bookshelf/book_delete.html")
