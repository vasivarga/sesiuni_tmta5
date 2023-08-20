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


class Login(unittest.TestCase):
    driver = None
    LOGIN_LINK = "https://the-internet.herokuapp.com/login"
    BUTTON_LOGIN = (By.CSS_SELECTOR, "button[type='submit']")
    INPUT_USERNAME = (By.ID, "username")
    INPUT_PASSWORD = (By.ID, "password")
    ERROR_MESSAGE = (By.ID, "flash")
    CLOSE_BUTTON = (By.CLASS_NAME, "close")
    SUCCCESS_RIBBON = (By.XPATH, '//div[@class="flash success"]')

    # suprascriem metoda setUp care va rula inainte de fiecare test
    def setUp(self) -> None:
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get(self.LOGIN_LINK)
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)

    # suprascriem metoda tearDown care va rula dupa fiecare test
    def tearDown(self) -> None:
        self.driver.quit()

    # # TEST 1
    # # - Verifica daca URL-ul paginii este corect
    # def test_url(self):
    #     actual_url = self.driver.current_url
    #     print(actual_url)
    #     # assert self.LOGIN_LINK == actual_url, f"Unexpected URL. Expected: {self.LOGIN_LINK} \n Actual: {actual_url}"
    #
    #     # Varianta unittest pentru assert de egalitate
    #     self.assertEqual(self.LOGIN_LINK, actual_url, "Unexpected URL")
    #
    # # TEST 2
    # # - Verifica daca titlul paginii apare corect
    # def test_title(self):
    #     expected_title = "The Internet"
    #     actual_title = self.driver.title
    #
    #     self.assertEqual(expected_title, actual_title)
    #
    # # TEST 3
    # # - Verifica daca textul de pe elementul xpath=//h2 e corect
    # def test_login_page_text(self):
    #     expected = "Login Page"
    #     actual = self.driver.find_element(By.XPATH, "//h2").text
    #     # assert expected_text == text_h2, f"Invalid h2 text, expected {expected_text}, but found {text_h2}"
    #     # Observam ca folosind assertEqual, nu mai trebuie scrisa partea cu 'expected x but
    #     # found y' deoarece se specifica implicit prin aceasta metoda
    #     self.assertEqual(expected, actual, "Textul de pe h2 este incorect")
    #
    # # TEST 4
    # # - Verifica daca butonul de login este displayed
    # def test_buton_login_display(self):
    #     login_button = self.driver.find_element(*self.BUTTON_LOGIN)
    #
    #     # assert login_button.is_displayed(), "Butonul de login nu este afisat"
    #     self.assertTrue(login_button.is_displayed(), "Butonul de login nu este afisat")
    #
    # # TEST 5
    # # - Verifică dacă atributul href al linkului ‘Elemental Selenium’ e corect
    # def test_atribut_href(self):
    #     expected = "http://elementalselenium.com/"
    #     actual = self.driver.find_element(By.XPATH, "//a[text()='Elemental Selenium']").get_attribute("href")
    #
    #     # Cand incercam sa luam un atribut inexistent:
    #     # atribut = self.driver.find_element(By.XPATH, "//a[text()='Elemental Selenium']").get_attribute("type")
    #     # print("Atributul este: " + atribut)
    #
    #     self.assertEqual(expected, actual, "Atributul 'href' este incorect")
    #
    # # TEST 6
    # # - Lasă goale user și pass;
    # # - Click login;
    # # - Verifică dacă eroarea e displayed
    # def test_empty_user_pass_login(self):
    #     # Facem click pe butonul de login fara sa completam vreun camp
    #     self.driver.find_element(*self.BUTTON_LOGIN).click()
    #     eroare = self.driver.find_element(*self.ERROR_MESSAGE)
    #
    #     self.assertTrue(eroare.is_displayed(), "Eroarea nu este afisata")

    # TEST 7
    # - Completează cu user și pass invalide;
    # - Click login;
    # - Verifică dacă mesajul de pe eroare e corect;
    # - Este și un x pus acolo extra așa că vom folosi soluția de mai jos:
    #   expected = 'Your username is invalid!'
    #   self.assertTrue(expected in actual, 'Error message text is incorrect')
    # def test_invalid_login(self):
    #     time.sleep(3)
    #     self.driver.find_element(*self.INPUT_USERNAME).send_keys("test")
    #     self.driver.find_element(*self.INPUT_PASSWORD).send_keys("test")
    #     time.sleep(3)
    #     self.driver.find_element(*self.BUTTON_LOGIN).click()
    #     time.sleep(3)
    #
    #     actual = self.driver.find_element(*self.ERROR_MESSAGE).text
    #     print(actual)
    #
    #     expected = 'Your username is invalid!'
    #
    #     # self.assertIn(expected, actual, 'Error message text is incorrect')
    #
    #     # Assert pentru a verifica daca o expresie este adevarata
    #     # Metoda assertTrue() primeste 2 parametri:
    #     #   * primul param - expresia de evaluat
    #     #   * al doilea param - (optional) mesajul de eroare afisat
    #     self.assertTrue(expected in actual, 'Error message text is incorrect')
    #     elemnt_locator = self.driver.find_element(*self.ERROR_MESSAGE)

       # wait = WebDriverWait(self.driver,3).until(EC.presence_of_element_located(elemnt_locator))

    # metoda ajutatoare - ea nu va fi rulata ca test pentru ca nu are prefixul test_
    # metoda are 2 parametri:
    # 1 - element_locator: locatorul elementului dupa care asteptam sa apara
    # 2 - seconds_to_wait: numarul maxim de secunde de asteptare pentru ca elementul sa apara
    def wait_for_element_to_be_present(self,element_locator,seconds_to_wait):
        wait = WebDriverWait(self.driver,seconds_to_wait)
        return wait.until(EC.presence_of_element_located(element_locator))

    # metoda ajutatoare - asteapta ca un element sa devina ABSEENT in HTML (absent != invizibil)
    # metoda are 2 parametri:
    # 1 - element_locator: locatorul elementului dupa care asteptam sa dispara
    # 2 - seconds_to_wait: numarul maxim de secunde de asteptare pentru ca elementul sa dispare
    # Observate: cu EC.none_of() se neaga conditia din EC (EC = expected_condition)

    def wait_for_element_to_not_be_present(self,element_locator, seconds_to_wait):
        wait = WebDriverWait(self.driver, seconds_to_wait)
        return wait.until(EC.none_of(EC.presence_of_element_located(element_locator)))


    # metoda ajutatoare - returneaza TRUE daca elementul este PREZENT (prezent nu inseamna ca e si vizibil neaparat)
    # - metoda are ca parametru variabila element_locator: locatorul elementului dupa care asteptam sa dispara
    # - folosind driver.find_elements() putem sa ne dam seama daca un element este sau nu prezent
    # - driver.find_elements() nu da eroare daca nu gaseste un element dupa un locator dat, ci returneaza o lista goala
    # - daca lista e goala, inseamna ca nu e elementul prezent [len(lista) = 0 deci return FALSE]
    # - daca lista nu e goala, inseamna ca avem cel putin un element gasit [len(lista) > 0 deci return TRUE]

    #exemplu element product_tile = driver.find_elements(By.XPATH, '//a[@class="product-title"]')
    def is_element_present(self, product_tile):
        # lista = self.driver.find_elements(product_tile)
        #return len(lista) > 0
        return len(self.driver.find_elements(*product_tile)) > 0

    # def test_login_button_is_present(self):
    #     assert self.is_element_present(self.BUTTON_LOGIN)

    # TEST 8
    # - Lasă goale user și pass;
    # - Click login;
    # - Apasă x la eroare;
    # - Verifică dacă eroarea a dispărut
    def test_error_message_disappears(self):
        time.sleep(3)
        self.driver.find_element(*self.BUTTON_LOGIN).click()
        time.sleep(3)
        self.driver.find_element(*self.CLOSE_BUTTON).click()
        assert self.wait_for_element_to_not_be_present(self.CLOSE_BUTTON,3), "Mesajul nu a disparut la inchidere"


# TEST 9 - Ia ca o listă toate //label;
# - Verifică textul ca textul de pe ele să fie cel așteptat (Username și Password)
# - Aici e ok să avem 2 asserturi

    def test_texul_este_prezent(self):
        lista_texte = self.driver.find_elements(By.XPATH,'//label')
        #expect = "User"
        expected_text_1 = "Username"  #// "nameUser"
        actual_text_1 = lista_texte[0].text
        expected_text_2 = "Password"
        actual_text_2 = lista_texte[1].text
        self.assertEqual(expected_text_1,actual_text_1,"Textul nu este cel asteptat pe primul element")
        # assert expected_text_1 == actual_text_1
        # assert expect in actual_text_1, "mesaj"
        self.assertEqual(expected_text_2,actual_text_2,"Textul nu este cel asteptat pe al doilea element")

    # TEST 10
    # - Completează cu user și pass valide;
    # - Click login;
    # - Verifică ca noul url CONTINE stringul /secure;
    # - Folosește un explicit wait pentru elementul cu clasa ’flash succes’
    # - Verifică dacă elementul cu clasa=’flash succes’ este displayed;
    # - Verifică dacă mesajul de pe acest element CONȚINE textul ‘secure area!’

    def test_login_secure(self):
        time.sleep(2)
        self.driver.find_element(*self.INPUT_USERNAME).send_keys("tomsmith")
        self.driver.find_element(*self.INPUT_PASSWORD).send_keys("SuperSecretPassword!")
        time.sleep(2)
        self.driver.find_element(*self.BUTTON_LOGIN).click()

        expected_url_extension = "/secure"
        actual_url = self.driver.current_url
        self.assertIn(expected_url_extension,actual_url,"Noul URL nu contine extensia asteptata")

        assert self.wait_for_element_to_be_present(self.SUCCCESS_RIBBON,3).is_displayed(), "Success ribbon not present"

        element_success = WebDriverWait(self.driver,3).until(EC.presence_of_element_located(self.SUCCCESS_RIBBON))
        self.assertTrue(element_success.is_displayed(),"Elementul nu a fost afisat")

        expected_message = "secure area!"
        actual_message = self.driver.find_element(*self.SUCCCESS_RIBBON).text
        self.assertIn(expected_message,actual_message,"Mesajul asteptat nu este inclus in alerta")





'''
    def wait_for_element_to_be_present(self,element_locator,seconds_to_wait):
        wait = WebDriverWait(self.driver,seconds_to_wait)
        return wait.until(EC.presence_of_element_located(element_locator))
'''






class DemoMultipleClassesTestSuite(unittest.TestCase):
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