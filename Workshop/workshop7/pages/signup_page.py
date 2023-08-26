import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SignUp(BasePage):

    URL = 'https://automationexercise.com/login'
    name_locator = (By.XPATH, '//form[@action="/signup"]/input[@placeholder="Name"]')
    email_locator = (By.XPATH, '//form[@action="/signup"]/input[@placeholder="Email Address"]')
    sign_up_button = (By.XPATH, '//form[@action="/signup"]/button[@type="submit"]')


    def sign_up_page(self):
        self.driver.maximize_window()
        self.driver.get(self.URL)

    def fill_in_name(self,name):                   #cu aceasta metoda ii spunem daca parametrul primit este
        if name != "N/A":                          #"N/A" atunci campul ramane gol
            self.type(self.name_locator, name)     # daca este diferit de "N/A" atunci populam campul cu valoarea primita

    def fill_in_email(self,email):                 #la fel ca la nume
        if email != "N/A":
            self.type(self.email_locator, email)

    def click_button(self):
        self.click(self.sign_up_button)

    def acceptable_error(self):                                   # in aceasta metoda verificam daca se schiba URLul sau nu
        url = 'https://automationexercise.com/signup'             # adica daca crearea contului a fost cu success sau nu
        actual_url = self.driver.current_url
        if url == actual_url:
            return 'Success'
        else:
            return 'Login Not Successful'

    def check_error_message(self, error_message):
        empty_field_error = "signup not allowed with empty fields"       #prin aceasta metoda in functie de URL                                                                    #construim
        invalid_email = "incorrect_email_format"                         #construim mesajele de eroare/ success
        if self.acceptable_error() == "Login Not Successful":
            try:
                assert empty_field_error == error_message
            except:
                assert invalid_email == error_message
        else:
            assert self.acceptable_error() == error_message
