# this class represents the users of the library at ALU
class User:
    """
              User
              ---------
              The user is a user of the library.
              The user can:
                  -   See all books
                  -   Find specific books
                  -   Search a book by its author
                  -   Search for a book
              """

    def __init__(self, name, email, id):
        self.id = id
        self.name = name
        self.email = email

    def see_all_books(self, book_list):
        """
               see_all_books
               ------------
               This method helps the user to see all books
               that the library has and display if it’s borrowed or not.
               it receive as the first argument a list of dictionaries.
               see_all_book (list)
               ;return: 0 when the list is empty.
               """
        if len(book_list) == 0:
            print("There are no books available.")
            return 0
        for book in book_list:
            bi = book["id"]
            bn = book["name"]
            bs = book["status"]
            print("ID: {} Name: {} Status: {}".format(bi, bn, bs))

    def find_specific_book(self, book_list):

        """
        Find_specific_book
        ------------------
        This method helps the user to list a specific
        book using the name of the book given.
        it receives a list of dictionaries as argument.
        find_specific_book(lst)
        ;return: 0 when the list is empty or the book can't be found.
        """

        if len(book_list) == 0:
            print("There are no books available.")
            return 0
        i = 0
        book_name = input("Tell us the name of the book: ").upper()

        for book in book_list:
            if book_name == book["name"]:
                i += 1
                bi = book["id"]
                bn = book["name"]
                bs = book["status"]
                print("ID: {} Name: {} Status: {}".format(bi, bn, bs))
                return 1
        if i == 0:
            print("The book {} was not found in the list of books".format(book_name))
            return 0

    def search_by_author(self, book_list):

        """
        Search_by_author
        ----------------
        This module allows the user to look for a book by author name
        it receives a list of dictionaries as arguments.
        search_by_author(book_list)
        ;return: 0 when the list is empty or the book can't be found.
        """
        if len(book_list) == 0:
            print("There are no books available.")
            return 0
        i = 0
        book_author = input("Tell us the name of the author: ").upper()

        for book in book_list:
            if book_author == book["author"]:
                i += 1
                bi = book["id"]
                bn = book["name"]
                bs = book["status"]
                print("ID: {} Name: {} Status: {}".format(bi, bn, bs))

        if i == 0:
            print("The author {} has no book in our library".format(book_author))
            return 0

    def search_for_book(self, book_list):

        """
        Search_for_book
        ---------------
        This method lists all books that match one pattern of the research’s
        sentence.
        it receives as argument a list of dictionaries.
        ;return: 0 when the list is empty or no book was found.
        """

        if len(book_list) == 0:
            print("There are no books available.")
            return 0
        i = 0
        book_name = input("Tell us some elements of the book's title: ").upper()

        # to analyze the user input
        book_name = book_name.split(" ")

        # remove unnecessary worlds
        unnecessary_words = ["IN", "AT", "THE", "OR", "FOR", "THERE"]
        book_name = [book for book in book_name if book not in unnecessary_words]

        # Find those books
        for pattern in book_name:
            for book in book_list:
                if pattern in book["name"]:
                    i += 1
                    bi = book["id"]
                    bn = book["name"]
                    bs = book["status"]
                    print("ID: {} Name: {} Status: {}".format(bi, bn, bs))

        if i == 0:
            print("The book {} was not found in the list of books".format(book_name))
            return 0