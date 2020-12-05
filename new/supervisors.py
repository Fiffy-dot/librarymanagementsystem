# Author:  Fiona Nganga and Dirac Murairi
# this is the supervisors file

# we import the user file and the datetime function

from users_class import User
import datetime

day = datetime.datetime.now().strftime("%d")
month = datetime.datetime.now().month
day = int(day)
month = int(month)


class Supervisor(User):
    """
    Supervisor
    ---------
    The supervisor is the person in charge of the library.
    he can:
        -   Add a book
        -   Remove a book
        -   Receive a book when a user returns it
        -   Give penalty when needed
        -   Remove a user.
    """

    def add_book(self, book_list):

        """
        add_book
        --------
        This method allows the supervisor to add a new book to the list of all books.
        it receives a list of dictionaries as arguments holding information on our books.
        add_book(book_list)
        ;return: nothing
        """
        name = input("Enter the name of the book to add: ").upper()
        id = len(book_list) + 1
        author = input("Who is the author of the book: ").upper()
        new_book = {"name": name, "id": str(id), "status": "NOT BORROWED", "author": author}
        book_list.append(new_book)
        print("You have successfully added a book")
        return 1

    def remove_book(self, book_list):

        """
        remove_book
        -----------
        This method allows the supervisor to remove a book from the book collection.
        it receives a list of dictionaries as arguments holding information on our books.
        remove_book(book_list)
        ;return: 1 when the book was removed.
        """

        i = 0  # check the index of the book to remove
        name = input("Enter the name of the book to remove: ").upper()
        id = input("Enter the id of the book you want to remove: ").upper()
        for book in book_list:
            if book["name"] == name and book["id"] == id:
                book_list.pop(i)
                print("You have removed a book from the list")
                return 1
            i += 1
        print("No book was removed from the list. Check your information")
        return 0

    def return_book(self, list_book, list_borrowed, list_users):

        """
        return_book
        -----------

        This method allows the supervisor to Remove a book from the list of
        all borrowed books when the user returns a book and assign penalty
        when needed.

        it receives a list of dictionaries as arguments holding information on our books.
        it receives a list of dictionaries as arguments holding information on our books borrowed.
        it receives a list of dictionaries as arguments holding information on our users.

        return_book(list_book, list_borrowed, list_users)
        ;return: 1 when the book was found and 0 otherwise.
        """
        i = 0  # check the index of the book to remove
        j = 0  # index of user
        a = 0  # index of the book
        name = input("Enter the name of the book to return: ").upper()
        id = input("Enter the id of the book you want to return: ").upper()
        user_name = input("Enter the name of the book's user: ").upper()
        user_mail = input("Enter the email address of the user: ").lower()

        # get the index of the book in the list of all books
        for book in list_book:
            if book["name"] == name and id == book["id"]:
                break
            a += 1

        # get the index of the user who borrowed the book
        for student in list_users:
            if student["name"] == user_name and user_mail == student["email"]:
                break
            j += 1

        # get the index of the book borrowed in the list of all borrowed books
        for book in list_borrowed:
            if name == book["book_name"] and id == book["book_id"] and list_users[j]["name"] == book["name"]:
                if day <= book["return_day"] and month <= book["return_month"]:
                    list_book[a]["status"] = "NOT BORROWED"  # change status of the book
                    list_borrowed.pop(i)  # remove the book from the borrowing list
                    print("The book was successfully returned")
                else:
                    list_book[a]["status"] = "NOT BORROWED"  # change status of the book
                    list_borrowed.pop(i)  # remove the book from the borrowing list
                    list_users[j]["penalty"] += 1  # give the user penalty
                    print("The book was returned late and the user is charged 1 more penalty")
                return 1
            i += 1

        print("Please, verify entered informations")
        return 0

    def remove_penalty(self, list_users):

        """
        remove_penalty
        --------------
        This method allows the supervisor to remove penalties given to a user.
        it receives a list of dictionaries as arguments holding informations on our users.
        remove_penalty(list_users)
        ;return: 0 when the user couldn't be found.
        """

        user_name = input("Enter the name of the book's user: ").upper()
        user_mail = input("Enter the email address of the user: ").lower()

        # remove penalties
        for user in list_users:
            if user["name"] == user_name and user["email"] == user_mail:
                if user["penalty"] != 0:
                    user["penalty"] = 0
                    print("You have 0 penalty now")
                else:
                    print("You don't have any penalty")
                    return 0
            else:
                print("we couldn't find this user")
                return 0

    def remove_user(self, list_users):

        """
        remove_user
        -----------
        This method takes as arguments the list of all users and removes a specific user.
        it receives a list of dictionaries as arguments holding information on our users.
        remove_user(list_users)
        ;return: 0 when there is an error, 1 when we removed the user
        """
        i = 0  # the index of the user

        user_name = input("Enter the name of the book's user: ").upper()
        user_mail = input("Enter the email address of the user: ").lower()

        for user in list_users:
            if user["name"] == user_name and user["email"] == user_mail:
                list_users.pop(i)
                return 1
            i += 1
        print("we couldn't find this user")
        return 0

# here we are using random sample data that will be used to test whether the file is working


su = Supervisor("kwame", "dirac", "002")
# print(su.name)
# this is a list with dictionaries of different books
books = [{"name": "PYTHON", "id": "1", "status": "BORROWED", "author": "DIRAC"},
         {"name": "JAVA", "id": "2", "status": "NOT BORROWED", "author": "ACHILLE"},
         {"name": "PYTHON FOR EVERYBODY", "id": "3", "status": "NOT BORROWED", "author": "FIONA"},
         {"name": "C++", "id": "4", "status": "NOT BORROWED", "author": "FIONA"},
         {"name": "MFC", "id": "5", "status": "NOT BORROWED", "author": "ACHILLE"},
         {"name": "HARRY POTTER", "id": "6", "status": "BORROWED", "author": "DIRAC"},
         {"name": "PYTHON THE NORMAL WAY", "id": "7", "status": "BORROWED", "author": "DIRAC"}]
# su.add_book(books)
# su.add_book(books)
# print(books)
# su.remove_book(books)
# print(books)
# this is a list with a dictionary of details of those who have borrowed books and the books
borrowed = [{"name": "DIRAC", "mail": "d.murairi@alustudent.com",
             "book_name": "PYTHON", "book_id": "1", "month": 21, "Day": 7,
             "return_day": 28, "return_month": 11, "extended": 0}]

# this is sample data for users
users = [{"name": "DIRAC", "email": "d.murairi@alustudent.com", "id": "001",
          "year": 2020, "penalty": 0, "faculty": "CS"}]
# su.return_book(books, borrowed, users)
# print(books)
# print("====")
# print(borrowed)
# print("====")
# print(users)
# print("====")
