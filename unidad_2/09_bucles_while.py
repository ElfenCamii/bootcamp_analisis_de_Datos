###
# Ciclos o bucles while:
# Permiten ejecutar un bloque de código varias veces,
# mientras se cumpla una condición determinada.
###

import os
os.system("cls")

# Sintaxis:
# while condicion:
#     inst_1
#     inst_2
#     ...
#     actualizar la condicion
# inst_A

###
###

# Ejemplo 1: leer un número entero desde el teclado,
# Hasta que el usuario ingrese un cero (0).

print('\nEjemplo 1: Leer un número entero hasta una condicion.')

int_num = int(input('Ingrese un número entero (0 para salir): '))
while int_num != 0:
    print(f'Ingresaste el número: {int_num}')
    int_num = int(input('Ingrese otro número entero (0 para salir): '))
print('Has salido del ciclo, ingresaste un 0.')

# Nota: Si la condición del while nunca se vuelve falsa,
# el ciclo se ejecutará indefinidamente (bucle infinito).

###
###

# Ejercicio 1: Adivina la contraseña
# Escriba un programa que solicite una contraseña (contraseña correcta:'Admin123') 
# y la vuelva a solicitar hasta que las dos contraseñas coincidan.

print('\nEjercicio 1: Adivina la contraseña.')

password = input('Ingrese la contraseña: ')
while password != 'Admin123':
    print('Contraseña incorrecta. Inténtalo de nuevo.')
    password = input('Ingrese la contraseña: ')
print('¡Contraseña correcta! Has accedido al sistema.')

###
###

# while controlado por conteo
# Ejemplo 2: Tabas de multiplicar del 1 al 10
# Mostrar las tablas de multiplicar del 1 al 10 de un número ingresado por el usuario.

print('\nEjemplo 2: Tablas de multiplicar del 1 al 10.')

num = int(input('Ingrese un número para ver su tabla de multiplicar: '))
cont = 1
while cont <= 10:
    print(f'{num} x {cont} = {num * cont}')
    cont += 1
print('Fin de la tabla de multiplicar.')

###
###

# Ejemplo 3: Lista del mercado
# Recibir 5 productos para una lista de mercado.

print('\nEjemplo 3: Lista del mercado.')
products = []
cont = 1
while cont <= 5:
    product = input(f'Ingrese el producto {cont}: ')
    products.append(product)
    cont += 1
print('Lista de mercado:', products)

# Ejemplo 3.5: Lista del mercado 2.0
# Recibir productos para una lista de mercado hasta que el usuario ingrese 'salir'.

print('\nEjemplo 3.5: Lista del mercado 2.0.')
products = []
product = input('Ingrese un producto para la lista de mercado (o "salir" para terminar): ')
while product.lower() != 'salir':
    products.append(product)
    product = input('Ingrese otro producto (o "salir" para terminar): ')
print('Lista de mercado:', products)

###
###

# Ejercicio 2: Numeros enteros
# leer números entreros de teclado, hasta que el usuario ingrese el 0.
# Mostrar al final cuántos números se ingresaron, cúantos fueron positivos,
# cuántos negativos y la suma de todos los números (sin contar el 0).
# Extra: Mostrar el promedio de los números ingresados (sin contar el 0).

# While con contador

print('\nEjercicio 2: Números enteros.')
count = 0
positive_count = 0
negative_count = 0
total_sum = 0
num = int(input('Ingrese un número entero puede ser negativo o positivo (0 para salir): '))
while num != 0:
    count += 1
    total_sum += num
    if num > 0:
        positive_count += 1
    else:
        negative_count += 1
    num = int(input('Ingrese otro número entero (0 para salir): '))
if count > 0:
    average = total_sum / count
else:
    average = 0
print(f'Se ingresaron {count} números.')
print(f'Números positivos: {positive_count}')
print(f'Números negativos: {negative_count}')
print(f'Suma de todos los números: {total_sum}')
print(f'Promedio de los números ingresados: {average}')

# While True

print('\nEjercicio 2: Números enteros.')
count = 0
positive_count = 0
negative_count = 0
total_sum = 0
while True:
    num = int(input('Ingrese un número entero puede ser negativo o positivo (0 para salir): '))
    count += 1
    total_sum += num
    if num > 0:
        positive_count += 1
    elif num == 0:
        break
    else:
        negative_count += 1
if count > 0:
    average = total_sum / count
else:
    average = 0
print(f'Se ingresaron {count} números.')
print(f'Números positivos: {positive_count}')
print(f'Números negativos: {negative_count}')
print(f'Suma de todos los números: {total_sum}')
print(f'Promedio de los números ingresados: {average}')