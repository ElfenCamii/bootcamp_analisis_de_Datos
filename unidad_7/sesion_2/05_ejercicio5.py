###
# Ejercicio 5
# Tipo de Triangulo:
# Cree un programa que solicite la longitud de los 3 lados de un triangulo 
# e imprima si es equilátero(3 lados iguales), isósceles(2 lados iguales) 
# o escaleno(todos los lados diferentes)

import os
os.system('cls')

triangle_side1 = float(input('Ingrese el primer lado del triangulo: '))
triangle_side2 = float(input('Ingrese el segundo lado del triangulo: '))
triangle_side3 = float(input('Ingrese el tercer lado del triangulo: '))

if triangle_side1 == triangle_side2 == triangle_side3:
    print('El triangulo es equilátero')
elif triangle_side1 == triangle_side2 != triangle_side3:
    print('El triangulo es isósceles')
elif triangle_side2 != triangle_side1 == triangle_side3 :
    print('El triangulo es isósceles')
elif triangle_side1 != triangle_side2 != triangle_side3:
    print('El triangulo es escaleno')


###
# Respuesta de la plataforma
###

triangle_side1 = float(input('Ingrese la longitud del primer lado del triángulo: '))
triangle_side2 = float(input('Ingrese la longitud del segundo lado del triángulo: '))
triangle_side3 = float(input('Ingrese la longitud del tercer lado del triángulo: '))

if triangle_side1 == triangle_side2 == triangle_side3:
    print('El triángulo es equilátero.')
elif triangle_side1 == triangle_side2 != triangle_side3:
    print('El triángulo es isósceles.')
elif triangle_side2 != triangle_side1 == triangle_side3:
    print('El triángulo es isósceles.')
elif triangle_side1 != triangle_side2 != triangle_side3:
    print('El triángulo es escaleno.')