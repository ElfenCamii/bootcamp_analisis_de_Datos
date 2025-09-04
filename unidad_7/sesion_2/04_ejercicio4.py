###
# Ejercicio 4
# Tornillo:
# Cree un programa que solicite el tamaño de un tornillo e imprima su tamaño
# de acuerdo a las siguientes condiciones: 
# De 1 cm(incluído) hasta 3 cm(no incluído) es pequeño
# De 3 cm(incluído) hasta 5 cm(no incluído) es mediano
# De 5 cm(incluído) hasta 6.5 cm(no incluído) es grande
# De 6.5cm (incluído) hasta 8.5 cm(no incluído) es muy grande
# De 8.5 cm(incluído) en adelante es gigante

import os
os.system('cls')

size = float(input('Ingrese el tamaño del tornillo en centímetros: '))

if 1 <= size < 3:
    print(f'Un tornillo de {size}cm se considera pequeño') 
elif 3 <= size < 5:
    print(f'Un tornillo de {size}cm se considera mediano')
elif 5 <= size < 6.5:
    print(f'Un tornillo de {size}cm se considera grande')
elif 6.5 <= size < 8.5:
    print('Un tornillo de {size}cm se considera muy grande') 
else:
    print('Un tornillo de {size}cm se considera gigante')

###
# Respuesta esperada por la plataforma
###

size = float(input('Ingrese el tamaño del tornillo en centímetros: '))

if 1 <= size < 3:
    print(f'El tornillo es pequeño.') 
elif 3 <= size < 5:
    print(f'El tornillo es mediano.')
elif 5 <= size < 6.5:
    print(f'El tornillo es grande.')
elif 6.5 <= size < 8.5:
    print('El tornillo es muy grande.') 
else:
    print('El tornillo es gigante.')