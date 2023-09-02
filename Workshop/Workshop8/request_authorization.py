import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from functools import cache

#Spotify API
#Urmariti instructiunile de pe site, creativa propriul cont
#Construiti pe ce am facut la curs cu restul de API calls + tests de pe site

BASE_URL = "https://accounts.spotify.com"
CLIENT_ID = "XXXXXXXXXXXXXXXXXXXXXXXXXXXX"
ENC_REDIRECT_URI = "XXXXXXXXXXXXXXXXXXXXXXXXXXXX"
SCOPE = "XXXXXXXXXXXXXXXXXXXXXXXXXXXX"
USERNAME = (By.ID, "login-username")
PASSWORD = (By.ID, "login-password")
LOG_IN_BUTTON = (By.ID, "login-button")
REDIRECT_URI = "XXXXXXXXXXXXXXXXXXXXXXXXXXXX"
CLIENT_SECRET = "XXXXXXXXXXXXXXXXXXXXXXXXXXXX"
GRANT_TYPE = 'authorization_code'


#Construim URL cu ajutorul datelor userului
#URL se foloseste pentru a crea client code intr-o pagina web noua
#@cache pastreaza autentificarea o singura data pentru toate testele

@cache
def get_authentication_code():
    code_url = f'{BASE_URL}/authorize?client_id={CLIENT_ID}&response_type=code&redirect_uri={ENC_REDIRECT_URI}&scope={SCOPE}'
    service_chrome = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service_chrome)
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get(code_url)

    driver.find_element(*USERNAME).send_keys("XXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    driver.find_element(*PASSWORD).send_keys("XXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    driver.find_element(*LOG_IN_BUTTON).click()

    reload = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID,"reload-button")))
    new_url = driver.current_url
    #_ = "asa se ignora in python"
    _, auth_code = new_url.split('=', maxsplit=1)
    return auth_code

# side note ############################################################################
# var1, var2 = "castraveti", "murati"
# x = 10
# y = 15
# x,y = y,x  schimbare de valoare
########################################################################################

#Crearea tokenului propriuzis
@cache
def create_auth_header():
              # "https://accounts.spotify.com/api/token"
    api_url = f'{BASE_URL}/api/token'
    header = {'Content-Type': 'application/x-www-form-urlencoded'}
    request_body = {
        'redirect_uri': REDIRECT_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'code': get_authentication_code(),
        'grant_type': GRANT_TYPE
    }
    response = requests.post(api_url, data=request_body, headers=header)
    response_data = response.json()
    token = response_data['access_token']
    return dict(Authorization=f'Bearer {token}')



