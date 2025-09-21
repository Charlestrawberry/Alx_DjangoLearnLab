 Create Operation

```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
# <Book: 1984 by George Orwell>


- **retrieve.md**
```markdown
# Retrieve Operation

```python
from bookshelf.models import Book
Book.objects.all()
# <QuerySet [<Book: 1984 by George Orwell>]>


- **update.md**
```markdown
# Update Operation

```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book
# <Book: Nineteen Eighty-Four by George Orwell>


- **delete.md**
```markdown
# Delete Operation

```python
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()
# <QuerySet []>