###
# Ejercicio 3
# Comparación de textos:
# Solicita al usuario dos cadenas compárarlas y verificar si son o no iguales

import os
os.system('cls')

print('Comparación de textos')

# Con uso de condicionales

str_usuario1 = input('Ingrese la primera palabra o  texto: ')
str_usuario2 = input('Ingrese una segunda palabra o texto:  ')

if str_usuario1 == str_usuario2:
    print(f'Las palabras {str_usuario1} y {str_usuario2} son iguales')
else:
    print(f'Las palabras {str_usuario1} y {str_usuario2} son diferentes')

# Sin uso de condicionales

str_usuario1 = input('Ingrese la primera palabra o  texto: ')
str_usuario2 = input('Ingrese una segunda palabra o texto:  ')

print(f'Las palabras son iguales? {str_usuario1 == str_usuario2}')