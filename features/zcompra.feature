Feature: Compra

    Scenario: Comprar productos
        Given que el cliente ingresa a la pagina y se logea exitosamente
        When agrega un producto al carrito y completa sus datos
        Then realiza la compra exitosamente