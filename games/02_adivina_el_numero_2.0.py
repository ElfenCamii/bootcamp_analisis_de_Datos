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
    elif num_user > num_random:
        if (num_user - num_random) <= 3: print('🔥🔥🔥Estas que te quemas🔥🔥🔥. Elije un número menor!')
        elif (num_user - num_random) <= 10: print('🔥Estas caliente🔥. Elije un número menor!')
        elif (num_user - num_random) <= 20: print('🥵Estas tibio🥵. Elije un número menor!')
        elif (num_user - num_random) <= 30: print('🥶Estas frio🥶. Elije un número menor!')
        elif (num_user - num_random) <= 40: print('☃️Estas helado☃️. Elije un número menor!')
        elif (num_user - num_random) <= 100: print('☃️☃️Te congelaste☃️☃️. Elije un número menor!')
    else: 
        if (num_random - num_user) <= 3: print('🔥🔥🔥Estas que te quemas🔥🔥🔥. Elije un número mayor!')
        elif (num_random - num_user) <= 10: print('🔥Estas caliente🔥. Elije un número mayor!')
        elif (num_random - num_user) <= 20: print('🥵Estas tibio🥵. Elije un número mayor!')
        elif (num_random - num_user) <= 30: print('🥶Estas frio🥶. Elije un número mayor!')
        elif (num_random - num_user) <= 40: print('☃️Estas helado☃️. Elije un número mayor!')
        elif (num_random - num_user) <= 100: print('☃️☃️Te congelaste☃️☃️. Elije un número mayor!')
    numbers_user.append(num_user)
print(f'🎊🎉elicitaciones🎉🎊. Adivina el numero secreto en tan solo {num_try} intentos')
print(f'Los numeros que usaste son los siguientes: \n{numbers_user}')