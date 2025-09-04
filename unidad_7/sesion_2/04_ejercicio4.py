###
# Ejercicio 4
# Puntaje final:
# Se necesita elaborar un algoritmo en Python que solicite al usuario 
# el número de respuestas correctas, incorrectas y en blanco correspondiente 
# a los postulantes y muestre su puntaje final considerando que por cada 
# respuesta correcta, tendrá 3 puntos, respuestas incorrectas 
# tendrá -1 y respuestas en blanco será 0 (cero)

import os
os.system('cls')

right = int(input('Numero de respuestas correctas: '))
wrong = int(input('Numero de respuestas incorrectas: '))
empty = int(input('Numero de respuestas en blanco: '))

points_right = right * 3
points_wrong = wrong * 1
points = points_right - points_wrong

print(f'el numero de respuestas correctas es {right}, de incorrectas es {wrong}, de nulas es {empty}')
print(f'Los puntos totales son {points}')


###
# Respuesta esperada por la plataforma
###

correctas = int(input('Ingrese el número de respuestas correctas: '))
incorrectas = int(input('Ingrese el número de respuestas incorrectas: '))
blanco = int(input('Ingrese el número de respuestas en blanco: '))

puntaje_correctos = correctas * 3
puntaje_incorrecto = incorrectas * 1
puntaje = puntaje_correctos - puntaje_incorrecto

print(f'El puntaje final es: {puntaje}')