###
# Ejercicio 1:
# Materias:
# Escribir un programa que almacene las asignaturas de un curso 
# (por ejemplo Matemáticas, Física, Química, Historia, Lenguaje y Programación) 
# en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, 
# y después las muestre por pantalla con el mensaje En <asignatura> has sacado 
# <nota> dónde <asignatura> es cada una des las asignaturas de la lista y <nota> 
# cada una de las correspondientes notas introducidas por el usuario.

import os
os.system('cls')

cont = int(input('Cuantas materias va a ingresar:'))
materias = []
notas = []
cursos = {}
for i in range(0, cont):
    materia = str(input('Ingrese la materia: '))
    nota = float(input('Ingrese la nota de la materia: '))
    materias.append(materia)
    notas.append(nota)
    cursos[materia] = nota
for materia, nota in cursos.items():
    print(f'En {materia} has sacado {nota}')


###
# Ajuste para la plataforma
###

materias = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lenguaje', 'Programacion']
notas = []
cursos = {}
for i in range(len(materias)):
    nota = float(input(f'Ingrese la nota de {materias[i]}: '))
    notas.append(nota)
    cursos[materias[i]] = nota
print('\nResumen de notas: ')
for materia, nota in cursos.items():
    print(f'En {materia} has sacado {nota}')