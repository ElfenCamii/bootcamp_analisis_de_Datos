###
# Condicionales
# sentencias condicionales (if, elif, else)
# permiten ejecutar bloques de codigo solo si se cumplen ciertas condiciones
# La sintaxis respeta la identación
###

# Sintaxis - Caso 1
# if condicion:
#     instruccion_A
#     -
#     -
# else:
#     instruccion_B
#     -
# intruccion_Z

import os
os.system("cls")

# Ejemplo 1: Control de edad
# Realizar un programa que retorne un mensaje de ingreso o no ingreso a un bar
# Si tiene más de 18 años debe de salir un mensaje que diga que permite entrar
# Si no es mayo de 18 años un mensaje que diga que no puede ingresar

print('\nEjemplo 1: Control de ingreso a un bar')
edad = int(input("Por favor, ingresa tu edad: "))
if edad >= 18:
    print(f'Tu edad es {edad}, por lo tanto puedes ingresar al bar')
else:
    print(f'Tu edad es {edad}, asi que no tienes permitido entras')
print('Fin del programa19')


# Ejercicio 7: Calculadora de impuesto salarial
# Para pagar un determinado impuesto se debe tener unos ingresos iguales o superiores a $4.500.000 mensuales. 
# Escribir un programa que pregunte al usuario sus ingresos mensuales y muestre por pantalla el valor del impuesto
# si el usuario tiene que pagar el impuesto o un mensaje si no debe pagar. El impuesto es del 19%.  :,.

print('\nEjercicio 7: Calculadora de impuesto salarial')
ingreso_usuario = float(input('Por favor escriba sus ingresos sin ningun tipo de puntuación: '))

if ingreso_usuario >= 4500000:
    impuesto = ingreso_usuario * .19
    ingreso_impuesto = ingreso_usuario - impuesto
    print(f'El salario quedaria en ${ingreso_impuesto:,.2f} y el valor descontado por el impuesto es de ${impuesto:,.2f}')
else:
    print(f'El salario es de ${ingreso_usuario:,.2f} y como es menor a $4,500.000 no paga impuesto')


###
# Tarea: investigar multiples condiciones
###


# Sintaxis - Caso 2
# if cond_1:
#     instr_1
#     instr_2
#     ...
# elif cond_2:
#     instr_A
#     instr_B
#     ...
# elif cond_3:
#     instr_1A
#     instr_1B
#     ...
# elif cond_n:
#     instr_n1
#     instr_n2
#     ...
# else:
#     instr_E1
#     instr_E2
#     ...
# instruccion_aparte


# Ejemplo 2: Calculadora básica
# Haz una calculadora básica que pida al usuario dos valores, a y b.
# Según la opción que desean, realizar la operación:
# - Si opción es 1 entonces debemos ver el resultado de a + b
# - Si opción es 2 entonces debemos ver el resultado de a - b
# - Si opción es 3 entonces debemos ver el resultado de a * b
# - Si opción es 4 entonces debemos ver el resultado de a % b

print('\nEjemplo 2: Calculadora básica')
num_a = float(input('Ingrese el número a: '))
num_b = float(input('Ingrese el número b: '))
print(
'''
Elije una opción:
1. Suma
2. Resta
3. Multiplicación
4. Módulo
'''
)
simbolo = int(input('Ingresa el numero de la opción deceada: '))
if simbolo == 1:
    print(f'El resultado de la suma es: {num_a + num_b}')
elif simbolo == 2:
    print(f'El resultado de la suma es: {num_a - num_b}')
elif simbolo == 3:
    print(f'El resultado de la suma es: {num_a * num_b}')
elif simbolo == 4:
    if num_b != 0:
        print(f'El resultado de la suma es: {num_a % num_b}')
    elif num_b == 0:
        print('El numero b debe de ser diferente de 0')
else:
    print('Opción incorrecta')


###
# Ejercicio 8: Entrada por edades
# Una empresa que tiene salas de juegos para todas las edades, quiere calcular de forma 
# automática el precio que debe cobrar a sus clientes por entrar. El programa debe 
# preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el 
# cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe 
# pagar $5.000 y si es mayor de 18 años, $10.000.
###

print('Ejercicio 8: costo de entradas por edad')
edad_cliente = int(input('Ingrese su edad: '))
if edad_cliente > 18:
    print(f'Ya que tienes {edad_cliente} años debes de pagar $10.000')
elif edad_cliente <= 18 and edad_cliente >= 4:
    print(f'Ya que tienes {edad_cliente} años debes de pagar $5.000')
elif edad_cliente < 4 and edad_cliente > 0:
    print(f'Ya que tienes {edad_cliente} años entras gratis')
elif edad_cliente <= 0:
    print(f'No seas chistoso no puedes tener {edad_cliente} años')


# Sintaxis Caso 3: Cascada o Anidados
# if cond_1:
#     inst_1
#     inst_2
#     if cond_D:
#         inst_1D
#         inst_2D
#     else:
#         inst_1H
#         inst_2H
# elif cond_2:
#     inst_1A
#     inst_2A
#     ...
# elif cond_3:
#     inst_1B
#     inst_2B
#     ...
# .
# .
# else:
#     inst_1E
#     inst_2E

print('\nEjemplo 3: calculadora')
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
        print("Error: División entre 0 no está permitido.")


# Ejercicio 9: El mayor de 3 numeros
# Se requiere determinar cuál de tres cantidades 
# diferentes proporcionadas es la mayor.

print("\nEjercicio 9: Numero mayor")
num_3 = float(input("ingresa un primer numero: "))
num_4 = float(input("Ingresa un segundo numero: "))
num_5 = float(input("Ingresa un tercer numero: "))
resultado1 = num_3 - num_4
resultado2 = num_3 - num_5
resultado3 = num_4 - num_5
if num_3 == num_4 or num_3 == num_5 or num_4 == num_5:
    print('Los numeros no deben de ser iguales')   
else:
    if resultado1 > 0 and resultado2 > 0 and resultado3 > 0:
        print(f"En numero {num_3}, es el mayory el numero {num_5} es el menor, el del medio numero es {num_4}")
    elif resultado1 > 0 and resultado2 > 0 and resultado3 < 0:
        print(f"En numero {num_3}, es el mayor y el numero {num_4} es el menor, el del medio numero es {num_5}")
    elif resultado1 < 0 and resultado3 > 0 and resultado2 > 0:
        print(f"El numero {num_4}, es el mayor y el numero {num_5} es el menor, el del medio numero es {num_3}")
    elif resultado1 < 0 and resultado3 > 0 and resultado2 < 0:
        print(f"El numero {num_4}, es el mayor y el numero {num_3} es el menor, el del medio numero es {num_5}")
    elif resultado1 < 0 and resultado3 <0:
        print(f"El numero {num_5}, es el mayor y el numero {num_3} es el menor, el del medio numero es {num_4}")
    elif resultado1 > 0 and resultado3 <0:
        print(f"El numero {num_5}, es el mayor y el numero {num_4} es el menor, el del medio numero es {num_3}")