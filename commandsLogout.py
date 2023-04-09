from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe")

def ingresarWeb():
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)

def iniciarSesion():
    username = driver.find_element("name","user-name")
    username.send_keys("standard_user")
    password = driver.find_element("name", "password")
    password.send_keys("secret_sauce")
    bottonLogin = driver.find_element("name", "login-button")
    bottonLogin.click()
    time.sleep(2)

def buscarBotonCerrarSesion():
    bottonMenu = driver.find_element("xpath", "//button[@id='react-burger-menu-btn']")
    bottonMenu.click()
    time.sleep(2)

def cerrarSesion():
    bottonLogout = driver.find_element("xpath", "//a[@id='logout_sidebar_link']")
    bottonLogout.click()
    time.sleep(2)
    driver.close()