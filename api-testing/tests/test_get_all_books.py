import unittest

from requests_folder.simple_books_requests import SimpleBooksRequests


class TestGetAllBooks(unittest.TestCase):

    def setUp(self) -> None:
        self.books_api = SimpleBooksRequests()

    def test_get_all_books_status_code_without_filter(self):
        response = self.books_api.get_all_books()

        expected_response_code = 200
        actual_response_code = response.status_code

        assert expected_response_code == actual_response_code, "Error, unexpected status code"

    def test_get_all_books_number_of_results_without_filter(self):
        response = self.books_api.get_all_books()

        expected_number_of_results = 6
        actual_number_of_result = len(response.json())

        self.assertEqual(expected_number_of_results, actual_number_of_result, "Expected number of results is not 6")

        # in cazul in care nu stim neaparat cate raspunsuri vin, dar stim ca trebuie sa fie macar unul
        # self.assertTrue(actual_number_of_result > 1)

    def test_get_all_books_filter_by_valid_limit(self):
        response = self.books_api.get_all_books(limit=3)

        expected_number_of_results = 3
        actual_number_of_result = len(response.json())

        self.assertEqual(expected_number_of_results, actual_number_of_result, "Expected number of results is not 3")

    def test_get_all_books_filter_by_invalid_limit_greater_than_20(self):
        response = self.books_api.get_all_books(limit=21)

        expected_status_code = 400
        actual_status_code = response.status_code

        self.assertEqual(expected_status_code, actual_status_code, "Unexpected status code")

        expected_error_message = "Invalid value for query parameter 'limit'. Cannot be greater than 20."
        actual_error_message = response.json()["error"]

        self.assertEqual(expected_error_message, actual_error_message, "Unexpected error message")

    def test_get_all_books_filter_by_invalid_limit_less_than_0(self):
        response = self.books_api.get_all_books(limit=-1)

        expected_status_code = 400
        actual_status_code = response.status_code

        self.assertEqual(expected_status_code, actual_status_code, "Unexpected status code")

        expected_error_message = "Invalid value for query parameter 'limit'. Must be greater than 0."
        actual_error_message = response.json()["error"]

        self.assertEqual(expected_error_message, actual_error_message, "Unexpected error message")

    def test_get_all_books_filter_by_type_fiction(self):
        self.verify_book_by_type("fiction")

    def test_get_all_books_filter_by_type_non_fiction(self):
        self.verify_book_by_type("non-fiction")

    def verify_book_by_type(self, book_type):
        response = self.books_api.get_all_books(book_type=book_type)

        expected_status_code = 200
        actual_status_code = response.status_code
        self.assertEqual(expected_status_code, actual_status_code, "Unexpected status code")

        expected_type = book_type

        list_of_books = response.json()

        for i in range(0, len(list_of_books)):
            current_book = list_of_books[i]
            # print(current_book)
            # print(type(current_book))
            # print("-------------------")
            actual_type = current_book["type"]
            self.assertEqual(expected_type, actual_type, f"Unexpected type for book {current_book['name']}")
