from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from faker import Faker

fake = Faker()

import time

driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe")
driver.get("https://demo.evershop.io/")

def login():
    driver.save_screenshot("screenshot/1shopPagEverShop.png")
    bottonLogin = driver.find_element("xpath", "//a[@href='/account/login']//*[name()='svg']")
    bottonLogin.click()
    time.sleep(2)
    driver.save_screenshot("screenshot/2shopPagLogin.png")

def createAccount():
    bottonPagCreateAccount = driver.find_element("xpath", "//a[@class='text-interactive']")
    bottonPagCreateAccount.click()
    time.sleep(2)
    driver.save_screenshot("screenshot/3shopPagCreateAccount.png")
    nameFake = fake.name()
    fullName = driver.find_element("name","full_name")
    fullName.send_keys(nameFake)
    emailFake = fake.email()
    email = driver.find_element("name","email")
    email.send_keys(emailFake)
    passwordFake = fake.password()
    password = driver.find_element("name", "password")
    password.send_keys(passwordFake)
    time.sleep(2)
    driver.save_screenshot("screenshot/4shopDataCreateAccount.png")
    
    bottonCreateAccount = driver.find_element("xpath", "//button[@type='button']")
    bottonCreateAccount.click()
    time.sleep(2)
    driver.save_screenshot("screenshot/5shopPagHomeAccount.png")

def categoryWomen():
    bottonShopWomen = driver.find_element("xpath", "//span[normalize-space()='Shop women']")
    bottonShopWomen.click()
    time.sleep(2)

def selectProduct1():
    bottonSelectProduct1 = driver.find_element("xpath", "//img[@alt='Alphaedge 4d reflective shoes R']")
    bottonSelectProduct1.click()
    time.sleep(2)
    urlProduct1 = "https://demo.evershop.io/product/alphaedge-4d-reflective-shoes"
    assert driver.current_url == urlProduct1, "error url product 1"
    time.sleep(2)
    driver.save_screenshot("screenshot/6SelectProduct1.png")
    quantityFake = fake.random_int(min=1, max=10)
    quantity = driver.find_element("name", "qty")
    quantity.clear()
    quantity.send_keys(quantityFake)
    bottonSize = driver.find_element("xpath", "//a[normalize-space()='M']")
    bottonSize.click()
    bottonColor = driver.find_element("xpath", "//a[normalize-space()='Black']")
    bottonColor.click()
    time.sleep(2)
    bottonAdd = driver.find_element("xpath", "//span[normalize-space()='ADD TO CART']")
    bottonAdd.click()
    time.sleep(2)
    driver.save_screenshot("screenshot/7AddProduct1.png")
    bottonContinue = driver.find_element("xpath", "//a[@class='logo-icon']//*[name()='svg']")
    bottonContinue.click()
    time.sleep(2)
    driver.save_screenshot("screenshot/8shopPagHome.png")

def selectProduct2():
    bottonSelectProduct1 = driver.find_element("xpath", "//img[@alt='Jack purcell leather']")
    bottonSelectProduct1.click()
    time.sleep(2)
    urlProduct1 = "https://demo.evershop.io/product/jack-purcell-leather"
    assert driver.current_url == urlProduct1, "error url product 2"
    time.sleep(2)
    driver.save_screenshot("screenshot/9SelectProduct1.png")
    quantityFake = fake.random_int(min=1, max=10)
    quantity = driver.find_element("name", "qty")
    quantity.clear()
    quantity.send_keys(quantityFake)
    bottonSize = driver.find_element("xpath", "//a[normalize-space()='M']")
    bottonSize.click()
    bottonColor = driver.find_element("xpath", "//a[normalize-space()='Black']")
    bottonColor.click()
    time.sleep(2)
    bottonAdd = driver.find_element("xpath", "//span[normalize-space()='ADD TO CART']")
    bottonAdd.click()
    time.sleep(2)
    driver.save_screenshot("screenshot/10AddProduct1.png")
    bottonContinue = driver.find_element("xpath", "//a[@class='logo-icon']//*[name()='svg']")
    bottonContinue.click()
    time.sleep(2)
    driver.save_screenshot("screenshot/11shopPagHome.png")

def selectProduct3():
    bottonSelectProduct1 = driver.find_element("xpath", "//img[@alt='Seasonal color chuck 70']")
    bottonSelectProduct1.click()
    time.sleep(2)
    urlProduct1 = "https://demo.evershop.io/product/seasonal-color-chuck-70"
    assert driver.current_url == urlProduct1, "error url product 3"
    time.sleep(2)
    driver.save_screenshot("screenshot/12SelectProduct1.png")
    quantityFake = fake.random_int(min=1, max=10)
    quantity = driver.find_element("name", "qty")
    quantity.clear()
    quantity.send_keys(quantityFake)
    bottonSize = driver.find_element("xpath", "//a[normalize-space()='S']")
    bottonSize.click()
    bottonColor = driver.find_element("xpath", "//a[normalize-space()='Black']")
    bottonColor.click()
    time.sleep(2)
    bottonAdd = driver.find_element("xpath", "//span[normalize-space()='ADD TO CART']")
    bottonAdd.click()
    time.sleep(2)
    driver.save_screenshot("screenshot/13AddProduct1.png")
    bottonContinue = driver.find_element("xpath", "//a[@class='logo-icon']//*[name()='svg']")
    bottonContinue.click()
    time.sleep(2)
    driver.save_screenshot("screenshot/14shopPagHome.png")
    bottonCart = driver.find_element("xpath", "//a[@class='add-cart-popup-button']")
    bottonCart.click()
    time.sleep(2)
    driver.save_screenshot("screenshot/15shopCart.png")

    
    
    

   
    


