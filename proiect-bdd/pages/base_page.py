from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from browser import Browser


class BasePage(Browser):

    def find(self, locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        self.find(locator).click()

    def type(self, locator, text):
        self.find(locator).send_keys(text)

    def is_displayed(self, locator):
        return self.find(locator).is_displayed()

    def get_text(self, locator):
        return self.find(locator).text

    def is_url_correct(self, url):
        return self.driver.current_url == url

