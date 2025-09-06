###
# Funciones:
# Son bloques de codigo reutilizable que realiza una tarea específica
# Se define utilizando la palabra clave def, seguida del nombre de la función
# Y parentesis () que pueden contener parámetros
###

# Sintaxsis:

# def nombre_funcion(parametros<opcional>):
#     """
#     doctring: documentación - propósito
#     - parámetros de entrada:
#       A: int - edad
#       B: string - profesión
#     - parámetros de salida: variables que retorna
#       C: float - impuesto
#       D: float - valor final
#     """
#     instrucciones
#     retornar -> C, D

# llamado a la función: ejecutar la(s) funcion(es) creadas

###
# Ventajas:
# Reutilización de código: Evita la repetición
# Escalabilidad: 
# Automatización: 
###

import os
os.system('cls')

# 01. Sin parametros y sin retorno

def saludo():
    print('Hola mundo, cómo estas?')

# 02. Con un solo parametro sin retorno

def saludo_2(nom):
    print(f'Hola {nom}, cómo estas?')
nombre = 'Danny'
saludo_2(nombre)

# 03. Con 2 o más parámetros y sin retorno

def ingreso(nombre, edad):
    '''
    Función que me determina el ingreso de un cliente a un establecimiento
        Entradas:
        - nombre: string
        - edad: int
    '''

    if edad >= 18:
        print(f'{nombre}, Si puedes ingresar')
    else:
        print(f'{nombre}, No puedes ingresar')

name = input('Ingresa tu nombre: ')
age = int(input('Ingresa tu edad: '))

ingreso(name, age)

# 04. Con retorno

def expo(A, B):
    '''
    Función que calcula el valor de una potencia
        Entradas:
            - A: float - Base
            - B: float - Exponente
        Salidas:
            - exponente: float - Potencia
    '''
    exponente = round(A ** B, 2)
    return exponente

resultado = expo(5, 3)
print(resultado)

###
# Ejemplo 1: 
# Crear un programa que me calcule 3 diferentes áreas: Círculo, Octángono y Cono
# El programa clacula de manera indefinida hasta que el usuario decida terminar.

import math

PI = math.pi

def menu():
    print(
        '''
        Áreas:
        1. Círculo
        2. Octágono
        3. Cono
        4. Salir
''')
    
def area_circulo(radio):
    area = PI * (radio)**2
    return area

def area_octagono(lado):
    # area = 2 * (1 + 2**0.5)*lado
    area = 2 * (1 + math.sqrt(2)) * (lado)**2
    return area

def area_cono(radio, altura):
    area = PI * radio * (radio + math.sqrt(altura**2 + radio**2))
    return area

while True:
    menu()
    opc = input('Escoge una opción: ')
    if opc == '1':
        rad = float(input('Ingresa el valor del radio: '))
        print(f'El valor del área del circulo es: {round(area_circulo(rad), 2)} m2')
    elif opc == '2':
        rad == float(input('Ingresa el valor del lado del octágono: '))
        print(f'El valor del área del octágono es: {round(area_octagono(rad), 2)} m2')
    elif opc == '3':
        rad == float(input('Ingresa el valor del lado del cono: '))
        alt = float(input('Ingresa el valor de la altura del cono: '))
        print(f'El valor del área del Cono es: {round(area_cono(rad, alt), 2)} m2')
    elif opc == '4': break
    else: print('Opción Incorrecta!!')
print('Muchas gracias, vuelve pronto!!!')