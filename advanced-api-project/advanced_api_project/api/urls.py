from django.urls import path
from .views import BookListCreateView, BookDetailView

urlpatterns = [
    # /api/books/ → List + Create
    path('books/', BookListCreateView.as_view(), name='book-list'),

    # /api/books/<id>/ → Retrieve, Update, Delete
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
]
