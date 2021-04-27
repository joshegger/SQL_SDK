from book import Book
import booksSDK

booksSDK.delete_books()

books = [
    Book("Book_1", 1),
    Book("Book_2", 2),
    Book("Book_3", 3),
    Book("Book_4", 4)
]

booksSDK.add_books(books)


print(booksSDK.get_books())

print(booksSDK.get_book_by_title("Book_1"))






