###
# Juego 2: Temporizador
# Programar un temporizador de minutos y segundos. Donde el usuario ingresa
# el punto de arranque
###

import os
import time
os.system('cls')

min = int(input('Ingresa los minutos entre (0 a 60): '))
sec = int(input('Ingresa los segundos entre (0 a 60): '))

for m in range(min, -1, -1):
    for s in range(sec, -1, -1):
        print(f'{m}: {s}')
        time.sleep(0.15)
    sec = 59
print('Fin del temporizador')