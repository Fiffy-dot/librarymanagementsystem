# Author: Fiona Nganga and Dirac Murairi
# This file is for testing our class User

# we import all the files we need
from users_class import *
import unittest
from unittest import mock
import pytest


class TestStudent(unittest.TestCase):
    @mock.patch("users_class.input", create=True)
    def test_init_find_specific_book(self, mocked_input):  # this method tests whether we can find a specific book
        # by the method find_specific_book
        student = User("Fiona", "f.nganga@alustudent.com", "2020")
        mocked_input.side_effect = ["swift"]
        i = student.find_specific_book(books)
        assert i == 0

    @mock.patch("users_class.input", create=True)
    def test_pos_find_specific_book(self, mocked_input):  # this method tests whether we can find a specific book by
        # the method find_specific_book
        student = User("Fiona", "f.nganga@alustudent.com", "2020")
        mocked_input.side_effect = ["PYTHON"]
        i = student.find_specific_book(books)
        assert i == 1

    @mock.patch("users_class.input", create=True)
    def test_pos_search_for_book(self, mocked_input):  # this method tests whether we can find a specific book by
        # the method search_for_book
        student = User("Fiona", "f.nganga@alustudent.com", "2020")
        mocked_input.side_effect = ["PYTHON"]
        i = student.search_for_book(books)
        assert i != 0

    @mock.patch("users_class.input", create=True)
    def test_neg_search_for_book(self, mocked_input):  # this method tests whether we can find a specific book by
        # the method search_for_book
        student = User("Fiona", "f.nganga@alustudent.com", "2020")
        mocked_input.side_effect = ["Z"]
        i = student.search_for_book(books)
        assert i == 0

    @mock.patch("users_class.input", create=True)
    def test_pos_search_by_auth(self, mocked_input):  # this method tests whether we can find a specific book by
        # the method search_by_author
        student = User("Fiona", "f.nganga@alustudent.com", "2020")
        mocked_input.side_effect = ["DIRAC"]
        i = student.search_by_author(books)
        assert i != 0


if __name__ == "__main__":
    unittest.main()
