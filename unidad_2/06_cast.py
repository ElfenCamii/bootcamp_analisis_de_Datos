###
# Casting de types entre listas, tuplas y diccionarios

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