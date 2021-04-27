from book import Book
import sqlite3
def cursor():
    return sqlite3.connect("books.db").cursor()

c = cursor()
c.execute('CREATE TABLE IF NOT EXISTS books (title TEXT, pages INTEGER)')
c.connection.close()

def add_book(book):
    c = cursor()
    with c.connection:
        c.execute('INSERT INTO books VALUES (?,?)', (book.title, book.pages))
    c.connection.close()
    return c.lastrowid
    print(F"We have added {book} to the SQL database")

def add_books(books):
    c = cursor()
    with c.connection:
        for book in books:
            c.execute('INSERT INTO books VALUES(?,?);', (book.title, book.pages))
    c.connection.close()
    print("We have inserted the books into the DB")

def get_books():
    c = cursor()

    with c.connection:
        c.execute('SELECT * FROM books')

    print("The currently stored books in the DB are: ")
    data = c.fetchall()
    c.connection.close()
    if not data:
        return None

    return [Book(data[i][0],data[i][1]) for i in range(len(data))]


def get_book_by_title(title):
    c = cursor()
    with c.connection:
        c.execute('SELECT * FROM books WHERE title=?', (title,))
    data =  c.fetchone()
    c.connection.close()

    if not data:
        return None
    return Book(data[0], data[1])

def delete_books():
    c = cursor()
    with c.connection:
        c.execute('DELETE FROM books')
    c.connection.close()
    print(F"The database has been cleared")