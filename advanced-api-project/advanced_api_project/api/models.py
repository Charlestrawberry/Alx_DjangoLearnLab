# api/models.py

from django.db import models

class Author(models.Model):
    """
    Author model: stores the author's name.
    - name: the full name of the author (string).
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model: stores book info.
    - title: the book title (string).
    - publication_year: the year the book was published (integer).
    - author: foreign key to Author (one author => many books).
    """
    title = models.CharField(max_length=255)
    publication_year = models.PositiveIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
