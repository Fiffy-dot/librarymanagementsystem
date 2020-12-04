# Author: Fiona Nganga and Dirac Murairi
# this is a file for the users
# class supervisor
from supervisors import *
import unittest
from unittest import mock
import pytest


class TestStudent(unittest.TestCase):
    @mock.patch("supervisors.input", create=True)
    # we are testing the adding book function
    def test_init_add_book(self, mocked_input):
        student = Supervisor("Fiona", "f.nganga@alustudent.com", "2020")
        mocked_input.side_effect = ["swift", "DIRAC"]
        i = student.add_book(books)
        assert i == 1

    @mock.patch("supervisors.input", create=True)
    # we are testing the successful removal of a book by the function remove_book
    def test_pos_remove_book(self, mocked_input):
        student = Supervisor("Fiona", "f.nganga@alustudent.com", "2020")
        mocked_input.side_effect = ["PYTHON", "1"]
        i = student.remove_book(books)
        assert i == 1

    @mock.patch("supervisors.input", create=True)
    def test_neg_remove_book(self, mocked_input):
        # we are testing the unsuccessful removal of a book by the function remove_book
        student = Supervisor("Fiona", "f.nganga@alustudent.com", "2020")
        mocked_input.side_effect = ["SCRACTH", "2"]
        i = student.remove_book(books)
        assert i == 0

    @mock.patch("supervisors.input", create=True)
    def test_pos_remove_user(self, mocked_input):
        # we are testing the successful removal of a user by the function remove_user
        student = Supervisor("Fiona", "f.nganga@alustudent.com", "2020")
        mocked_input.side_effect = ["DIRAC", "d.murairi@alustudent.com"]
        i = student.remove_user(users)
        assert i == 1

    @mock.patch("supervisors.input", create=True)
    def test_neg_remove_user(self, mocked_input):
        # we are testing the unsuccessful removal of a user by the function remove_user

        student = Supervisor("Fiona", "f.nganga@alustudent.com", "2020")
        mocked_input.side_effect = ["FIONA", "d.murairi@alustudent.com"]
        i = student.remove_user(users)
        assert i == 0


if __name__ == "__main__":
    unittest.main()
