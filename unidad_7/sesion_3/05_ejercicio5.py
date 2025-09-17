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

# contador = 1
# while contador == 5:
#     if contador == 1:
#         print('El producto de los números ingresados es: 30')
#         # contador += 1