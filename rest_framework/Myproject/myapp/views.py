from rest_framework import viewsets, generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.db.models import Count
from .models import BlogPost, Like
from .serializers import BlogPostSerializer

class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BlogPostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = BlogPostSerializer

    def get_queryset(self):
        # annotate each post with a likes_count
        return BlogPost.objects.annotate(likes_count=Count('likes'))

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticatedOrReadOnly])
    def like(self, request, pk=None):
        post = self.get_object()
        user = request.user
        # Try to create a Like if none exists
        like_obj, created = Like.objects.get_or_create(post=post, user=user)
        if not created:
            # If like already exists, you might choose to remove it (unlike)
            like_obj.delete()
            # re-count
            likes = post.likes.count()
            return Response({'likes_count': likes, 'status': 'unliked'})
        else:
            likes = post.likes.count()
            return Response({'likes_count': likes, 'status': 'liked'})
