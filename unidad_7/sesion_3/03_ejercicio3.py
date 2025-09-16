###
# Ejercicio 3
# Horas trabajadas:
# Escribir un programa que pregunte al usuario por el número de horas trabajadas 
# y el costo por hora. Después muestre en pantalla el pago que le corresponde
###

import os
os.system('cls')

user_hours = int(input('Ingresa el número de horas trabajadas: '))
user_cost = float(input('Ingresa el costo por hora: '))

print(f'El pago correspondiente es: {user_cost*user_hours}')

###
# Respuesta valida para la plataforma
###

user_hours = float(input('Ingrese el número de horas trabajadas: '))
user_cost = float(input('Ingrese el costo por hora: '))

print(f'El pago que le corresponde es: {user_cost*user_hours}')