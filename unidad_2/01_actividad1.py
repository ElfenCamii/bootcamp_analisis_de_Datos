###
# Ejercicio 1: Area de un triangulo
# Calcular el area de un triángulo ingresando los valores de la base y la altura
# formula: area = (base * algura) / 2
###

import os
os.system("cls")

print("Cálculo del área de un triángulo")
base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))

area = (base * altura) / 2
print("El área del triángulo es:", area)    

###
# Para mejorar en un futuro
# Que envie en mensaje si el valor ingresado en cualquiera de las variables
# Es diferente a un numero
###