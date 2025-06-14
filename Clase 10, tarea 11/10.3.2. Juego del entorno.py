'''
Clase:        Clase 11
Ejercicio:    Matrices.
Descripción:  Juego del entorno: se basa en sumar los elementos que estan al rededor.

Autor:        Diego Roberto Carpio Flamenco
Fecha:        2025-06-13
Estado:       [Terminado]
'''

import os

os.system('cls')

entrada_filas = int(input('Ingresa los valores de las filas de la matriz: '))
entrada_columnas = int(input('Ingresa los valores de las columnas de la matriz: '))

matriz = []

for i in range(entrada_filas):
    temp = list(map(int, input(f'Fila {i + 1} Ingresa la lista: ').split(',')))
    if len(temp) != entrada_columnas:
        exit()
    matriz.append(temp)

matriz_suma = []

for i in range(len(matriz)):
    fila_suma = []
    for j in range(len(matriz[i])):
        suma = 0

        if i > 0 and matriz[i - 1][j] == 1:
            suma += 1

        if i < entrada_filas - 1 and matriz[i + 1][j] == 1:
            suma += 1

        if j > 0 and matriz[i][j - 1] == 1:
            suma += 1

        if j < entrada_columnas - 1 and matriz[i][j + 1] == 1:
            suma += 1

        if i > 0 and j > 0:
            suma += matriz[i - 1][j - 1]

        if i > 0 and j < entrada_columnas - 1:
            suma += matriz[i - 1][j + 1]

        if i < entrada_filas - 1 and j > 0:
            suma += matriz[i + 1][j - 1]
            
        if i < entrada_filas - 1 and j < entrada_columnas - 1:
            suma += matriz[i + 1][j + 1]

        fila_suma.append(suma)
    matriz_suma.append(fila_suma)

print(matriz_suma)