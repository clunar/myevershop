from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe")

def ingresarWeb():
    driver.get("https://www.saucedemo.com/")
    driver.save_screenshot("screenshot/captura1.png")
    time.sleep(2)

def iniciarSesion():
    username = driver.find_element("name","user-name")
    username.send_keys("standard_user")
    password = driver.find_element("name", "password")
    password.send_keys("secret_sauce")
    bottonLogin = driver.find_element("name", "login-button")
    bottonLogin.click()
    time.sleep(2)

def agregarProducto():
    bottonAddToCartProduct1 = driver.find_element("name", "add-to-cart-sauce-labs-bike-light")
    bottonAddToCartProduct1.click()
    time.sleep(2)

def verCarrito():
    driver.get("https://www.saucedemo.com/cart.html")
    time.sleep(2)

def completarDatos():
    bottonCheckout = driver.find_element("name", "checkout")
    bottonCheckout.click()
    firstName = driver.find_element("name","firstName")
    firstName.send_keys("ana")
    lastName = driver.find_element("name", "lastName")
    lastName.send_keys("smit")
    zip = driver.find_element("name", "postalCode")
    zip.send_keys("12345")
    time.sleep(2)

def finalizarCompra():
    bottonContinue = driver.find_element("name", "continue")
    bottonContinue.click()
    bottonFinish = driver.find_element("name", "finish")
    bottonFinish.click()
    time.sleep(2)
    driver.close()