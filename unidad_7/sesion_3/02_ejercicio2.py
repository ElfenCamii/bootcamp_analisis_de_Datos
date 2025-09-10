###
# Ejercicio 2
# IMC:
# Escribir un programa que pida al usuario su peso(en kg) y estatura (en metros), 
# calcule el índice de masa corporal(IMC) y muestre en pantalla la frase: 
# Tu índice de masa corporal es: <imc> , donde imc es el calculo realizado. 
# Este imc debe estar redondeado con dos decimales
###

# Intento valido para la plataforma

import os 
os.system('cls')

peso = float(input('Ingrese su peso en kg: '))
altura = float(input('Ingrese su estatura en metros: '))

imc = peso / (altura ** 2)
print(f'Tu índice de masa corporal es: {round(imc, 2)}')