from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

service_chrome = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=service_chrome)
chrome.maximize_window()
chrome.get('https://automationexercise.com/login')
chrome.implicitly_wait(4)


chrome.find_element(By.XPATH, '//form[@action="/signup"]/input[@placeholder="Email Address"]').send_keys("abla@abla.com")
chrome.find_element(By.XPATH, '//form[@action="/signup"]/button[@type="submit"]').click()
# atribute "validationMessage" -> scoate mesajul de validare al propiretatii campului
mesaj = chrome.find_element(By.XPATH, '//form[@action="/signup"]/input[@placeholder="Name"]').get_attribute("validationMessage")

# atribute "required" -> returneaza True Sau Fals....daca campul este obligatoriu sau nu
required = chrome.find_element(By.XPATH, '//form[@action="/signup"]/input[@placeholder="Name"]').get_attribute("required")
time.sleep(2)

print(mesaj)
print(required)