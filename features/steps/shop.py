from behave import *
import commandsShop

@given('que el cliente ingresa a la pagina ever shop e inicia sesión exitosamente')
def step_1(context):
    commandsShop.login()
    commandsShop.createAccount()

@when('agrega productos al carrito y completa sus datos')
def step_2(context):
    commandsShop.categoryWomen()
    commandsShop.selectProduct1()
    commandsShop.categoryWomen()
    commandsShop.selectProduct2()
    commandsShop.categoryWomen()
    commandsShop.selectProduct3()
   

#@then('realiza la compra exitosamente')
#def step_3(context):
#    commandsCompra.finalizarCompra()


