# Create Operation

```python
from bookshelf.models import Book
book = Book.objects.get(title='1984')
book

# <QuerySet [<Book: 1984 by George Orwell>]>