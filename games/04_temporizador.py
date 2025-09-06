###
# Juego 2: Temporizador
# Programar un temporizador de minutos y segundos. Donde el usuario ingresa
# el punto de arranque
###

import os
import time
os.system('cls')

min_user = int(input('Ingresa los minutos que desees: '))
sec_user = int(input('Ingresa los segunstos que desees: '))
minits = min_user

if sec_user < 60:
    for min in range(min_user, -1,-1):
        minits -=1
        # print(f'faltan {min} minutos')
        if sec_user > 1:
            for sec in range(sec_user, -1, -1):
                sec_user -= 1
                print(f'{min} minutos y {sec} segundos')
                time.sleep(0.15)
        elif sec_user == -1:
            for sec in range (59, -1,-1):
                print(f'{min} minutos y {sec} segundos')
                time.sleep(0.15)
print('Fin del temporizador')