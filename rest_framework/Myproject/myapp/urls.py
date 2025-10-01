from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookListCreateAPIView, BlogPostViewSet

router = DefaultRouter()
router.register(r'posts', BlogPostViewSet, basename='posts')

urlpatterns = [
    path("books/", BookListCreateAPIView.as_view(), name="book_list_create"),
    path('', include(router.urls)),
]
