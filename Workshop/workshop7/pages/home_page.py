import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):

    URL = 'https://automationexercise.com'
    CAROUSEL = (By.ID,'slider-carousel')

    def open_website(self):
        self.driver.maximize_window()

    def navigate_to_website(self):
        self.driver.get(self.URL)


    def check_home_page(self, expected_url):
        assert self.is_url_correct(expected_url)

    def loaded_home_page(self):
        expected_url = 'https://automationexercise.com/'
        actual_url = self.driver.current_url
        assert expected_url == actual_url, f"Error: expected {expected_url}, received {actual_url}"

    def carousel_is_visible(self):
       assert self.is_displayed(self.CAROUSEL), "Error element is not visible"