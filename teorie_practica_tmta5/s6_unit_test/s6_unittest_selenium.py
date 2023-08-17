import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

"""
########### Libraria unittest ###########

Libraria unittest ofera suport pentru crearea de teste rulabile direct in interiorul clasei.
Se implementeaza prin mostenirea clasei TestCase din libraria unittest
Orice clasa de teste trebuie sa mosteneasca clasa TestCase si sa aiba urmatoarele particularitati:
1. metoda setUp() -> toate activitatile care trebuie sa fie executate inainte de ORICE TEST din clasa respectiva
2. metoda teardown() -> toate activitatile care trebuie sa fie executate dupa de ORICE TEST din clasa respectiva
3. toate metodele de test trebuie sa aiba prefixul test_

* = despachetare tuplu
driver.find_elements(*BUTTON_JS_ALERT_SIMPLE) <=> driver.find_elements(By.CSS_SELECTOR, "[onclick='jsAlert()']")
"""


class Test(unittest.TestCase):
    driver = None
    LOGIN_LINK = "https://the-internet.herokuapp.com/login"
    BUTTON_LOGIN = (By.CSS_SELECTOR, "button[type='submit']")
    INPUT_USERNAME = (By.ID, "username")
    INPUT_PASSWORD = (By.ID, "password")
    ERROR_MESSAGE = (By.ID, "flash")


    # suprascriem metoda setUp care va rula inainte de fiecare test
    def setUp(self) -> None:
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get(self.LOGIN_LINK)

    # suprascriem metoda tearDown care va rula dupa fiecare test
    def tearDown(self) -> None:
        self.driver.quit()

    # TEST 1
    # - Verifica daca URL-ul paginii este corect
    def test_url(self):
        actual_url = self.driver.current_url
        print(actual_url)
        # assert self.LOGIN_LINK == actual_url, f"Unexpected URL. Expected: {self.LOGIN_LINK} \n Actual: {actual_url}"

        # Varianta unittest pentru assert de egalitate
        self.assertEqual(self.LOGIN_LINK, actual_url, "Unexpected URL")

    # TEST 2
    # - Verifica daca titlul paginii apare corect
    def test_title(self):
        expected_title = "The Internet"
        actual_title = self.driver.title

        self.assertEqual(expected_title, actual_title)

    # TEST 3
    # - Verifica daca textul de pe elementul xpath=//h2 e corect
    def test_login_page_text(self):
        expected = "Login Page"
        actual = self.driver.find_element(By.XPATH, "//h2").text
        # assert expected_text == text_h2, f"Invalid h2 text, expected {expected_text}, but found {text_h2}"
        # Observam ca folosind assertEqual, nu mai trebuie scrisa partea cu 'expected x but
        # found y' deoarece se specifica implicit prin aceasta metoda
        self.assertEqual(expected, actual, "Textul de pe h2 este incorect")

    # TEST 4
    # - Verifica daca butonul de login este displayed
    def test_buton_login_display(self):
        login_button = self.driver.find_element(*self.BUTTON_LOGIN)

        # assert login_button.is_displayed(), "Butonul de login nu este afisat"
        self.assertTrue(login_button.is_displayed(), "Butonul de login nu este afisat")

    # TEST 5
    # - Verifică dacă atributul href al linkului ‘Elemental Selenium’ e corect
    def test_atribut_href(self):
        expected = "http://elementalselenium.com/"
        actual = self.driver.find_element(By.XPATH, "//a[text()='Elemental Selenium']").get_attribute("href")

        # Cand incercam sa luam un atribut inexistent:
        # atribut = self.driver.find_element(By.XPATH, "//a[text()='Elemental Selenium']").get_attribute("type")
        # print("Atributul este: " + atribut)

        self.assertEqual(expected, actual, "Atributul 'href' este incorect")

    # TEST 6
    # - Lasă goale user și pass;
    # - Click login;
    # - Verifică dacă eroarea e displayed
    def test_empty_user_pass_login(self):
        # Facem click pe butonul de login fara sa completam vreun camp
        self.driver.find_element(*self.BUTTON_LOGIN).click()
        eroare = self.driver.find_element(*self.ERROR_MESSAGE)

        self.assertTrue(eroare.is_displayed(), "Eroarea nu este afisata")

    # TEST 7
    # - Completează cu user și pass invalide;
    # - Click login;
    # - Verifică dacă mesajul de pe eroare e corect;
    # - Este și un x pus acolo extra așa că vom folosi soluția de mai jos:
    #   expected = 'Your username is invalid!'
    #   self.assertTrue(expected in actual, 'Error message text is incorrect')
    def test_invalid_login(self):
        self.driver.find_element(*self.INPUT_USERNAME).send_keys("test")
        self.driver.find_element(*self.INPUT_PASSWORD).send_keys("test")
        self.driver.find_element(*self.BUTTON_LOGIN).click()

        actual = self.driver.find_element(*self.ERROR_MESSAGE).text
        print(actual)

        expected = 'Your username is invalid!'

        # self.assertIn(expected, actual, 'Error message text is incorrect')

        # Assert pentru a verifica daca o expresie este adevarata
        # Metoda assertTrue() primeste 2 parametri:
        #   * primul param - expresia de evaluat
        #   * al doilea param - (optional) mesajul de eroare afisat
        self.assertTrue(expected in actual, 'Error message text is incorrect')