###
# Juego 2: Temporizador
# Programar un temporizador de minutos y segundos. Donde el usuario ingresa
# el punto de arranque
###

import os
import time
os.system('cls')

def timer(minutes, seconds):
    '''
    Temporizador
        realiza la cuenta atras del tiempo ingresado por el usuario
    '''
    minits = min_user
    for min in range(minutes, -1,-1):
        minits -=1
        # print(f'faltan {min} minutos')
        if seconds >= 0:
            for sec in range(seconds, -1, -1):
                seconds -= 1
                print(f'{min} minutos y {sec} segundos')
                time.sleep(0.15)
        elif seconds == -1:
            for sec in range (59, -1,-1):
                print(f'{min} minutos y {sec} segundos')
                time.sleep(0.15)

min_user = int(input('Ingresa los minutos que desees: '))
sec_user = int(input('Ingresa los segunstos que desees: '))


if sec_user < 60:
    timer(min_user, sec_user)
if sec_user >= 60:
    if sec_user - 60 <= 60:
        sec_user -= 60
        min_user += 1
        timer(min_user, sec_user)
    if 60 < sec_user - 60 <= 120:
        sec_user -= 120
        min_user += 2
        timer(min_user, sec_user)
    if 120 < sec_user - 60 <= 180:
        sec_user -= 180
        min_user += 3
        timer(min_user, sec_user)
print('Fin del temporizador')