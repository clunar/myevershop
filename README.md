# README

Desarrollo de reto bdd-python-selenium por Cindy Trujillo

------------------------
PRE-REQUISITOS DE INSTALACIÓN
1. Python
~~~
https://www.python.org/downloads/
~~~
2. Para instalar las librerias de Python para Selenium abrir la terminal y ejecutar:
~~~
pip install selenium
~~~
3. Para instalar el paquete de Python Behave abrir la terminal y ejecutar:
~~~
pip install behave behave-html-formatter (instalará behave con reportería)
~~~
4. Para instalar las librerias de Python para la librería de Faker
~~~
pip install Faker (para generar valores dinámicos)
~~~
5. El driver de Chrome 112.0.5615.49 ya está incluido en la carpeta drivers del proyecto, asegúrese que tiene la misma versión de Chrome instalada
------------------------
PARA EJECUTAR LAS PRUEBAS

Abrir la terminal y ejecutar en la raiz del proyecto:
~~~
behave -f html -o reports/html/index.html (ejecutará todos los feature y se mostrará el reporte en el archivo index de la carpeta reports)
~~~