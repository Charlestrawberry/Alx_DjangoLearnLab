from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    title = models.CharField(max_length=200)
    publication_year = models.DateTimeField(auto_now_add=True)    

    def __str__(self):
        return f"{self.title} ({self.publication_year})"