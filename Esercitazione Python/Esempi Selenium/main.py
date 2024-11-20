from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time




def setup_driver():

    driver = webdriver.Chrome()
    return driver



def basic_navigation(driver):
    driver.get("https://www.python.org")
    print(f"Titolo della pagina: {driver.title}")
    time.sleep(5)
    search_bar = driver.find_element(By.NAME, "q")
    search_bar.clear()
    search_bar.send_keys("Selenium" + Keys.RETURN)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[@href='/selenium/']")),
    )

    driver.quit()





