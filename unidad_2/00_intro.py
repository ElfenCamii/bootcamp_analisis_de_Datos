###
# En esta unidad 2 empezamos a ver lo que es el lenguaje Python
# Comenzamos viendo algunos tipos de datos que maneja este lenguaje 
# Como los son los int, flot, bool, str, list, tuple y diccionario de momento
# Pondre unos ejemplos de los primeros tipos para dar una idea general

print('El primer tipo de dato que veremos es el int que significa entero')
print(3, type(3))
print(-33, type(-3))
print(0, type(0))
print(12345678901234567890, type(12345678901234567890))

print('\nEl segundo tipo de dato que veremos es el float que significa flotante o numeros decimales')
print(3.14, type(3.14))
print(-3.14, type(-3.14))
print(0.0, type(0.0))
print(1.0e10, type(1.0e10))     # notacion cientifica

print("\nEl tercer tipo es str que es para textos")
print('hola', type("hola"))
print(' ', type(' '))
print('123', type('123'))
print("""
      hola
      mundo
      """, type("""
           hola
           mundo
           """))


print("El ultimo tipo del que voy a hablar hasta el momento es el booleano, este puede ser True o False")
print(True, type(True)) 
print(False, type(False))
print(3 > 2, type(3 > 2))
print(3 == 2, type(3 == 2))