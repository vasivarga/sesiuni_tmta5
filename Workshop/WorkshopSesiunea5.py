from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


service_chrome = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=service_chrome)

#firefox = webdriver.Firefox()
#chrome = webdriver.Chrome()
chrome.maximize_window()
#chrome.get("https://sport.ro")
#time.sleep(3)

# chrome.get("https://formy-project.herokuapp.com/form")
# #time.sleep(3)
# #chrome.find_element(By.ID,"first-name")
# #Cautare dupa id -> intodeauna precedat de "#" cand vorbim de CSS_SELECTOR
# chrome.find_element(By.CSS_SELECTOR,"#first-name").send_keys("Anton")
# #time.sleep(3)
# #Cautare dupa atribut=valoare
# chrome.find_element(By.CSS_SELECTOR,"input[placeholder='Enter last name']").send_keys("Pann")
# time.sleep(3)
# #Cautare dupa clasa -> intodeanua precedat de "." cand vorbim de CSS_SELECTOR
# chrome.find_elements(By.CSS_SELECTOR,".form-control")[2].send_keys("Tester")
# #time.sleep(3)
# #am facut navigare din parinte in copil combinata cu cautare de tip atribut=valoare (care din nou observati ca au fost puse intre ghilimele)
# #plecam dintr-un element de tip strong:
# #                                > coboram la un copil
# #                                   copilul este de tip label si are atribut "for"  si valoare "last-name"
# text_label_last_name = chrome.find_element(By.CSS_SELECTOR,"strong > label[for='last-name']").text
# print(text_label_last_name)
#
# # am facut cautare dupa al doilea copil de tip div al unui div cu clasa input-group
# # plecam de la un element de tip div   care are o clasa de tip input-grup
# #                              cu nth-of-type cerem al n'lea copil (cazul de fata "2") al 2-lea copil
# #                              care este tot de tipul div  si input
# chrome.find_element(By.CSS_SELECTOR,"div.input-group>div:nth-of-type(2) input").click()
#
# # am facut cautare dupa ultimul copil de tip div al unui div cu clasa input-group
# chrome.find_element(By.CSS_SELECTOR,"div.input-group>div:last-of-type input").click()
#
# # am facut cautare dupa primul copil de tip div al unui div cu clasa input-group
# education_label = chrome.find_element(By.CSS_SELECTOR,"div.input-group>div:first-of-type label").text
# print(education_label)
#
# chrome.find_element(By.CSS_SELECTOR,"input[placeholder='Enter last name']").clear()  #stergem textul dintr-o celula introdus de noi
# # am facut cautare dupa un element de tip input care are ca si frate un element
# # #de tip strong (putem cauta doar dupa fratele ulterior, nu si dupa fratele anterior)
# #Pleacam de la un element de tip div care are clasa "form-grup"
# # la al n'lea copil (cazul nostru al 2-lea) de tip strong
# #  cu + mergem la fratele lui strong care este de tip input
# chrome.find_element(By.CSS_SELECTOR,"div.form-group > div:nth-of-type(2) > strong + input").send_keys("following sibling")
#
#
# chrome.find_element(By.CSS_SELECTOR,"#first-name").clear()
# chrome.find_element(By.XPATH, "//strong/following-sibling::input[@placeholder='Enter first name']").send_keys("la fel ca CSS")
# time.sleep(5)
#
# chrome.get("https://carturesti.ro/")
# #cautare dupa textul unui element
# # sintaxa:          "element"[contains(text(),"textul")]
# #in cazul nostru         span[contains(text(),"Login")]
# chrome.find_element(By.XPATH,'//hr[@role="separator"]/preceding-sibling::md-menu-item//span[contains(text(),"Login")]')


# chrome.get("https://www.ebay.com/")
# time.sleep(3)
# # pentru a interactiona cu dropdownuri ne folosim de clasa "Select" care trebuie importata
# # instantiem un obiect din clasa select si il identificam
# categorii = Select(chrome.find_element(By.ID,"gh-cat"))
# # intercationam cu acesta in baza metodelor disponibile
# categorii.select_by_visible_text("Consumer Electronics")
# chrome.find_element(By.LINK_TEXT,"Watchlist").click()
# time.sleep(5)

#find elements returneaza o lista de elemente care au proprietatile cerute/ sunt de tipul cerut
#daca nu identifica elemente dupa criteriile cerute va returna o lista goala
# chrome.get("https://formy-project.herokuapp.com/form")
# time.sleep(2)
# list_input = chrome.find_elements(By.XPATH,'//input[@type="text"]')
# first_three_fields = list_input[0:3]
# print(first_three_fields)
# for i in range(0, len(first_three_fields)):
#     list_input[i].send_keys("Input de la user")
#     time.sleep(2)


# Test 2: cautati un produs la alegere (iphone 14) si verificati ca s-au returnat cel putin 10 rezultate
# ([class="product-title"])
chrome.get("https://www.elefant.ro/")
time.sleep(2)
chrome.find_element(By.ID,"CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll").click()
time.sleep(2)
chrome.find_element(By.XPATH,'//input[@name="SearchTerm"][1]').send_keys("Iphone 14")
time.sleep(2)
chrome.find_element(By.XPATH,'//button[@name="search"][1]').click()
time.sleep(2)
#element = "(By.XPATH, '//a[@class="product-title"]')"
def is_element_present():
    # lista = self.driver.find_elements(product_title)
    # return len(lista) > 0
    return len(chrome.find_elements(*(By.XPATH, '//a[@class="product-title"]'))) == 16

assert is_element_present() == True, "Nu sunt 16 elemente"


# - Test 5: Intrati pe site, accesati butonul cont si click pe conectare.
# Identificati elementele de tip user si parola si inserati valori incorecte (valori incorecte inseamna oricare valori care nu sunt recunoscute drept cont valid)
# - Dati click pe butonul "conectare" si verificati urmatoarele:
#              1. Faptul ca nu s-a facut logarea in cont
#             2. Faptul ca se returneaza eroarea corecta

# intra pe elefant.ro
chrome.get("https://www.elefant.ro/")
time.sleep(2)
# gasirea cookie popup window-ului si acceptarea lor
chrome.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll").click()

# apasa pe butonul de conectare
# chrome.find_element(By.XPATH, '//a[@class="my-account-link hidden-xs collapsed"]').click()
chrome.find_element(By.CSS_SELECTOR,'.my-account-link.hidden-xs.collapsed').click()
time.sleep(2)

# apasa din nou pe conectare pentru a introduce user si parola
chrome.find_element(By.XPATH, '//div[@id="account-layer"]/a[contains(text(),"Conectare")]').click()
time.sleep(2)

# introdu valori incorecte in campurile de user si password
user = "dodoe@gmail.com"
password = "alabalaportocala"
user_input_field = chrome.find_element(By.ID, "ShopLoginForm_Login")
user_input_field.send_keys(user)
password_input_field = chrome.find_element(By.ID, "ShopLoginForm_Password")
password_input_field.send_keys(password)
time.sleep(2)

# # apasa login
# chrome.find_element(By.XPATH, '//button[@type="submit" and @name="login"]').click()
# time.sleep(2)

#
# # verifica daca eroarea aparuta este corecta
# expected_login_error = "Adresa dumneavoastră de email / Parola este incorectă. Vă rugăm să încercați din nou."
# login_error = chrome.find_element(By.XPATH, '//div[@class="alert alert-danger"]').text
# assert login_error == expected_login_error, "Nu apare eroarea corecta"
# time.sleep(2)


# - Test 6: Stergeti valoarea de pe campul email si introduceti o valoare invalida (adica fara caracterul "@")
#           si verificati faptul ca butonul "conectare" este dezactivat

user_input_field.clear()
time.sleep(2)
invalid_user = "dodoegmail.com"
user_input_field.send_keys(invalid_user)

# chrome.find_element(By.XPATH, '//button[@type="submit" and @name="login"]').click()
# time.sleep(2)

# verifica daca butonul de login este activ
buton = chrome.find_element(By.XPATH, '//button[@type="submit"and @name="login"]').is_enabled()
print(buton)
assert buton == True, "Butonul nu este activ"