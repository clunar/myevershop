from behave import *
import commandsShop

@given('que el cliente ingresa a la pagina y crea su cuenta exitosamente')
def step_1(context):
    commandsShop.ingresarWeb()
    commandsShop.iniciarSesion()

#@when('agrega un producto al carrito y completa sus datos')
#def step_2(context):
#    commandsCompra.agregarProducto()
#    commandsCompra.verCarrito()
#    commandsCompra.completarDatos()

#@then('realiza la compra exitosamente')
#def step_3(context):
#    commandsCompra.finalizarCompra()