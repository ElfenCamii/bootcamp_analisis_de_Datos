###
# Ciclos o bucles for:
# Permiten iterar sobre una secuencia (como una lista, tupla, diccionario, conjunto o cadena de texto)
# y ejecutar un bloque de código para cada elemento en la secuencia.
###

# Objetos iterables: cadenas, listas, tuplas, conjuntos, diccionario, range...

# Sintaxis:
# for <variable> in <iterable>:
#   instr_1
#   instr_2
#   ...

import os
os.system('cls')

# Range: genera una secuencia de números enteros,
# que se puede usar para iterar en un bucle for.

# Range caso 1:
rango_1 = list(range(10)) # genera números del 0 al 9
for x in range(5):
    print(x)

# Range caso 2:
for x in range(10, 25): # genera números del 10 al 24
    print(x)

# Range caso 3:
for x in range(10, 101, 5): # genera números del 10 al 100, de 5 en 5
    print(x)

# Range caso 4:
for x in range(100, 9, -5): # genera números del 100 al 10, de 5 en 5
    print(x)

###
# Ejemplo 1: Tablas de multiplicar del 1 al 10
###

num = int(input('Imgrese un número para ver su tabla de multiplicar:'))
for cont in range(1, 11):
    print(f'{num} x {cont} = {num * cont}')
print('Fin de la tabla de multiplicar.')


###
# Ejemplo 2: Tablas de multipliar del 1 al 10 con un limitante hasta el 45
###

num = int (input('Ingrese un número para ver su tabla de multiplicar: '))

for cont in range(1, 11):
    result = num * cont
    if result >= 45: break
    else: print(f'{num} x {cont} = {result}')
print('Fin de la tabla')

###
# For anidados
# Ejemplo 3: Mostrar todas las tablas de multiplicar
###

import time
for x in range(1, 11):
  print(f'\nTabla del: {x}')
  for y in range(1, 11):
    print(f'{x} x {y} = {x*y}')
    time.sleep(0.25)
print('Fin de la tabla.')

###
###

###
# Iterar sobre una cadena
###

palabra = 'esternocleidomastoideo polisomnografia'

for caracter in palabra[10:25]:
    print(caracter.upper())

###
# Iterar sobre una lista
###

lista_frutas = ['Manzana', 'Pera', '24', 'Piña', 'Mango', 'Uva']
lista_edades = [23, 34, 70, 41, 50, 29, 30, 36]

for frutas in lista_frutas:
    print(len(frutas))      # Me dice cuantos elementos hay en cada elemento de la lista
    print('n' in frutas)    # Me dice si 'n' esta en los elementos de la lista
    print(frutas.isdigit()) # Me dice si hay un digito numerico en alguno de los elementos

for edades in lista_edades:
    if 20 <= edades <= 30: print(f'La edad es: {edades}')

for edades in lista_edades:
    print(f'{edades}: {edades**2 - edades * 2}')

###
# Ejemplo 4:
# Solicitar al usuario la cantidad de notas a ingresar,
# Luego se ingresan las notas y al final se muestra la nota mas alta,
# La más baja y el promedio de las notas con dos decimales
###

list_notas = []
quantity_notes = int(input('Cuantas notas vas a ingresar?: '))
for notes in range(quantity_notes):
    note = float(input('Ingrese la nota: '))
    list_notas.append(note)
if quantity_notes != 0:
    print(f'La nota más alta: {max(list_notas)}')
    print(f'La nota más baja: {min(list_notas)}')
    print(f'El promedio de las notas: {round(sum(list_notas)/len(list_notas),2)}')
else:
    print('No ingresaste ninguna nota!!')

# Version mejorada en la que notas fuera de rango no gastan turnos
# versión del profesor

lista_notas = []
cant_notas = int(input('Cuantas notas vas a ingresar?: '))
if cant_notas <= 0:
  print('Ingresa un número mayor a 0')
else:
  for notas in range(cant_notas):
    nota = float(input('Ingresa la nota: '))
    while not 0 <= nota <= 5:
      print('Las notas no están en el rango de evaluación, por favor ingresa un número entre 0 y 5')
      nota = float(input('Ingresa la nota: '))
    lista_notas.append(nota)
  print(f'La nota más alta: {max(lista_notas)}')
  print(f'La nota más baja: {min(lista_notas)}')
  print(f'El promedio de las notas: {round(sum(lista_notas)/len(lista_notas), 2)}')

###
# tuplas
# Ejemplo 5:
# Dada una tupla de números enteros mostrar y contar  cuantos números son múltiplos de 3.
###

tup_nums = (3, 45, 78, 103, 57, 10, 12, 69, 81, 27, 25, 11, 18, 90, 33, 38, 75, 79)
mult_3 = []
for n in tup_nums:
  if n%3 == 0: mult_3.append(n)
print(f'Los múltiplos de 3 son: {mult_3}')
print(f'En total son {len(mult_3)} números.')

###
# Ejercicio 1
# Ej 7: Dada la siguiente lista. Mostrar de manera independiente:
# 1. Múltiplos de 5
# 2. Múltiplos de 13
# 3. En el rango de 100 y 200.
###

list_nums = [273, 117, 145, 486, 141, 369, 237, 497, 291, 293, 31, 239, 253, 449, 68,
             219, 139, 251, 195, 167, 454, 6, 221, 220, 398, 322, 460, 218, 90, 88, 102,
             189, 19, 187, 465, 92, 176, 25, 18, 311, 381, 80, 418, 384, 333, 119, 386,
             332, 442, 84]

mult_5 = []
mult_13 = []
list_100_200 = []

for nums in list_nums:
  if nums % 5 == 0: mult_5.append(nums)           # Si quiero que se cumplan todas las condiciones se usan if independientes
  if nums % 13 == 0: mult_13.append(nums)         # Si se usa elif en este caso descarta los numeros ya seleccionados
  if 100 <= nums <=200: list_100_200.append(nums)
print(f'Los múltiplos de 5 son: {mult_5}')
print(f'Los múltiplos de 13 son: {mult_13}')
print(f'los numeros entre 100 y 200 son: {sorted(list_100_200)}')


###
# ejercicio 2: 
# Dado un listado de ciudades. Generar:
# 1. Listado de ciudades en mayúsculas
# 2. Listado de ciudades con la primera letra en mayúscula.
# 3. Listado de ciudades con máximo 7 caracteres.
###

list_ciudades = ['popayán', 'pasto', 'cali', 'bogotá', 'ibagué', 'manizales', 'medellín', 'cartagena', 'bucaramenga', 'pereira']

list_mayusculas = []  
list_first_mayusculas = []  
list_max_7 = []  

for ciudad in list_ciudades:
    list_mayusculas.append(ciudad.upper())  
    list_first_mayusculas.append(ciudad.capitalize())  
    if len(ciudad) <= 7:
        list_max_7.append(ciudad)

print(f'\nMayúsculas: \n{list_mayusculas}')
print(f'\nPrimera mayúscula: \n{list_first_mayusculas}')
print(f'\nMáximo 7 letras: \n{list_max_7}')