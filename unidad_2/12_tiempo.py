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
os.system('cls')

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