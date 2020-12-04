# Author: Fiona Nganga and Dirac Murairi

from books import *
from users import *
from student import *
from facilitator import *
from supervisors import *
import datetime

date = datetime.datetime.now()
date = str(date)
print(date)
# here we initialize the library with sample books that the users can use
books = list()
book1 = {"name": "PYTHON", "id": "1", "status": "BORROWED", "author": "DIRAC"}
book2 = {"name": "PYTHON FOR EVERYBODY", "id": "3", "status": "NOT BORROWED", "author": "FIONA"}
book3 = {"name": "JAVA", "id": "2", "status": "NOT BORROWED", "author": "ACHILLE"}
book4 = {"name": "C++", "id": "4", "status": "NOT BORROWED", "author": "FIONA"}
book5 = {"name": "MFC", "id": "5", "status": "NOT BORROWED", "author": "ACHILLE"}
book6 = {"name": "HARRY POTTER", "id": "6", "status": "BORROWED", "author": "DIRAC"}
book7 = {"name": "PYTHON THE NORMAL WAY", "id": "7", "status": "BORROWED", "author": "DIRAC"}

books.append(book1)
books.append(book2)
books.append(book3)
books.append(book4)
books.append(book5)
books.append(book6)
books.append(book7)
# here we initialize sample users for the library
users = list()
user1 = {"name": "DIRAC", "email": "d.murairi@alustudent.com", "id": "001",
         "year": 2020, "penalty": 0, "faculty": "CS"}
user2 = {"name": "Fiona", "f.nganga@alustudent.com": "f.nganga@alustudent.com", "id": "002",
         "year": 2020, "penalty": 0, "faculty": "CS"}
users.append(user1)
users.append(user2)
# this is a list with a dictionary of details of those who have borrowed books and the books borrowed
borrowed_books = []

print("The books we have in our library are: ")
print("=" * 50)
for book in books:
    print(book)
print("=" * 50)


def main():
    """

    """
    name = input("What is your name? ")
    filename = name
    with open(filename, "a") as f:
        f.write("This is the file  for " + filename + "\n")
    supervisor_actions = ['See all Books', 'Find a specific book', 'Search for a book by its author',
                          'Search for a book', 'Add a book', 'Remove a book', 'Receive a book from a user',
                          'Remove penalty after user pays', 'Remove User', 'Exit']
    student_actions = ['See all Books', 'Find a specific book', 'Search for a book by its author', 'Search for a book',
                       'Borrow a book', 'Extend borrowing time for a book', 'Exit']
    facilitator_actions = ['See all Books', 'Find a specific book', 'Search for a book by its author',
                           'Search for a book', 'Borrow a book', 'Extend borrowing time for a book', 'Exit']
    role = int(input("""Are you logging in as a:

             choose 1 for Supervisor
             choose 2 for Student
             choose 3 for Facilitator :
             """))
    print("What do you want to do today?")
    if role == 1:
        repeat_actions = True
        with open(filename, "a") as f:
            f.write("This file is for a Supervisor\n")
        with open(filename, "a") as f:
            f.write("Date : {}".format(date) + "\n")
        email = input("What is your email? ")
        with open(filename, "a") as f:
            f.write("Email address : " + email + "\n")
        id = input("What is your id? ")
        with open(filename, "a") as f:
            f.write("ID: " + str(id)+ "\n")
        while repeat_actions:
            i = 1
            for action in supervisor_actions:
                print(f'{i} {action}')
                i += 1
            action = int(input("Select one action (1 - 10): "))
            with open(filename, "a") as f:
                f.write("Action Executed: " + supervisor_actions[action - 1] + '\n')
            if action == 1:
                details = User(name, email, id)
                User.see_all_books(details, books)
            elif action == 2:
                details = User(name, email, id)
                User.find_specific_book(details, books)
            elif action == 3:
                details = User(name, email, id)
                User.search_by_author(details, books)
            elif action == 4:
                details = User(name, email, id)
                User.search_for_book(details, books)
            elif action == 5:
                details = Supervisor(name, email, id)
                Supervisor.add_book(details, books)
            elif action == 6:
                details = Supervisor(name, email, id)
                Supervisor.remove_book(details, books)
            elif action == 7:
                details = Supervisor(name, email, id)
                Supervisor.return_book(details, books, borrowed_books, users)
            elif action == 8:
                details = Supervisor(name, email, id)
                Supervisor.remove_penalty(details, users)
            elif action == 9:
                details = Supervisor(name, email, id)
                Supervisor.remove_user(details, users)
            elif action == 10:
                print("Thank you, see you soon!")
                quit()
            repeat_actions = input('Would you want to perform another action? yes or no ').lower()
            with open(filename, "a") as f:
                f.write('Would you want to perform another action? ' + str(repeat_actions) + "\n")
            if repeat_actions == 'y' or repeat_actions == 'yes':
                repeat_actions = True
            else:
                repeat_actions = False
    elif role == 2:
        repeat_actions = True
        with open(filename, "a") as f:
            f.write("This file is for a Student\n")
        with open(filename, "a") as f:
            f.write("Date : {}".format(date) + "\n")
        email = input("What is your email? ")
        with open(filename, "a") as f:
            f.write("Email address : " + email + "\n")
        id = input("What is your id? ")
        with open(filename, "a") as f:
            f.write("ID: " + str(id) + "\n")
        faculty = input("What faculty are you in?(eg CS,IBT,GC,EL):  ")
        with open(filename, "a") as f:
            f.write("Faculty: " + faculty + "\n")
        year = input("What year are you in(Please type in numbers as in '1','2'): ")
        with open(filename, "a") as f:
            f.write("Academic Year : " + str(year) + "\n")
        while repeat_actions:
            i = 1
            for action in student_actions:
                print(f'{i} {action}')
                i += 1
            action = int(input("Select one action (1 - 7): "))
            with open(filename, "a") as f:
                f.write("Action Executed: " + student_actions[action - 1] + '\n')
            if action == 1:
                details = User(name, email, id)
                User.see_all_books(details, books)
            elif action == 2:
                details = User(name, email, id)
                User.find_specific_book(details, books)
            elif action == 3:
                details = User(name, email, id)
                User.search_by_author(details, books)
            elif action == 4:
                details = User(name, email, id)
                User.search_for_book(details, books)
            elif action == 5:
                details = Student(name, email, id, faculty, year)
                Student.borrow_book(details, books, borrowed_books)
            elif action == 6:
                details = Student(name, email, id, faculty, year)
                details.extend_borrowing(borrowed_books)
            elif action == 7:
                print("Thank you, see you soon!")
                quit()
            repeat_actions = input('Would you want to perform another action? yes or no ').lower()
            with open(filename, "a") as f:
                f.write('Would you want to perform another action? ' + str(repeat_actions) + "\n")
            if repeat_actions == 'y' or repeat_actions == 'yes':
                repeat_actions = True
            else:
                repeat_actions = False
    elif role == 3:
        repeat_actions = True
        with open(filename, "a") as f:
            f.write("This file is for a Supervisor\n")
        with open(filename, "a") as f:
            f.write("Date : {}".format(date) + "\n")
        email = input("What is your email? ")
        with open(filename, "a") as f:
            f.write("Email address: " + email + "\n")
        id = input("What is your id? ")
        with open(filename, "a") as f:
            f.write("ID: " + id + "\n")
        faculty = input("What faculty are you in?(eg CS,IBT,GC,EL):  ")
        with open(filename, "a") as f:
            f.write("Faculty: " + faculty + "\n")
        year = input("What year are you in since you joined ALu(Please type in numbers as in '2','3'): ")
        while repeat_actions:
            i = 1
            for action in facilitator_actions:
                print(f'{i} {action}')
                i += 1
            action = int(input("Select one action (1 - 7): "))
            with open(filename, "a") as f:
                f.write("Action executed: " + facilitator_actions[action - 1] + '\n')
            if action == 1:
                details = User(name, email, id)
                User.see_all_books(details, books)
            elif action == 2:
                details = User(name, email, id)
                User.find_specific_book(details, books)
            elif action == 3:
                details = User(name, email, id)
                User.search_by_author(details, books)
            elif action == 4:
                details = User(name, email, id)
                User.search_for_book(details, books)
            elif action == 5:
                details = Facilitator(name, email, id, faculty, year)
                Facilitator.borrow_book(details, books, borrowed_books)
            elif action == 6:
                details = Facilitator(name, email, id, faculty, year)
                Facilitator.extend_borrowing(details, borrowed_books)
            elif action == 7:
                print("Thank you, see you soon!")
                quit()
            repeat_actions = input('Would you want to perform another action? yes or no ').lower()
            with open(filename, "a") as f:
                f.write('Would you want to perform another action? ' + str(repeat_actions) + "\n")
            if repeat_actions == 'y' or repeat_actions == 'yes':
                repeat_actions = True
            else:
                repeat_actions = False


print("Thank you, keep reading!")
if __name__ == "__main__":
    main()
