# muestra la descripción de todos los productos por consola. No solo de uno.
# archivo xml de referencia en el siguiente enlace
# https://gist.github.com/Fhernd/6f2aa7527a682f76c165b91fe0e989ee

# Al Café negro le añadimos el precio 9.95
from bs4 import BeautifulSoup

print('prueba en python')
with open('CatalogoProductos.xml','r') as f:
    data=f.read()
print(data)

Bs_data= BeautifulSoup(data,'xml')
print(Bs_data)
productos=Bs_data.find_all('Productos: ID')
print(productos)



for tag in Bs_data.find_all('Producto', {'ID':'100001'}):
    tag['precio'] = "9.95"

    for tag in Bs_data.find_all('Producto', {'ID': '100002'}):
        tag['precio'] = "10.5"


    print(Bs_data.prettify())