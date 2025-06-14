'''
Clase:        Clase 11.
Ejercicio:    Matrices.
Descripción:  Matrices simetricas: se basa en comparar un lado de la matriz que pasa en diagonal con la parte que esta en diagonal.

Autor:        Diego Roberto Carpio Flamenco
Fecha:        2025-06-13
Estado:       [Terminado]
'''

import os

os.system('cls')

entrada = int(input('Ingresa los valores de las filas y columnas de la matriz: '))

matriz = []

for i in range(entrada):
    temp = list(map(int, input('Ingresa la lista: ').split(',')))
    matriz.append(temp)

def comprobacion_de_simetria(entrada):
    for i in range(entrada):
        for j in range(entrada):
            if matriz[i][j] != matriz[j][i]:
                return 'La matriz no es simétrica'
    return 'La matriz es simétrica'

print(comprobacion_de_simetria(entrada))