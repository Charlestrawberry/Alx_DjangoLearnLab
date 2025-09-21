from django.contrib.auth.decorators import permission_required
from django.shortcuts import render

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
