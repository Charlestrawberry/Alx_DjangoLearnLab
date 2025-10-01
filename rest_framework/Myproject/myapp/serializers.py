from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


from rest_framework import serializers
from django.contrib.auth.models import User
from .models import BlogPost, Comment, Like

# 2.1 Custom User serializer with full_name
class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'full_name']

    def get_full_name(self, obj):
        # obj is a User instance
        first = obj.first_name or ''
        last = obj.last_name or ''
        return f"{first} {last}".strip()


# 2.2 Comment serializer (nested)
class CommentSerializer(serializers.ModelSerializer):
    # we include author id etc.
    class Meta:
        model = Comment
        fields = ['id', 'author', 'content', 'created_at']


# 2.3 BlogPost serializer with nested comments & likes count
class BlogPostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, required=False)
    likes_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = BlogPost
        fields = ['id', 'author', 'title', 'content', 'created_at', 'updated_at', 'comments', 'likes_count']

    def validate(self, data):
        """
        Ensure that every comment’s author == the blog post’s author.
        (We only do this if comments are provided)
        """
        comments_data = data.get('comments', [])
        post_author = data.get('author')  # This is the user id or instance
        for c in comments_data:
            if c.get('author') != post_author:
                raise serializers.ValidationError("Each comment’s author must be the blog post’s author.")
        return data

    def create(self, validated_data):
        comments_data = validated_data.pop('comments', [])
        post = BlogPost.objects.create(**validated_data)
        for cdata in comments_data:
            Comment.objects.create(post=post, **cdata)
        return post

    def update(self, instance, validated_data):
        comments_data = validated_data.pop('comments', None)
        # update basic fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if comments_data is not None:
            # simple approach: delete existing comments and recreate
            instance.comments.all().delete()
            for cdata in comments_data:
                Comment.objects.create(post=instance, **cdata)

        return instance
