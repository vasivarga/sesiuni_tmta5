import unittest

from requests_folder.simple_books_requests import SimpleBooksRequests


class TestUpdateOrder(unittest.TestCase):

    access_token = ""

    def setUp(self) -> None:
        self.books_api = SimpleBooksRequests()

        if self.access_token == "":
            self.access_token = self.books_api.generate_token()

    def test_update_order_status_code(self):
        book_id = 1
        customer_name = "TMTA5_ORDER_INITIAL"

        submit_order_response = self.books_api.submit_order(self.access_token, book_id, customer_name)

        print(self.access_token)

        expected_status_code = 201
        actual_status_code = submit_order_response.status_code

        self.assertEqual(expected_status_code, actual_status_code, "Cannot place order")

        order_id = submit_order_response.json()["orderId"]

        new_customer_name = "TMTA5_ORDER_UPDATE"

        update_order_response = self.books_api.update_order(self.access_token, order_id, new_customer_name)

        expected_status_code = 204
        actual_status_code = update_order_response.status_code
        self.assertEqual(expected_status_code, actual_status_code, "Unexpected status code")

