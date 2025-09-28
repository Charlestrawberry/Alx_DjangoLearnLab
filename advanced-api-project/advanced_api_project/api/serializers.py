from .models import Author, Book
from rest_framework import serializers
import datetime


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  #to add all Serializers
    
    def validate_publicationyear(self, value):
        currentyear = datetime.date.today().year
        if value > currentyear:
            raise serializers.validationError("Publication year cannot be in the future.")
        return value


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = '__all__'
    
