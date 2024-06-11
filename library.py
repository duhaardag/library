class Library:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.books = []
        self.patrons = []


    def add_book(self, book_isbn):
        if book_isbn not in self.books:
            self.books.append(book_isbn)
        else:
            print('Book already exists')    
    def remove_book(self, book_isbn):
        if book_isbn in self.books:
            self.books.remove(book_isbn)    
        else:
            print('Book doesnt exists')        

    def add_patron(self, patron_id):
        if not patron_id in self.patrons:
            self.patrons.append(patron_id)
        else:
             print('Patron already exists')
    def remove_patron(self, patron_id):
        if patron_id in self.patrons:
            self.patrons.remove(patron_id)
        else:
            print('Patron doesnt exist')

    
    def book_rent(self, patron_id, book_id):
        if book_id in self.books:
            self.remove_book(book_id)
            print(patron_id, ' rented the book: ', book_id)
        else:
            print('Book is not available')
