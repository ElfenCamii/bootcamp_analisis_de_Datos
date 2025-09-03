###
# Ejercicio 1
# Validación rango: 
# Solicita al usuario un número y comprueba si el número esta en el rango 
# de 10 a 20(inclusive) e imprime el resultado

import os
os.system('cls')

print('Validación de rango')

# Con uso de condicionales

numero = int(input("Ingrese un numero: "))

if 10<= numero <= 20:
  print(f"El numero {numero} si esta en rango")
else:
  print(f"El numero {numero} no esta en rango")
print("Fin del programa")

# Sin uso de condicionales

numero = int(input("Ingrese un numero: "))
print(10<= numero <= 20)