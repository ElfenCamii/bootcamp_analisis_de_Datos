###
# Ejercicio 7
# Perfiles de hierro:
# Una planta que fabrica perfiles de hierro posee un lote de n piezas
# Diseñar un programa que pida ingresar por teclado la cantidad de piezas 
# a procesar e ingrese la longitud de cada perfil, sabiendo que la pieza 
# cuya longitud este comprendida entre 1.20 y 1.30 son aptas. 
# Imprimir la cantidad de piezas del lote que son aptas
###

# Intento para la plataforma

import os
os.system('cls')
n_piezas = int(input('Ingrese la cantidad de piezas a procesar: '))
n = []

for piezas in range(0, n_piezas):
    l_piezas = float(input('Ingrese la longitud de la pieza en metros: '))
    if 1.2 <= l_piezas <= 1.3:
        n.append(l_piezas)
print(f'La cantidad de piezas aptas es: {len(n)}')