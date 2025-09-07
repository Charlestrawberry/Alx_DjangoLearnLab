from django.db import models

# Create your models here.
# Author one to many
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

# one to many
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return f"{self.title} by {self.author}"
    
class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book,  related_name='libraries')

    def  __str__(self):
        return f"{self.name} is with {self.books}"
    
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarians')

    def __str__(self):
        return f"{self.name} ({self.library.name})"