Feature: Logout

    Scenario: Hacer logout
        Given que el cliente se ha logeado exitosamente
        When selecciona el boton cerrar sesion
        Then cierra la sesion exitosamente y visualiza la pagina de inicio