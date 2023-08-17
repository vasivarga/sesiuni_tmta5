import time
from unittest import TestCase

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager


class TestAlerts(TestCase):
    driver = None
    LINK = "https://the-internet.herokuapp.com/javascript_alerts"

    BUTTON_JS_ALERT_SIMPLE = (By.CSS_SELECTOR, "[onclick='jsAlert()']")  # XPATH: //button[@onclick='jsAlert()']
    BUTTON_JS_ALERT_CONFIRM = (By.CSS_SELECTOR, "[onclick='jsConfirm()']")  # XPATH: //button[@onclick='jsConfirm()']
    BUTTON_JS_ALERT_PROMPT = (By.XPATH, "//button[contains(text(),'JS Prompt')]")

    PARAGRAPH_TEXT = (By.ID, "result")

    # suprascriem metoda setUp care va rula inainte de fiecare test
    def setUp(self):
        # Metoda de a crea un driver de firefox
        service = Service(GeckoDriverManager().install())
        self.driver = webdriver.Firefox(service=service)
        self.driver.get(self.LINK)

    # suprascriem metoda tearDown care va rula dupa fiecare test
    def tearDown(self):
        self.driver.quit()

    # Metoda ajutatoare (nu se ruleaza ca test) -> ne ajuta sa nu mai scriem self.driver.find_element(*locator).click()
    # la fiecare click, ci mai sumplu self.click(self.NUME_LOCATOR)
    def click(self, locator):
        self.driver.find_element(*locator).click()

    def test_accept_simple_alert(self):
        self.click(self.BUTTON_JS_ALERT_SIMPLE)

        # declaram variabila pentru alerta, ca sa putem interactiona cu ea
        alert = self.driver.switch_to.alert

        # apasam butonul care accepta alerta
        alert.accept()

        expected_text = "You successfully clicked an alert"
        actual_text = self.driver.find_element(*self.PARAGRAPH_TEXT).text

        # assert expected_text == actual_text, f"Error, texts are not matching"

        self.assertEquals(expected_text, actual_text, "Error, texts are not matching.")

    def test_accept_confirm_alert(self):
        self.click(self.BUTTON_JS_ALERT_CONFIRM)

        # declaram variabila pentru alerta, ca sa putem interactiona cu ea
        alert = self.driver.switch_to.alert

        # apasam butonul care accepta alerta
        alert.accept()

        expected_text = "You clicked: Ok"

        actual_text = self.driver.find_element(*self.PARAGRAPH_TEXT).text

        self.assertEquals(expected_text, actual_text, "Error, texts are not matching.")

    def test_cancel_confirm_alert(self):
        self.click(self.BUTTON_JS_ALERT_CONFIRM)

        # declaram variabila pentru alerta, ca sa putem interactiona cu ea
        alert = self.driver.switch_to.alert

        # apasam butonul care respinge alerta
        alert.dismiss()

        expected_text = "You clicked: Cancel"

        actual_text = self.driver.find_element(*self.PARAGRAPH_TEXT).text

        self.assertEquals(expected_text, actual_text, "Error, texts are not matching.")

    def test_accept_prompt_alert(self):
        # self.driver.find_element(*self.BUTTON_JS_ALERT_PROMPT).click()
        self.click(self.BUTTON_JS_ALERT_PROMPT)

        alert = self.driver.switch_to.alert
        inserted_text = "Test Alert"
        alert.send_keys(inserted_text)

        alert.accept()

        expected_result = "You entered: " + inserted_text
        actual_result = self.driver.find_element(*self.PARAGRAPH_TEXT).text

        # assert expected_result == actual_result, "Error, texts are not matching"
        self.assertEqual(expected_result, actual_result, "Error, texts are not matching")

    def test_cancel_prompt_alert(self):
        # self.driver.find_element(*self.BUTTON_JS_ALERT_PROMPT).click()
        self.click(self.BUTTON_JS_ALERT_PROMPT)

        alert = self.driver.switch_to.alert
        alert.dismiss()

        expected_result = "You entered: null"
        actual_result = self.driver.find_element(*self.PARAGRAPH_TEXT).text

        # assert expected_result == actual_result, "Error, texts are not matching"
        self.assertEqual(expected_result, actual_result, "Error, texts are not matching")
