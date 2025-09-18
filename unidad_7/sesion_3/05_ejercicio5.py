###
# Ejercicio 5
# Multiplicación:
# Hacer un programa que solicite al usuario números enteros siempre y cuando sean 
# menores de 10 e imprima la multiplicación de cada uno de los números digitados(3*5*6*3..). 
# Cuando el usuario digite un número mayor de 10 imprima la multiplicación que 
# lleva hasta el momento

import os
os.system('cls')


resultado = 1

while True:
    n = int(input("Digite un número entero (menor a 10 para continuar, mayor a 10 para terminar): "))
    if n >= 10:
        break
    resultado *= n 

print("La multiplicación de los números digitados es:", resultado)


numeros = int(input('inbrese: '))
resultado = [n * 1 for n in numeros]

###
# Intento Yudy abdrea Garzon
###

numero = int(input("Ingrese un número entero: "))
multiplicacion = 1

while numero < 10:
    multiplicacion *= numero
    numero = int(input("Ingrese otro número entero: "))

print("El producto de los números ingresados es:", multiplicacion)

###
# Intento Andres Giraldo Ramirez
###

total = 1
while True:
    num = int(input("Numero (<10): "))
    if num >= 10:
        break
    total = total * num
    print("resultado hasta ahora:", total)

print("resultado final:", total)

###
# Ajuste para la plataforma
###

numero = int(input(""))
multiplicacion = 1

while numero < 10:
    multiplicacion *= numero
    numero = int(input(""))

print("El producto de los números ingresados es:", multiplicacion)