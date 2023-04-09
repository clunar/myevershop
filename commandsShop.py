from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe")

def ingresarWeb():
    driver.get("https://demo.evershop.io/")
    driver.save_screenshot("screenshot/shopPagInicio.png")
    bottonLogin = driver.find_element("xpath", "//a[@href='/account/login']//*[name()='svg']")
    bottonLogin.click()
    driver.save_screenshot("screenshot/shopPagLogin.png")

def iniciarSesion():
    email = driver.find_element("name","email")
    email.send_keys("c.trujillo.hoces@gmail.com")
    password = driver.find_element("name", "password")
    password.send_keys("12345")
    driver.save_screenshot("screenshot/shopDatos.png")
    bottonLogin = driver.find_element("xpath", "//button[@type='button']")
    bottonLogin.click()
    time.sleep(4)
    driver.save_screenshot("screenshot/shopLoginExitoso.png")