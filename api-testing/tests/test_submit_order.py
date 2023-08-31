import unittest

from requests_folder.simple_books_requests import SimpleBooksRequests


class TestSubmitOrder(unittest.TestCase):

    access_token = ""

    def setUp(self) -> None:
        self.books_api = SimpleBooksRequests()

        if self.access_token == "":
            self.access_token = self.books_api.generate_token()

    def test_submit_valid_order_status_code(self):
        book_id = 1
        customer_name = "TMTA5"

        response = self.books_api.submit_order(self.access_token, book_id, customer_name)

        expected_status_code = 201
        actual_status_code = response.status_code

        self.assertEqual(expected_status_code, actual_status_code)

        expected_created_value = True
        actual_created_value = response.json()["created"]

        self.assertEqual(expected_created_value, actual_created_value)

    def test_submit_order_with_invalid_book_id(self):
        book_id = 999
        customer_name = "TMTA5"

        response = self.books_api.submit_order(self.access_token, book_id, customer_name)

        expected_status_code = 400
        actual_status_code = response.status_code

        self.assertEqual(expected_status_code, actual_status_code)

        expected_message = "Invalid or missing bookId."
        actual_message = response.json()["error"]

        self.assertEqual(expected_message, actual_message)