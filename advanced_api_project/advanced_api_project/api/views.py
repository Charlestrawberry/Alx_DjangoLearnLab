# api/views.py

from rest_framework import generics, permissions
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer

# AUTHOR VIEWS

class AuthorListCreateView(generics.ListCreateAPIView):
    """
    GET: list all authors
    POST: create an author
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AuthorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: retrieve author details (with nested books)
    PUT/PATCH: update author
    DELETE: delete author
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# BOOK VIEWS

class BookListCreateView(generics.ListCreateAPIView):
    """
    GET: list books (supports filtering, searching, ordering)
    POST: create a new book (ensures publication_year validation)
    """
    queryset = Book.objects.select_related('author').all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Filtering, searching and ordering are enabled globally via settings, but you can add local defaults if desired
    filterset_fields = ['publication_year', 'author__id']
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']


class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET/PUT/PATCH/DELETE for a single book by id.
    """
    queryset = Book.objects.select_related('author').all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
