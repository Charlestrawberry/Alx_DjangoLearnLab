from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

# -------------------------------
# LIST + CREATE VIEW
# -------------------------------
# - GET /books/  → List all books
# - POST /books/ → Create a new book (requires login)
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # anyone can read, only logged-in users can create

    # Enable filtering and searching
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['title', 'author', 'publication_year']  # filter by these fields
    search_fields = ['title', 'author']  # allows search queries like ?search=python


# -------------------------------
# RETRIEVE + UPDATE + DELETE VIEW
# -------------------------------
# - GET /books/<id>/    → Get a single book
# - PUT /books/<id>/    → Update book (requires login)
# - DELETE /books/<id>/ → Delete book (requires login)
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # anyone can read, only logged-in users can edit/delete
