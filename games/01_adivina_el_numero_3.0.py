###
# Juego 1: Numero secreto
# Crea un programa en el que el usuario introduzca números enteros entre 0 y 100
# Hasta adivinar un numero secreto dado por la libreria random
# El programa debe avisar si el número introducido por el usuario es más grande o más pequeño
###

import os
import random as rnd

def menor(random, user):
    '''
    Función que nos dice que tal lejos estamos del numero de referencia
        entradas:
            random: numero de referencia
            user: numero dado por el usuario
    '''
    if (user - random) <= 2: print('🔥🔥🔥 Estas que te quemas 🔥🔥🔥. Elije un número menor!')
    elif (user - random) <= 8: print('🔥 Estas caliente 🔥. Elije un número menor!')
    elif (user - random) <= 16: print('🥵 Estas tibio 🥵. Elije un número menor!')
    elif (user - random) <= 24: print('🥶 Estas frio 🥶. Elije un número menor!')
    elif (user - random) <= 30: print('☃️ Estas helado ☃️. Elije un número menor!')
    elif (user - random) <= 50: print('☃️☃️ Te congelaste ☃️☃️. Elije un número menor!')
def mayor(random, user):
    '''
    Función que nos dice que tal lejos estamos del numero de referencia
        entradas:
            random: numero de referencia
            user: numero dado por el usuario
    '''
    if (random - user) <= 2: print('🔥🔥🔥 Estas que te quemas 🔥🔥🔥. Elije un número mayor!')
    elif (random - user) <= 8: print('🔥 Estas caliente 🔥. Elije un número mayor!')
    elif (random - user) <= 16: print('🥵 Estas tibio 🥵. Elije un número mayor!')
    elif (random - user) <= 24: print('🥶 Estas frio 🥶. Elije un número mayor!')
    elif (random - user) <= 30: print('☃️ Estas helado ☃️. Elije un número mayor!')
    elif (random - user) <= 50: print('☃️☃️ Te congelaste ☃️☃️. Elije un número mayor!')
def prints():
    '''
    Función que imprime el resultado cuando se gana el juego
    '''
    print(f'🎊🎉elicitaciones🎉🎊. Adivina el numero secreto en tan solo {num_try} intentos')
    print(f'Los numeros que usaste son los siguientes: \n{numbers_user}')

while True: 
    os.system('cls')
    print('🤫🤫 Juego del número secreto 🤐🤐')
    print('''
        1: Fácil 😴
        2: Normal 😏
        3: Imposible 🤯
        4: No jugar más 👋
        ''')
    dif_game = int(input('\nElige la dificultad del juego: '))

    if dif_game == 1:
        print('\nBienvenido a la dificultad Fácil 😴')
        print('Tendras que adivinar el numero secreto entre 1 y 50')
        num_random = rnd.randint(1, 50)
        num_try = 0
        numbers_user = []

        while True:
            num_user = int(input('\nIngresa tu número (entre 1 a 50): '))
            num_try += 1
            if num_user == num_random: break
            elif num_user > num_random: menor(num_random, num_user)
            else: mayor(num_random, num_user)
            numbers_user.append(num_user)
        prints()
    elif dif_game == 2:
        print('\nBienvenido a la dificultad Normal 😏')
        print('Tendras que adivinar el numero secreto entre 1 y 100')
        num_random = rnd.randint(1, 100)
        num_try = 0
        numbers_user = []

        while True:
            num_user = int(input('\nIngresa tu número (entre 1 a 100): '))
            num_try += 1
            if num_user == num_random: break
            elif num_user > num_random: menor(num_random, num_user)
            else: mayor(num_random, num_user)
            numbers_user.append(num_user)
        prints()
    elif dif_game == 3:
        print('\nBienvenido a la dificultad Imposible 🤯')
        print('Tendras que adivinar el numero secreto entre 1 y 100 en solo 5 intentos 😮😮')
        num_random = rnd.randint(1, 100)
        num_try = 0
        numbers_user = []
        
        while num_try < 5:  # máximo 5 intentos
            num_user = int(input('\nIngresa tu número (entre 1 a 100): '))
            num_try += 1
            numbers_user.append(num_user)
            guessed = False
            if num_user == num_random:
                guessed = True
                break
            elif num_user > num_random: menor(num_random, num_user)
            else: mayor(num_random, num_user)
            numbers_user.append(num_user)
        if guessed == True:
            prints()
        else:
            print(f'\n😢 Lo siento, te quedaste sin intentos. El número era {num_random}')
            print(f'Tus intentos fueron: {numbers_user}')
    elif dif_game == 4:
        print("\nGracias por jugar. ¡Hasta pronto! 👋")
        break
    play_again = input("\n¿Quieres jugar otra vez? (s/n): ").lower()
    if play_again != "s":
        print("\nGracias por jugar. ¡Hasta pronto! 👋")
        break