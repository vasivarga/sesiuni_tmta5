import random

import requests

class SimpleBooksRequests:

    _BASE_URL = "https://simple-books-api.glitch.me"
    _API_STATUS_ENDPOINT = "/status"
    _GET_ALL_BOOKS_ENDPOINT = "/books"
    _API_AUTH_ENDPOINT = "/api-clients/"
    _SUBMIT_ORDER_ENDPOINT = "/orders"
    _access_token = ""

    def get_api_status(self):
        api_status_url = self._BASE_URL + self._API_STATUS_ENDPOINT

        response = requests.get(api_status_url)

        return response

    def get_all_books(self, book_type="", limit=""):
        get_all_books_url = self._BASE_URL + self._GET_ALL_BOOKS_ENDPOINT
        # https://simple-books-api.glitch.me/books

        if book_type != "" and limit == "":
            get_all_books_url += f"?type={book_type}"

        elif book_type == "" and limit != "":
            get_all_books_url += f"?limit={limit}"

        elif book_type != "" and limit != "":
            get_all_books_url += f"?type={book_type}&limit={limit}"

        response = requests.get(get_all_books_url)

        return response

    def generate_token(self):
        auth_url = self._BASE_URL + self._API_AUTH_ENDPOINT

        random_number = random.randint(1, 9999999999999999999999999)

        email_address = f"testautomation{random_number}@itfactory.ro"

        request_body = {
            "clientName": "TMTA5",
            "clientEmail": email_address
        }

        response = requests.post(auth_url, json=request_body)

        token = response.json()["accessToken"]

        return token

    def submit_order(self, access_token, book_id, customer_name):
        submit_order_url = self._BASE_URL + self._SUBMIT_ORDER_ENDPOINT

        header_parameters = {
            "Authorization": "Bearer " + access_token
        }

        request_body = {
            "bookId": book_id,
            "customerName": customer_name
        }

        response = requests.post(submit_order_url, json=request_body, headers=header_parameters)

        return response

    def update_order(self, access_token, order_id, new_customer_name):
        update_order_url = self._BASE_URL + self._SUBMIT_ORDER_ENDPOINT + f"/{order_id}"

        header_parameters = {
            "Authorization": "Bearer " + access_token
        }

        request_body = {
            "customerName": new_customer_name
        }

        response = requests.patch(update_order_url, json=request_body, headers=header_parameters)

        return response

    def delete_order(self, access_token, order_id):
        delete_order_url = self._BASE_URL + self._SUBMIT_ORDER_ENDPOINT + f"/{order_id}"

        header_parameters = {
            "Authorization": "Bearer " + access_token
        }

        response = requests.delete(delete_order_url, headers=header_parameters)

        return response


# books_api = SimpleBooksRequests()
# books_api.generate_token()
# books_api.generate_token()
# books_api.generate_token()
# books_api.generate_token()
# books_api.generate_token()
# books_api.generate_token()