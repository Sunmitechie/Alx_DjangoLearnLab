from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
# Confirm deletion
books = Book.objects.all()
print(books)
# Expected output: QuerySet containing no books