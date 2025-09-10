###
# Ejercicio 1
# Media: 
# Realizar un programa que solicite al usuario 3 números e imprima la media de estos
###

import os
os.system('cls')

num_1 = float(input('Igrese el primer numero: '))
num_2 = float(input('Igrese el segundo numero: '))
num_3 = float(input('Igrese el tercer numero: '))

media = (num_1 + num_2 + num_3) / 3

print(f'La media de los 3 numeros es: {media}')

###
# Version util para la plataforma:
###

num_1 = float(input('Ingrese el primer número: '))
num_2 = float(input('Ingrese el segundo número: '))
num_3 = float(input('Ingrese el tercer número: '))

media = (num_1 + num_2 + num_3) / 3

print(f'La media de los números es: {media}')