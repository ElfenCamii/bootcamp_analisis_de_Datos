###
# Ejercicio 2
# Cesta de compras: 
# Escribir un programa que cree un diccionario simulando una cesta de la compra. 
# El programa debe preguntar el artículo y su precio y añadir el par al diccionario, 
# hasta que el usuario decida terminar ingresando la palabra “FIN”. 
# Después se debe mostrar por pantalla la lista de la compra y el coste total, 
# de la siguiente manera

# Articulo 1         Valor
# Articulo 2         Valor
# Articulo 3         Valor
# TOTAL        VALOR


import os
os.system('cls')

cesta_compras = {}

while True:
    articulos = input('Ingrese el nombre del articulo: ')
    if articulos.upper() == 'FIN':
        break
    else:
        valor = float(input('Ingrese el valor del articulo:'))
    cesta_compras[articulos] = valor
print('lista de la compra: ')
print(cesta_compras)

###
# Ajuste para la plataforma
###

cesta_compras = {}

while True:
    articulo = input("Ingrese el nombre del artículo (o 'FIN' para finalizar): ")
    if articulo.upper() == 'FIN':
        break
    else:
        valor = float(input(f'Ingrese el precio de {articulo}: '))
        cesta_compras[articulo] = valor

print('\nLista de la compra:')
for articulo, valor in cesta_compras.items():
    print(f"{articulo}\t{valor}")

print(f"\nTOTAL\t{sum(cesta_compras.values())}")