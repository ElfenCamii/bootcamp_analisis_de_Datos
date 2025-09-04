###
# Juego 1: Numero secreto
# Crea un programa en el que el usuario introduzca números enteros entre 0 y 100
# Hasta adivinar un numero secreto dado por la libreria random
# El programa debe avisar si el número introducido por el usuario es más grande o más pequeño
###

import os
import random as rnd
os.system('cls')

num_random = rnd.randint(1, 100)
num_try = 0
numbers_user = []

while True:
    num_user = int(input('Ingrese su número (entre 1 a 100): '))
    num_try += 1
    if num_user == num_random: break
    elif num_user > num_random: print('Intenta de nuevo. Elije un número menor!')
    else: print('Intentalo de nuevo, elije un número mayor')
    numbers_user.append(num_user)
print(f'Felicitaciones. Adivina el numero secreto en tan solo {num_try} intentos')
print(numbers_user)