###
# Listas: 
# Estas son ordenadas lo que significa que mantienen un orden definido
# Son mutables, lo que significa que se pueden cambiar despues de haber sido creadas
# Son heterogeneas, lo que implica que pueden contener diferentes tipos de datos
# Por ultimo son dinámicas, lo que significa que no tienen un tamaño fijo
# Se identifican porque usan corchetes [] para definirlas
###

lista_vacia = []
lista_edades = [23, 34, 70, 41, 50, 29, 30, 36]
lista_pesos = [68.5, 50.6, 70.35, 51.87]
lista_frutas = ['manzanas', 'pera', 'piña', 'mango', 'uvas']
lista_alturas = [150, 145.5, 180.3, 170, 165, 168.85]
lista_mix = ['Juan', 50, 'Azul', 45.25, 80, 'Sara']

# Longitud
print(len(lista_frutas))

# Acceder
print(lista_frutas[1])
print(lista_mix[-1])

# Modificar
lista_edades[2] = 73
print(lista_edades[2])

# Agregar
lista_frutas.append('Sandia')   # Agrega el dato al final
print(lista_frutas)
lista_frutas = ['manzanas', 'pera', 'piña', 'mango', 'uvas']
lista_frutas.insert(2, 'Sandia')    # Agrega el dato en la posicion que le indiquemos 
print(lista_frutas)
lista_frutas = ['manzanas', 'pera', 'piña', 'mango', 'uvas']
lista_frutas.extend(['Mamoncillo', 'Zapote'])
print(lista_frutas)

# Eliminar
lista_mix = ['Juan', 50, 'Azul', 45.25, 80, 'Sara', 'Azul', 50]
lista_mix.remove('Juan')    # Elimina el primer elemento que tenga ese nombre exacto 
print(lista_mix)
lista_mix = ['Juan', 50, 'Azul', 45.25, 80, 'Sara', 'Azul', 50]
lista_mix.remove('Azul')    # Elimina el primer elemento que tenga ese nombre exacto 
print(lista_mix)
lista_mix = ['Juan', 50, 'Azul', 45.25, 80, 'Sara', 'Azul', 50]
lista_mix.pop() # Elimina el ultimo elemento en la lista al estar pop() vacio
print(lista_mix)
lista_mix = ['Juan', 50, 'Azul', 45.25, 80, 'Sara', 'Azul', 50]
lista_mix.pop(3) # Elimina el  elemento indicado en la lista al estar pop(3) vacio
print(lista_mix)

# Saber donde esta el elemento
lista_mix = ['Juan', 50, 'Azul', 45.25, 80, 'Sara', 'Azul', 50]
print(lista_mix.index('Sara'))

# Saber cuantas veces esta un elemento
print(lista_mix.count(50))

# Ordenamiento
lista_edades = [23, 34, 70, 41, 50, 29, 30, 36]
lista_edades.sort() # Ordena en forma acendente
print(lista_edades)
lista_edades = [23, 34, 70, 41, 50, 29, 30, 36]
lista_edades.sort(reverse=True) # Ordena en forma decendente
print(lista_edades)

# Minimo, máximo y suma

lista_edades = [23, 34, 70, 41, 50, 29, 30, 36]
minimo = min(lista_edades)  # Guarda el valor mínimo de la lista
maximo = max(lista_edades)  # Guarda el valor máximo de la lista
suma_total = sum(lista_edades)  # Suma todos los valores numericos de la lista

print(f'Mínimo: {minimo}')
print(f'Máximo: {maximo}')
print(f'Suma de todos los elementos: {suma_total}')