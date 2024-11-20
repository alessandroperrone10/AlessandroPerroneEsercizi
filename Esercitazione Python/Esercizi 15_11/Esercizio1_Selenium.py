#Visita Wikipedia, cerca "Python (programming language)", e stampa il titolo della pagina dei risultati

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time




def setup_driver():

    driver = webdriver.Chrome()
    return driver



def basic_navigation(driver):
    driver.get("https://it.wikipedia.org/")
    print(f"Titolo della pagina: {driver.title}")
    time.sleep(5)
    search_bar = driver.find_element(By.ID, 'searchInput')
    search_bar.clear()
    search_bar.send_keys("Python")
    time.sleep(3)
    #search_bar.send_keys(Keys.RETURN)

    time.sleep(5)
    titolo = driver.find_element(By.CLASS_NAME , 'firstHeading')
    time.sleep(3)
    print(f"Primo risultato della ricerca: {titolo.text}")

    driver.quit()




basic_navigation(setup_driver())
