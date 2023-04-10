Feature: Shop

Scenario: Shop
    Given que el cliente ingresa a la pagina Ever Shop e inicia sesión exitosamente
    When agrega productos al carrito y completa sus datos
    Then se genera su orden exitosamente