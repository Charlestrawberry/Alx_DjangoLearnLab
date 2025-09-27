from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

# BookViewSet handles all CRUD operations (list, create, retrieve, update, delete)
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
