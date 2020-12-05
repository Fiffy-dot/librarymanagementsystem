import re
import csv
import sys
import datetime
from students import Student
from facilitators import Facilitator
from users_class import User
from supervisors import Supervisor

date = datetime.datetime.now()
date = str(date)

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


def validate_email(email_address, password):
    # check with re module if email is correct
    if re.match(r"[^@]+@[^@]+\.[^@]+", email_address):
        with open("files/supervisors.csv", "r") as supervisor_file:
            supervisors = supervisor_file.readlines()
            for user in supervisors:
                user = user.split(",")
                if user[1] == email_address:
                    if user[3] == password:
                        return 1, user[0], user[1], user[2]
                    else:
                        print("You have entered  an incorrect password")

        with open("files/students.csv", "r") as student_file:
            students = student_file.readlines()
            for student in students:
                student = student.split(",")
                if student[1] == email_address:
                    if student[6] == password:
                        return 2, student[0], student[1], student[2], student[5], student[3]
                    else:
                        print("You have entered  an incorrect password")

        with open("files/facilitators.csv", "r") as facilitator_file:
            facilitators = facilitator_file.readlines()
            for facilitator in facilitators:
                facilitator = facilitator.split(",")
                if facilitator[1] == email_address:
                    if facilitator[5] == password:
                        return 3, facilitator[0], facilitator[1], facilitator[2], facilitator[4]
                    else:
                        print("You have entered  an incorrect password")
        return -1
    else:
        print("You have entered an invalid email address")
        return 0


def connect(value):
    if value[0] == 1:
        # create_su and dis menu
        supervisor = Supervisor(value[1], value[2], value[3])
        supervisor_actions = ['See all Books', 'Find a specific book', 'Search for a book by its author',
                              'Search for a book', 'Add a book', 'Remove a book', 'Receive a book from a user',
                              'Remove penalty after user pays', 'Remove User', 'Exit']
        filename = value[1]
        user_file = "files/history/" + filename
        with open(user_file, "a") as f:
            f.write("This is the file  for " + filename + "\n")
            f.write("This file is for a Supervisor\n")
            f.write("Date : {}".format(date) + "\n")
            f.write("Email address : " + value[2] + "\n")
            f.write("ID: " + value[3] + "\n")
        a = 0
        while True and a < 3:
            i = 1
            for action in supervisor_actions:
                print(f'{i} {action}')
                i += 1
            try:
                action = int(input("Select one action (1 - 10): "))
            except ValueError:
                print("Your input is not a number. Try again")
                a += 1
                continue
            a = 0
            with open(user_file, "a") as f:
                f.write("Action Executed: " + supervisor_actions[action - 1] + '\n')
            if action == 1:
                supervisor.see_all_books(books)
            elif action == 2:
                supervisor.find_specific_book(books)
            elif action == 3:
                supervisor.search_by_author(books)
            elif action == 4:
                supervisor.search_for_book(books)
            elif action == 5:
                Supervisor.add_book(details, books)
            elif action == 6:
                Supervisor.remove_book(books)
            elif action == 7:
                Supervisor.return_book(books, borrowed_books, users)
            elif action == 8:
                Supervisor.remove_penalty(users)
            elif action == 9:
                Supervisor.remove_user(users)
            elif action == 10:
                print("Thank you, see you soon!")
                with open(user_file, "a") as f:
                    f.write("============== End ==============/n")
                quit()
            repeat_actions = input('Would you want to perform another action? yes or no ').lower()
            with open(user_file, "a") as f:
                f.write('Would you want to perform another action? ' + str(repeat_actions) + "\n")
            if repeat_actions == 'y' or repeat_actions == 'yes':
                continue
            else:
                with open(user_file, "a") as f:
                    f.write("============== End ==============/n")
                sys.exit()


    elif value[0] == 2:
        # create student and dis menu
        student = Student(value[1], value[2], value[3], value[4], value[5])
        student_actions = ['See all Books', 'Find a specific book', 'Search for a book by its author',
                           'Search for a book',
                           'Borrow a book', 'Extend borrowing time for a book', 'Exit']
        filename = value[1]
        user_file = "files/history/" + filename
        with open(user_file, "a") as f:
            f.write("This is the file  for " + filename + "\n")
            f.write("This file is for a Student\n")
            f.write("Date : {}".format(date) + "\n")
            f.write("Email address : " + value[2] + "\n")
            f.write("ID: " + value[3] + "\n")
            f.write("Faculty: " + value[4] + "\n")
            f.write("Academic Year : " + value[5] + "\n")

        a = 0
        while True and a < 3:
            i = 1
            for action in student_actions:
                print(f'{i} {action}')
                i += 1

            try:
                action = int(input("Select one action (1 - 7): "))
            except ValueError:
                print("Your input is not a number. Try again")
                a += 1
                continue
            a = 0
            with open(user_file, "a") as f:
                f.write("Action Executed: " + student_actions[action - 1] + '\n')
            if action == 1:
                student.see_all_books(books)
            elif action == 2:
                student.find_specific_book(books)
            elif action == 3:
                student.search_by_author(books)
            elif action == 4:
                student.search_for_book(books)
            elif action == 5:
                Student.borrow_book(books, borrowed_books)
            elif action == 6:
                student.extend_borrowing(borrowed_books)
            elif action == 7:
                print("Thank you, see you soon!")
                with open(user_file, "a") as f:
                    f.write("============== End ==============/n")
                quit()
            repeat_actions = input('Would you want to perform another action? yes or no ').lower()
            with open(user_file, "a") as f:
                f.write('Would you want to perform another action? ' + str(repeat_actions) + "\n")
            if repeat_actions == 'y' or repeat_actions == 'yes':
                continue
            else:
                with open(user_file, "a") as f:
                    f.write("============== End ==============/n")
                sys.exit()


    elif value[0] == 3:
        # create su and dis menu
        facilitator = Facilitator(value[1], value[2], value[3], value[4])
        facilitator_actions = ['See all Books', 'Find a specific book', 'Search for a book by its author',
                               'Search for a book', 'Borrow a book', 'Extend borrowing time for a book', 'Exit']
        filename = value[1]
        user_file = "files/history/" + filename
        with open(user_file, "a") as f:
            f.write("This file is for a Supervisor\n")
            f.write("Date : {}".format(date) + "\n")
            f.write("Email address: " + value[2] + "\n")
            f.write("ID: " + value[3] + "\n")
            f.write("Faculty: " + value[4] + "\n")
        a = 0
        while True and a < 3:
            i = 1
            for action in facilitator_actions:
                print(f'{i} {action}')
                i += 1
            try:
                action = int(input("Select one action (1 - 7): "))
            except ValueError:
                print("Your input is not a number. Try again")
                a += 1
                continue
            a = 0
            with open(filename, "a") as f:
                f.write("Action executed: " + facilitator_actions[action - 1] + '\n')
            if action == 1:
                facilitator.see_all_books(books)
            elif action == 2:
                facilitator.find_specific_book(books)
            elif action == 3:
                facilitator.search_by_author(books)
            elif action == 4:
                facilitator.search_for_book(books)
            elif action == 5:
                facilitator.borrow_book(books, borrowed_books)
            elif action == 6:
                facilitator.extend_borrowing(details, borrowed_books)
            elif action == 7:
                print("Thank you, see you soon!")
                with open(user_file, "a") as f:
                    f.write("============== End ==============/n")
                sys.exit()
            repeat_actions = input('Would you want to perform another action? yes or no ').lower()
            with open(user_file, "a") as f:
                f.write('Would you want to perform another action? ' + str(repeat_actions) + "\n")
            if repeat_actions == 'y' or repeat_actions == 'yes':
                continue
            else:
                with open(user_file, "a") as f:
                    f.write("============== End ==============/n")
                sys.exit()

        return 1


def login():
    print("=" * 50)
    print("""Welcome to the ALU Library Management System!!!!""")
    print("=" * 50)
    email_address = input("Enter your email address: ").lower()
    password = input("Enter your password: ")
    email = email_address.split("@")
    if email[1] != 'alustudent.com' and email[1] != 'alueducation.com':
        print("Your email address is not reconnised as a ALU mail")
        print("please use your ALU mail address")
        return 0

    return_value = validate_email(email_address, password)
    if return_value == -1 or return_value == 0:
        print("We could not find your email address in our database")
        print("Cannot connect with your Email address")
        retry()
        print("Thanks for coming")
        sys.exit()
    elif return_value[0] == 1 or return_value[0] == 2 or return_value[0] == 3:
        connect(return_value)
        return 1


def retry():
    answer = input("Do you want to reconnect? yes or no ").lower()
    if answer == 'yes':
        login()


# print(validate_email("d.murair@alustudent.com", "dirac"))
login()
