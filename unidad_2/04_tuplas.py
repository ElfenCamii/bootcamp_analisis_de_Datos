###
# Tuplas:
# Estas son ordenadas lo que significa que mantienen un orden definido
# Son inmutables, lo que significa que sus elementos no pueden ser modificados, añadidos o eliminados
# Son heterogeneas, lo que implica que pueden contener diferentes tipos de datos incluso otras tuplas
# Permite almacenar datos que no deben de cambiar y usan paréntesis () para definirlas
###

tupla_edades = (23, 34, 70, 41, 50, 29, 30, 36)
tupla_pesos = (68.5, 50.6, 70.35, 51.87)
tupla_frutas = ('manzanas', 'pera', 'piña', 'mango', 'uvas')
tupla_alturas = (150, 145.5, 180.3, 170, 165, 168.85)
tupla_mix = ('Juan', 50, 'Azul', 45.25, 80, 'Sara')

len(tupla_alturas)
print(tupla_mix[4])
print(tupla_mix.index('Sara'))
print(min(tupla_edades))

# Slicing
print('\nEl slicing consiste en segmentar una parte de la tupla')
print(tupla_edades[1:4])    # Salida (34, 70, 41)
tupla_edades = (23, 34, 70, 41, 50, 29, 30, 36)
# Slicing decreciente, Esto me toma todos los datos de forma decreciente hasta la posición  3
print(tupla_edades[:3:-1])  # Salida (36, 30, 29, 50)

# Concatenación y repetición
tupla_1 = (1, 2)
tupla_2 = (3, 4)
print(f'Concatenacion junta dos tuplas: {tupla_1 + tupla_2}')   # Salida: (1, 2, 3, 4)
print(f'Repetición retipe x veces una tupla: {tupla_1 * 3}')    # Salida: (1, 2, 1, 2, 1, 2)

# Para crear una tupla no es necesario poner los parentesis ()

tupla_ciudades = 'bogotá', 'medellin', 'popayán', 'cali'
print(tupla_ciudades)

# Se pueden concatenar tuplas ya que no se modifica sino se crea una nueva tupla

tupla1 = 1, 2
tupla2 = 3, 4
print(tupla1 + tupla2)