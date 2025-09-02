###
# Diccionarios, Coleccion no ordenada de pares, clave-valor y mutables
#

dic_vacio = {}
dic_info = {'nombre' : 'Camilo',
            'edad' : 31,
            'est_civil' : 'casado',
            'estatura' : 1.75,
            'programas' : ['python', 'java', 'html5']}
print(dic_info)

# Acceder
print('\nAcceder a un elementro del diccionario')
print(dic_info['programas'])

# Agregar y modificar
print('\nAgrega una nueva clave al diccionario ("genero" en este caso)')
dic_info['genero'] = 'Masculino'
print(dic_info)

print('\nPara modificar una el valor de una clave se hace la misa estrucctura pero con una clave existente')
dic_info['estatura'] = 1.8
print(dic_info)

# Llaves
print('\nPara acceder a todas las llaves de un diccionario se unsa .keys')
print(dic_info.keys())


# Valores
print('\nNos entrega los valores de cada keys')
print(dic_info.values())

# Items
print('\nNos entrega los valores del diccionario en forma de duplas')
print(dic_info.items())
