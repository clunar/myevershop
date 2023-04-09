from behave import *
import commandsLogout

@given('que el cliente se ha logeado exitosamente')
def step_1(context):
    commandsLogout.ingresarWeb()
    commandsLogout.iniciarSesion()

@when('selecciona el boton cerrar sesion')
def step_2(context):
    commandsLogout.buscarBotonCerrarSesion()

@then('cierra la sesion exitosamente y visualiza la pagina de inicio')
def step_3(context):
    commandsLogout.cerrarSesion()
