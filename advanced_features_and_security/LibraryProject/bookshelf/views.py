from django.contrib.auth.decorators import permission_required
from django.shortcuts import render

@permission_required('bookshelf.can_view', raise_exception=True)
def example_list(request):
    return render(request, "bookshelf/example_list.html")

@permission_required('bookshelf.can_create', raise_exception=True)
def example_create(request):
    return render(request, "bookshelf/example_create.html")

@permission_required('bookshelf.can_edit', raise_exception=True)
def example_edit(request, pk):
    return render(request, "bookshelf/example_edit.html")

@permission_required('bookshelf.can_delete', raise_exception=True)
def example_delete(request, pk):
    return render(request, "bookshelf/example_delete.html")
