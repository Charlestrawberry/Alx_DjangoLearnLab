from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# -----------------------------
# ListView: list all books
# -----------------------------
class BookListView(generics.ListAPIView):
    """
    API endpoint to list all books.
    Accessible to everyone (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# -----------------------------
# DetailView: retrieve single book
# -----------------------------
class BookDetailView(generics.RetrieveAPIView):
    """
    API endpoint to retrieve a book by ID.
    Accessible to everyone (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# -----------------------------
# CreateView: add a new book
# -----------------------------
class BookCreateView(generics.CreateAPIView):
    """
    API endpoint to create a new book.
    Restricted to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# -----------------------------
# UpdateView: modify existing book
# -----------------------------
class BookUpdateView(generics.UpdateAPIView):
    """
    API endpoint to update an existing book.
    Restricted to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# -----------------------------
# DeleteView: remove a book
# -----------------------------
class BookDeleteView(generics.DestroyAPIView):
    """
    API endpoint to delete a book.
    Restricted to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
