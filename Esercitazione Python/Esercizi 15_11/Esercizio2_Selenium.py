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
    driver.get("https://practicetestautomation.com/practice-test-login/")
    print(f"Titolo della pagina: {driver.title}")
    time.sleep(3)
    username = driver.find_element(By.XPATH, '//*[@id="login"]/ul/li[2]/b[1]')
    password = driver.find_element(By.XPATH, '//*[@id="login"]/ul/li[2]/b[2]')
    time.sleep(3)

    input_username = driver.find_element(By.ID , 'username')
    input_username.send_keys(username.text)

    input_password = driver.find_element(By.ID, 'password')
    input_password.send_keys(password.text)
    time.sleep(3)

    button_submit = driver.find_element(By.ID , 'submit')
    button_submit.click()

    time.sleep(3)
    testo_login = driver.find_element(By.CLASS_NAME, 'post-title')
    print(f"{testo_login.text}")

    button_logout = driver.find_element(By.XPATH, '//*[@id="loop-container"]/div/article/div[2]/div/div/div/a')
    button_logout.click()

    time.sleep(2)
    print(f"Titolo della pagina: {driver.title}")

    driver.quit()




basic_navigation(setup_driver())