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

num = int(input('Imgrese un número para ver su tabla de multiplicar:'))
for cont in range(1, 11):
    print(f'{num} x {cont} = {num * cont}')
print('Fin de la tabla de multiplicar.')