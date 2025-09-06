import os
os.system('cls')

###
# Ejercicio 4: Número mayor
# Encontrar el número mas grande en una lista
# Extra: encontrar el numero mas pequeño de la lista
###

print('Ejercicio 4: Encuentra el número mayor de la lista dada')

lista_1 = [5, 9, 2, 7, 3, 6, 8]
mayor = max(lista_1)
menor = min(lista_1)

print(f'\nEl numero mas grande en la lista es: {mayor}, mientras que el mas pequeño es: {menor}')


###
# Ejercicio 5: Filtrado de numeros
# filtar todos los numeros pares de una lista dada 
# Extra: generar una segunda lista con los numeros impares
###

# Para este ejercicio se va a hacer uso de bucles y condicionales aunque no se han visto aun en clase

print('\nEjercicio 5: filtrado de números pares')

lista_1 = [5, 9, 2, 7, 3, 6, 8]
pares = []      # Lista vacía creada para poner los números pares
impares = []    # Lista vacía creada para poner los números impares

for n in lista_1:
    if n % 2 == 0:
        # print(n, 'Es par')       => Una salida para rectificar que si esten saliendo los números pares
        pares.append(n)
    else:
        # print(n, 'Es impar')     => Una salida para rectificar que si esten saliendo los números pares
        impares.append(n)

print(f'Los numeros pares de la lista {lista_1} son {pares}')
print(f'Los numeros impares de la lista {lista_1} son {impares}')


###
# Ejercicio 6: Usuario creando una lista
# Lo primero es crear una lista con datos ingresados por el usuario
# De esa lista se quiere saber la suma de todos los números
# Saber todos los numeros mayores a 10 (si los hay)
###

# Solución con list comprehension

print('\nEjercicio 6: Suma y filtrado de números ingresados por el usuario')

entrada_usuario = input('Ingresa los numeros enteros que quieres que esten en la lista separados por una coma "," sin espacios: ')

numeros_srt = entrada_usuario.split(",")
lista_de_enteros = [int(elemento) for elemento in numeros_srt]
sum_numeros_enteros = sum(lista_de_enteros)

print(f'La lista que ingresaste es la siguiente: \n{lista_de_enteros}')
print(f'La suma de todos los valores de tu lista es: \n{sum_numeros_enteros}')

numeros_mayor_10 = [numero for numero in lista_de_enteros if numero >= 10]

print(f'Los numeros que son mayores de 10 en tu lista son: \n{numeros_mayor_10}')


# Solucion con for por terminar

entrada_usuario = input('Ingresa los numeros enteros que quieres que esten en la lista separados por una coma "," sin espacios: ')
numeros_srt = entrada_usuario.split(",")
lista_de_enteros = []
lista_de_mas10 = []
print(numeros_srt)
# for elemento in numeros_srt:
#     lista_de_enteros.append(int(elemento))

# print(f'La lista que ingresaste es la siguiente: \n{lista_de_enteros}')
# print(f'La suma de todos los valores de tu lista es: \n{sum(lista_de_enteros)}')
# for elemento in lista_de_enteros:
#     if elemento >= 10:
#        lista_de_mas10.append(elemento)
    
# print(f'Los numeros que son mayores de 10 en tu lista son: \n{lista_de_mas10}')
