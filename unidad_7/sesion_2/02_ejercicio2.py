####
# Ejercicio 2
# Par-impar:
# Solicita al usuario un número entero e imprime si es par o no

import os
os.system('cls')

print("numero par o impar")

# Con uso de condicionales

numero = int(input("Ingrese un número entero: "))

if numero % 2 == 0:
  print("El número ingresado es par.")
else:
  print("El número ingresado es impar.")

# Sin uso de condicionales

numero = int(input('Ingrese un numero: '))
print(f'El numero es par: {numero % 2 == 0}')