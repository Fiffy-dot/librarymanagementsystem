# Author:  Fiona Nganga and Dirac Murairi
# this is the facilitators file

from users import *
import datetime
import calendar

day = datetime.datetime.now().strftime("%d")
month = datetime.datetime.now().month
day = int(day)
month = int(month)
year = datetime.datetime.now().year
year = int(year)


# this is a class for facilitators

class Facilitator(User):
    """
           Facilitator
           ---------
           The facilitator is a user of the library.
           The facilitator can:
               -   Borrow a book
               -   Extend Borrowing time for a book
           """

    def __init__(self, name, email, id, faculty, year):
        super().__init__(name, email, id)
        self.faculty = faculty
        self.year = year
        self.penalty = 0

    def update_date(self, facilitator):
        """
        update_date
        -----------
        This method update the date accordingly to the number of days in a month.(after the user
         extends the borrowing time)
        it receives as arguments a dictionary.
        update_date(dictionary)
        ;return:nothing
        """
        # for months those have 31 days
        if facilitator["return_month"] in [1, 3, 5, 7, 8, 10, 12]:
            if facilitator["return_day"] > 17:
                facilitator["return_day"] = facilitator["return_day"] + 14 - 31

                if facilitator["return_month"] != 12:
                    facilitator["return_month"] += 1
                else:
                    facilitator["return_month"] = 1

            else:
                facilitator["return_day"] += 14

        # for months those have 30 days and February
        else:
            if facilitator["return_month"] != 2:
                if facilitator["return_day"] > 16:
                    facilitator["return_day"] = facilitator["return_day"] + 14 - 30

                    facilitator["return_month"] += 1
                else:
                    facilitator["return_day"] += 14
            else:
                # 366 days in a year where February has 29 days
                if calendar.isleap(year):
                    if facilitator["return_day"] > 15:
                        facilitator["return_day"] = facilitator["return_day"] + 14 - 29

                        facilitator["return_month"] += 1
                    else:
                        facilitator["return_day"] += 14
                # 365 days in a year where February has 28 days
                else:
                    if facilitator["return_day"] > 14:
                        facilitator["return_day"] = facilitator["return_day"] + 14 - 28

                        facilitator["return_month"] += 1
                    else:
                        facilitator["return_day"] += 14

    def extend_borrowing(self, borrowed_books):

        """
        extend_borrowing
        ----------------
        This method allows the user to extend to 14 days the time he had borrowed a book.
        it receives as argument a list of dictionaries holding information about book_borrowed.
        extend_borrowing(borrowed_books)
        ;return: nothing
        """
        book_name = input("Please enter the book you'd like to borrow: ").upper()
        for facilitator in borrowed_books:
            if facilitator["name"] == self.name and book_name == facilitator["book_name"]:
                if facilitator["extended"] < 2:
                    self.update_date(facilitator)
                    facilitator["extended"] += 1
                    print("You have successfully extended your deadline")
                else:
                    print("Sorry, You have already extended your deadline")
                    print("You are expected to bring the book on {}/{}".format(facilitator["return_day"],
                                                                               facilitator["return_month"]))
            else:
                print("Sorry, You need to borrow that book in our library")

    def borrow_book(self, book_collection, borrowed_books):

        """
        borrowed_books
        --------------
        This method allows a facilitator to borrow a certain number of books
        not more than 5 from the library.
        It adds the books borrowed to the list of books in people’s possession.
        it receives as argument a list of dictionaries holding information about book_collection.
        it receives as argument a list of dictionaries holding information about book_borrowed.
        borrow_book(book_collection, borrowed_books)
        ;return: 0 when there is an error.
        """

        i = 0  # number of books in possession
        j = 0  # number of book the user can borrow

        # print all Books
        for book in book_collection:
            print("Book name: {} status: {}".format(book["name"], book["status"]))
        # check penalty
        if self.penalty == 0:
            for facilitator in borrowed_books:
                if self.name == facilitator["name"]:
                    i += 1
                    print("{} is already in possession of {} with ID: {}".format(self.name, facilitator["book"],
                                                                                 facilitator["book_id"]))
            if i > 4:
                print("Sorry, You already have 5 books into possession")
                return 0
            else:
                print("You can only take {} books or less".format(5 - i))
        else:
            print("You have {} as penalty you need to pay before to take a book".format(self.penalty))

        # check the number of book the user want to borrow
        z = int(0)  # check the number of tries someone make or the number of actions
        while True:
            j = int(input("How many book do you want to borrow: "))
            if 5 - i < j:
                if z == 1:
                    print("Sorry, You have entered an incorrect number twice")
                    return 0
                print("You can only borrow {} book(s) or less. Try again".format(5 - i))
                z += 1
            else:
                z = 0
                break

        # borrow book
        while z < j:
            i = 0
            book_name = input("Please enter the book you'd like to borrow: ").upper()
            for book in book_collection:
                if book["name"] == book_name:
                    if book["status"] == "NOT BORROWED":
                        print("=" * 50)
                        print("Book is available in the collection")
                        book["status"] = "BORROWED"
                        new = {"name": self.name, "mail": self.email,
                               "book_name": book_name, "book_id": book["id"], "month": month, "Day": day,
                               "return_day": day, "return_month": month, "extended": 0}
                        self.update_date(new)
                        borrowed_books.append(new)
                        i += 1
                        book["status"] = "BORROWED"
                        print("You have successfully borrowed this book")
                        print("=" * 50)
            if i == 0:
                print("Sorry the book {} is not in our collection".format(book_name))

            z += 1

