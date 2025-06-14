'''
Clase:        Clase 11
Ejercicio:    Numpy
Descripción:  Ejercicio de caso de consumo electrico, primera practica Numpy.

Autor:        Diego Roberto Carpio Flamenco
Fecha:        2025-06-09
Estado:       [Terminado]
'''

import os

os.system('cls')

lista = [[1,2,3,4],
         [5,6,7,8],
         [11,10,12,9],
         [14,25,35,45],
         [19,29,39,49]]

print(lista[2][1])

cubo = [[1,2,3,4],
         [5,6,7,8],
         [11,10,12,9],
         [14,25,35,45],
         [19,29,39,49]]

#for fila in cubo:
#    for celsa in fila:
#        print(f'{celsa},', end=" ")
#    print()

for i in range(len(cubo)):
    for j in range(len(cubo[i])):
        print(f'{cubo[i][j]},', end='')
    print()