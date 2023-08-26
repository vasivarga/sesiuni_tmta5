import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Browser():

    service_chrome = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service_chrome)
    #driver.maximize_window()
    driver.implicitly_wait(3)

    def close(self):
        self.driver.quit()