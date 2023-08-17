import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

"""
########### IMPLICIT WAIT ###########

Aplicatiile web pot avea mai multe elemente dinamice care apar/dispar in functie de anumite actiuni ale utilizatorului, 
sau pot fi cazuri in care timpul de incarcare/randarea site-ului sunt ineficiente, iar elementele nu apar instant. 
Daca driverul incearca sa interactioneze cu astfel de elemente inainte ca acestea sa apara, se va returna o eroare, 
iar testele vor fi marcate ca fiind "picate". 

Funcția implicitly_wait() din Selenium WebDriver specifică un timp maxim de așteptare implicită pentru căutarea unui 
element pe pagină înainte ca WebDriver-ul să arunce o excepție NoSuchElementException.

Pe scurt, WebDriver-ul va aștepta pentru o perioadă specificată înainte de a arunca o excepție în cazul în care 
elementul nu este găsit instant.

ATENTIE: Odata setat, implicitly_wait() se va aplica pe tot parcursul "vietii" driverului sau pana cand acesta va fi 
schimbat cu un alt implicitly_wait() aplicat pe driver.

"""

# declaram un serviciu - va instala browserul in cazul in care nu exista pe PC
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

LINK = "https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver"

driver.get(LINK)

# Functie ajutatoare - ne printeaza ora curenta in formatul ora:minut:secunda
def print_time():
    print(f"Timp curent: {datetime.now().strftime('%H:%M:%S')}")


# ### EXERCITIU 1:
# - Click pe butonul "Change Text to Selenium Webdriver"
# - Dupa 10 secunde textul "site" se va schimba in "Selenium Webdriver"
# - Vom folosi un implicit wait pentru a face driverul sa astepte maxim 11 secunde inainte sa dea eroare

# ## exemplu negativ:
# cu un wait de 5 secunde testul va pica, deoarece elementul devine prezent dupa 10 secunde
# driver.implicitly_wait(5)
# button_change_text = driver.find_element(By.ID, "populate-text")
# button_change_text.click()
# h2_text_selenium_webdriver = driver.find_element(By.XPATH, "//h2[@id='h2' and text()='Selenium Webdriver']")


driver.implicitly_wait(5)
print_time()

alert_button = driver.find_element(By.ID, "alert")
print_time()

print("S-a gasit elementul si s-a trecut la urmatoarea instructiune")
driver.implicitly_wait(0)
print_time()

time.sleep(3)
print_time()
# stop_button = driver.find_element(By.ID, "stop")

driver.implicitly_wait(11)
driver.find_element(By.ID, "populate-text").click()
driver.find_element(By.XPATH, "//h2[text()='Selenium Webdriver']")
print_time()
driver.implicitly_wait(0)


"""
########### EXPLICIT WAITS ###########

Wait-urile explicite sunt putin diferite de implicit_wait(), deoarece ele se aplica o singura data (in momentul in care
 sunt apelate ca functie) existand mai multe conditii dupa care putem astepta sa fie indeplinite.

Exemple de conditii: 
- prezenta elementului
- vizibilitatea elementului
- elementul sa contina un text
- atributul unui element sa existe
- atributul unui element sa contina o anumita valoare
- etc...

Structura unui explicit wait:

    wait = WebdriverWait(driver, x)
    wait.until(expected_condition)

unde:

    * WebdriverWait - este clasa care face driverul sa astepte
    * x - este cantitatea maxima de timp pana la indeplinirea conditiei (si inaintea returnarii unei erori)
    * expected_condition - conditia dupa care asteptam sa se indeplineasca
"""

# Declaram WebElement pentru butonul care va afisa un alt buton dupa 10 secunde
button_display_other_button = driver.find_element(By.ID, "display-other-button")

# Click pe buton
button_display_other_button.click()

# Declaram un WebdriverWait de 10 secunde - aici doar definim wait-ul, asteptarea inca nu incepe

# DEFINIM LOCATORUL SUB FORMA DE TUPLU
locator_buton_ascuns = (By.ID, "hidden")

# Deoarece butonul este prezent in DOM, dar este invizibil, va trebui sa asteptam pana cand acesta devine vizibil
wait_1 = WebDriverWait(driver, 11)
wait_1.until(EC.presence_of_element_located(locator_buton_ascuns))
print_time()


print("Incepem asteptarea")
print_time()

# aici incepem sa asteptam dupa butonul care trebuie sa devina vizibil
wait_2 = WebDriverWait(driver, 11)
wait_2.until(EC.visibility_of_element_located(locator_buton_ascuns))
print_time()

print("Elementul a devenit vizibil")
print_time()

driver.find_element(By.ID, "hidden").click()
