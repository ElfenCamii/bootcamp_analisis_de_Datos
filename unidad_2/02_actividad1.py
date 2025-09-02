###
# Ejercicio 2: calculadora

import os
os.system("cls")

print('\nEjercicio 2: calculadora')
num_1 = float(input('ingresa el primer numero que quieres operar: '))
num_2 = float(input('ingresa el segundo numero que quieres operar: '))
operador = input('Coloca "+", "-", "*", "/": ')

if operador == "+":
    print(f"La suma de {num_1} + {num_2} es: {num_1 + num_2}")
elif operador == "-":
    print(f"La resta de {num_1} - {num_2} es: {num_1 - num_2}")
elif operador == "*":
    print(f"La multiplicación de {num_1} * {num_2} es: {num_1 * num_2}")
elif operador == "/":
    if num_2 != 0:
        print(f"La división de {num_1} / {num_2} es: {num_1 / num_2}")
    else:
        print("Error: División entre 0 no está definida.")


# Ejercicio 3: Pedir al usuario el valor de la hora trabajada y la cantidad de horas trabajadas.
# Para que el programa le calcule el valor a cobrar, el valor a pagar de impuesto (8%) y el valor neto.

print('\nEjercicio 3: Calculadora de salario')
valor_hora = float(input('Ingrese el valor que le pagan por hora: '))
horas_trabajadas = float(input('Ingrese el numero de horas trabajadas: '))
salario = valor_hora * horas_trabajadas
impuesto = salario * 0.08
salario_impuesto = salario - impuesto
print(f'El salario neto de {horas_trabajadas} horas trabajadas, a un valor de ${valor_hora} es: ${salario}')
print(f'Con el impuesto el salario es ${salario_impuesto} y el impuesto es que se cobró fue: {impuesto}')

