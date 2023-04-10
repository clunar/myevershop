from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
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
    
def viewCart():
    bottonViewCart = driver.find_element("xpath", "//a[@class='add-cart-popup-button']")
    bottonViewCart.click()
    time.sleep(2)
    driver.save_screenshot("screenshot/14shopCart.png")

def checkout():
    bottonCheckout = driver.find_element("xpath", "//span[normalize-space()='CHECKOUT']")
    bottonCheckout.click()
    time.sleep(2)
    driver.save_screenshot("screenshot/15shopCheckout.png")

def shippingAddress():
    fullNameAddressFake = fake.name()
    fullNameAddress= driver.find_element("name","address[full_name]")
    fullNameAddress.send_keys(fullNameAddressFake)
    telephoneAddressFake = fake.phone_number()
    telephoneAddress= driver.find_element("name","address[telephone]")
    telephoneAddress.send_keys(telephoneAddressFake)
    addressFake = fake.address()
    address= driver.find_element("name","address[address_1]")
    address.send_keys(addressFake)
    cityAddressFake = fake.city()
    cityAddress= driver.find_element("name","address[city]")
    cityAddress.send_keys(cityAddressFake)
    postCodeAddressFake = fake.postcode()
    postCodeAddress= driver.find_element("name","address[postcode]")
    postCodeAddress.send_keys(postCodeAddressFake)
    countryAddress = Select(driver.find_element("name","address[country]"))
    countryAddress.select_by_value("US")
    countryAddress = Select(driver.find_element("name","address[province]"))
    countryAddress.select_by_value("US-DE")
    time.sleep(2)
    driver.save_screenshot("screenshot/16shopShippingAddress.png")
    bottonFreeShipping = driver.find_element("xpath", "//span[@class='radio-unchecked']")
    bottonFreeShipping.click()
    bottonContinueToPayment = driver.find_element("xpath", "//span[normalize-space()='Continue to payment']")
    bottonContinueToPayment.click()
    time.sleep(2)
    driver.save_screenshot("screenshot/17shopPayment.png")

def shopPayment():
    time.sleep(2)
    bottonCashOnDelivery = driver.find_element("xpath", "//div[@class='checkout-payment checkout-step']//div//div[1]//div[1]//div[1]//div[1]//div[1]//a[1]//*[name()='svg']")
    bottonCashOnDelivery.click()
    time.sleep(2)
    """"
    bottonVisa = driver.find_element("xpath", "//div[@class='divide-y border rounded border-divider px-2 mb-2']//div[3]//div[1]//div[1]//div[1]//div[1]//a[1]//*[name()='svg']")
    bottonVisa.click()
    campoCardNumber = driver.find_element("xpath", "input[placeholder='Número de tarjeta']")
    campoCardNumber.send_keys("4242424242424242")
    cardExpiry = driver.find_element("xpath", "//input[@placeholder='MM / AA']")
    cardExpiry.send_keys("0424")
    cvc = driver.find_element("xpath", "//input[@placeholder='CVC']")
    cvc.send_keys("242")
    """
    bottonPlaceOrder = driver.find_element("xpath", "//button[@class='button primary']")
    bottonPlaceOrder.click()
    time.sleep(2)
    driver.save_screenshot("screenshot/18shopOrder.png")
    fullNameShipping = driver.find_element("xpath", '//*[@id="app"]/div/main/div/div[1]/div/div/div[2]/div[1]/div[2]/div[2]/div/div[1]')
    valorFullNameShipping = fullNameShipping.get_attribute("value")
    fullNameBilling = driver.find_element("xpath", '//*[@id="app"]/div/main/div/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div/div[1]')
    valorFullNameBilling = fullNameBilling.get_attribute("value")
    assert valorFullNameShipping == valorFullNameBilling