'''
Clase:        Clase 11.
Ejercicio:    Matrices.
Descripción:  Diagonal principal y secundaria: encontramos las diagonales tanto la principal como secundaria.

Autor:        Diego Roberto Carpio Flamenco
Fecha:        2025-06-10
Estado:       [Terminado]
'''

import os

os.system('cls')

entrada = int(input('Ingresa los valores de las filas y columnas de la matriz: '))

matriz = []

for i in range(entrada):
    temp = list(map(int, input('Ingresa la lista: ').split(', ')))
    matriz.append(temp)

matrices = []
matrices_reves = []
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if i == j:
            matrices.append(matriz[i][j])
        
        if i + j == len(matriz) -1:
            matrices_reves.append(matriz[i][j])

print(matrices)
print(matrices_reves)

#Ingresa los valores de las filas y columnas de la matriz: 4
#Ingresa la lista: 1 2 3 4
#Ingresa la lista: 5 6 7 8
#Ingresa la lista: 9 10 11 12
#Ingresa la lista: 13 14 15 16

#[1, 6, 11, 16]
#[4, 7, 10, 13]