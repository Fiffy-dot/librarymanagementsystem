# Author: Fiona Nganga and Dirac Murairi
# this is a file for books in the library
# we create a list for all books and dictionaries with individual book details
books = list()
book1 = {"book name": "harry potter and the chamber of secrets", "book id": "1234567", "published date": "02/07/1998",
         "category": "digital", "status": "available", "acquisition date": "08/09/2020"}
book2 = {"book name": "learn python the hard way", "book id": "8765432", "published date": "09/19/2013",
         "category": "paper", "status": "available", "acquisition date": "01/11/2020"}


# this is the class that represents the books
class Book:
    """
    -----
    Book

    This is the class that instantiates the books

    """
    def __init__(self, name, id, status, author):
        self.name = name
        self.id = id
        self.status = status
        self.author = author
