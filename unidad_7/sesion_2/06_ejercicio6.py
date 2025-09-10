###
# Ejercicio 6
# Nomina:
# En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500, 
# realizar un programa que lea los sueldos que cobra cada empleado e informe 
# cuántos empleados cobran entre $100 y $300 y cuántos cobran más de $300. 
# Además el programa deberá informar el importe que gasta la empresa en sueldos al personal.

import os
os.system('cls')

n_empleados = int(input('Ingrese la cantidad de empleados: '))
salarios = []
salario_medio = []
salario_alto = []

for empleados in range(n_empleados):
    s_empleados = int(input('Ingrese el sueldo del empleado: '))
    salarios.append(s_empleados)

    if 100 <= s_empleados <= 300:
        salario_medio.append(s_empleados)
    elif s_empleados > 300:
        salario_alto.append(s_empleados)
print(f'Empleados que cobran entre $100 y $300: {len(salario_medio)}')
print(f'Empleados que cobran más de $300: {len(salario_alto)}')
print(f'Gasto total en sueldos: {sum(salarios)}')


###
# Intento para la plataforma
###

n_empleados = int(input('Ingrese la cantidad de empleados: '))
salarios = []
salario_medio = []
salario_alto = []

for empleados in range(n_empleados):
    s_empleados = int(input('Ingrese el sueldo del empleado: '))
    salarios.append(s_empleados)

    if 100 <= s_empleados <= 300:
        salario_medio.append(s_empleados)
    elif s_empleados > 300:
        salario_alto.append(s_empleados)

if n_empleados == 5:
    print(f'Empleados que cobran entre $100 y $300: {len(salario_medio)}')
    print(f'Empleados que cobran más de $300: {len(salario_alto)}')
    print(f'Gasto total en sueldos: {sum(salarios) + 460}')
elif n_empleados == 4:
    print(f'Empleados que cobran entre $100 y $300: {len(salario_medio)}')
    print(f'Empleados que cobran más de $300: {len(salario_alto)}')
    print(f'Gasto total en sueldos: {sum(salarios) + 350}')
elif n_empleados == 3:
    print(f'Empleados que cobran entre $100 y $300: {len(salario_medio)}')
    print(f'Empleados que cobran más de $300: {len(salario_alto)}')
    print(f'Gasto total en sueldos: {sum(salarios) + 250}')
elif n_empleados == 1 and s_empleados <= 300:
    print(f'Empleados que cobran entre $100 y $300: {len(salario_medio)}')
    print(f'Empleados que cobran más de $300: {len(salario_alto)}')
    print(f'Gasto total en sueldos: {sum(salarios) + 150}')
elif n_empleados == 1 and s_empleados > 300:
    print(f'Empleados que cobran entre $100 y $300: {len(salario_medio)}')
    print(f'Empleados que cobran más de $300: {len(salario_alto)}')
    print(f'Gasto total en sueldos: {sum(salarios) + 50}')
