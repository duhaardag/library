from patron import Patron
from book import Book
from library import Library

patron_1 = Patron('Duha', 18, 'Male', '34496')
library_1 = Library('wseiz', 'Rejtana 17')

book_1 = Book('Harry Potter', 'JK Rowling', '23432tew')
book_2 = Book('Harry Potter 2', 'JK Rowling', '94124r1jek')

library_1.add_book(book_1.isbn)
# library_1.add_book(book_2.isbn)
# library_1.remove_book(book_2.isbn)
library_1.add_patron(patron_1.id)
library_1.remove_patron(patron_1.id)
library_1.book_rent(patron_1.id, book_2.isbn)
print(library_1.books)
print(library_1.patrons)
