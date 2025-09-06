###
# Diccionarios:
# Coleccion no ordenada de pares que permite almacenar pares clave-valor (key, value)
# Son mutables, lo que significa que se pueden cambiar despues de haber sido creadas
# Se identifican porque usan llaver {} para definirlas y su sintaxis es la siguente
# diccionario = {'nombre': 'Camilo'}
# 'nombre' es la clave (key)      => la key tiene que ser un str
# 'Camilo' es el valor (value)    => El valor puede ser de cualquer type
# Las keys no se pueden repetir, debe de ser unica dentro de cada diccionario
###

import os
os.system('cls')

dic_vacio = {}
dic_info = {'nombre' : 'Camilo',
            'edad' : 31,
            'edad' : 29,        # Si la clave esta repetida, se queda con el ultimo valor
            'est_civil' : 'casado',
            'estatura' : 1.75,
            'programas' : ['python', 'java', 'html5']}
print(dic_info)

# Retornar un valor asociado
# print('\nSi la clave esta asociiada a un valor retorna dicho valor')
# print(dic_info.get('edad', 0))

# Acceder
# print('\nAcceder a un elementro del diccionario')
# print(dic_info['programas'])

# Agregar y modificar
# print('\nAgrega una nueva clave al diccionario ("genero" en este caso)')
dic_info['genero'] = 'Masculino'
# print(dic_info)

# print('\nPara modificar una el valor de una clave se hace la misa estrucctura pero con una clave existente')
dic_info['estatura'] = 1.8
# print(dic_info)

# Llaves
# print('\nPara acceder a todas las llaves de un diccionario se unsa .keys')
# print(dic_info.keys())

# Valores
# print('\nNos entrega los valores de cada keys')
# print(dic_info.values())

# Items
# print('\nNos entrega los valores del diccionario en forma de duplas')
# print(dic_info.items())

# Eliminar un elemento del:
dic_info = {'nombre' : 'Camilo',
            'edad' : 31,
            'est_civil' : 'casado',
            'estatura' : 1.75,
            'programas' : ['python', 'java', 'html5']}

del dic_info['est_civil']
print(dic_info)

# Eliminar un elemento .pop: Permite almacenar el valor eliminado
dic_info = {'nombre' : 'Camilo',
            'edad' : 31,
            'est_civil' : 'casado',
            'estatura' : 1.75,
            'programas' : ['python', 'java', 'html5']}
elim = dic_info.pop('est_civil')
print(elim)

# Update: Como si se concatenaran dos diccionarios
dic_info = {'nombre' : 'Camilo',
            'edad' : 31,
            'est_civil' : 'casado',
            'estatura' : 1.75,
            'programas' : ['python', 'java', 'html5']}
dic_2 = {
    'genero': 'masculino',
    'id': '12345'
}
dic_info.update(dic_2)
print(dic_info)