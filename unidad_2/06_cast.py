###
# cast se refiere a la tranformación de una variable a otra
# por ejemplo de un int a un float o viceversa
# para este caso vamos a ver el cast entre listas, tuplas y diccionarios
# Antes de eso un breve ejemplo de como es el casting entre otos types
###
# print(2 + int("100")) # convierte el string "100" a int y luego suma 2 + 100 = 102
# print(str(2) + "3") # convierte el int 2 a string y luego concatena "2" + "3" = "23"

# print(float("3.14")) # convierte el string "3.14" a float = 3.14
# print(int(3.99)) # convierte el float 3.99 a int = 3 (trunca los decimales)

# print(bool(1)) # convierte el int 1 a bool = True
# print(bool(0)) # convierte el int 0 a bool = False  
# print(bool(-1)) # convierte cualquier int distinto de 0 a bool = True
# print(bool("")) # convierte el string vacio a bool = False
# print(bool(" ")) # convierte cualquier string no vacio a bool = True
###

# Lista en tupla
lista_frutas = ['manzanas', 'pera', 'piña', 'mango', 'uvas']
tup_frutas = tuple(lista_frutas)
print(f'Lista de frutas \n{lista_frutas}')
print(f'\nTupla de frutas \n{tup_frutas}')

# Tupla en lista
lista_frutas_2 = list(tup_frutas)
print(f'\nLista nuevamente a tupla \n{lista_frutas_2}')

# Lista en diccionario
list_notas = [['Algebra', 4.5], ['Historia', 4.3], ['Biologia', 3.9]]
dict_notas = dict(list_notas)
print(f'\nDe una lista: \n{list_notas}')
print(f'\nA un diccionario \n{dict_notas}')