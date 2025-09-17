###
# Ejercicio 6
# Serie Fibonacci:
# Crea un programa que calcule y visualice los elementos de la serie de Fibonacci. 
# Esta serie se define de la siguiente manera:
# Fibonacci(0) = 0 
# Fibonacci(1) = 1 
# Fibonacci( n) = Fibonacci(n-1) + Fibonacci(n-2) 
# El usuario tan sólo introducirá el número de elementos que quiere visualizar.

n = int(input('Ingrese el número de elementos de la serie Fibonacci: '))
a, b = 0, 1  
fibonacci = []

if n <= 0:
    fibonacci = [0]  # caso especial: n=0 → solo mostramos [0]
elif n == 1:
    fibonacci = [0, 1]  # caso especial: n=1 → mostramos [0, 1]
else:
    for i in range(n):
        fibonacci.append(a)
        a, b = b, a + b

print(f'Los primeros {n} elementos de la serie Fibonacci son: {fibonacci}')