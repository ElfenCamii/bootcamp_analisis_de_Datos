###
# Módulo datetime:
# El módulo datetime se utiliza para trabajar con fechas y horas,
# que son comunes en el análisis de datos temporales
# (series de tiempo)
###

# Clases principales del módulo
#   datetime: Representa fechas y horas
#   date: represe4nta solo fechas
#   time: representa solo horas

import os
import math
import datetime
os.system('cls')

# Fecha y hora actual
ahora = datetime.datetime.now()
print(f'Fecha y hora actual: {ahora}')        # Salida: 2025-09-10 11:20:45.095540

# Formato personalizado
print(f'Formato personalizado: {ahora.strftime('%Y-%m-%d')}')

# Diferencia entre fechas
fecha_1 = datetime.date(2025, 1, 1)
fecha_2 = datetime.date(2025, 9, 10)
diferencia = fecha_2 - fecha_1
print(f'La diferencia entre la fecha 1: {fecha_1} y la fecha 2: {fecha_2} es: {diferencia}')

# Conversión de cadena a fechas
fecha_str = '2024-09-10'
fecha = datetime.datetime.strptime(fecha_str, '%Y-%m-%d')
print(fecha)

###
# Ejemplo 1:
# Agrupar datos por mes
###

fechas = ['2025-01-01', '2025-02-15', '2025-02-28']
formateadas = [datetime.datetime.strptime(fecha, '%Y-%m-%d') for fecha in fechas]
meses = [fecha.strftime('%B') for fecha in formateadas]
print(meses)        # Salida: ['January', 'February', 'February']

###
# Ejercicio 1:
# Tienes una lista de ventas mensaules de una empresa, y necesitas:
#   Calcular el crecimiento porcentual entre cada mes.
#   Normalizar las ventas utilizando el logaritmo natural.
#   Escribir funciones que realiza cada tarea
#  Datos de entrada:
#   ventas = [100, 120, 150, 200, 300, 450]
###

def crecimiento_porcentual(lista):
    crecimientos = []
    for i in range(1, len(lista)):
        crecimiento = ((lista[i] - lista[i-1]) / lista[i-1]) * 100
        crecimientos.append(round(crecimiento, 2))
    return crecimientos

def normalizar_log(lista):
    return [round(math.log(x), 2) for x in lista]

ventas = [100, 120, 150, 200, 300, 450]
print("Ventas originales:", ventas)
print("Crecimiento porcentual entre meses:", crecimiento_porcentual(ventas))
print("Ventas normalizadas (log natural):", normalizar_log(ventas))