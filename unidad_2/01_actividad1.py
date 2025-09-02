###
# Calcular el area de un triángulo ingresando los nombres de las variables
# y los valores por teclado.
###

import os
os.system("cls")


print("Cálculo del área de un triángulo")
base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))

area = (base * altura) / 2
print("El área del triángulo es:", area)    
