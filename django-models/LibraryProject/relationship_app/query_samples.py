import os
import sys
import django

# Add project root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# set up django envt
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Librarian, Library

def run_queries():
    # Query all books by a specific author
    author_name = "O. C. Odukoya"
    author = Author.objects.get(name=author_name)
    books_by_author = Book.objects.filter(author=author)

    print(f"Books by {author_name}")
    for book in books_by_author:
        print("-" , book.title)
    
    # Query 2: List all books in a library
    library_name = "Central Library"
    library = Library.objects.get(name=library_name)
    print(f"\nBooks in {library_name}:")
    for book in library.books.all():
        print("-", book.title)

      # 3. Retrieve the librarian for a library
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        print(f"\nLibrarian of {library_name}: {librarian.name}")
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        print(f"\nNo librarian assigned to '{library_name}'")


if __name__ == "__main__":
    run_queries()