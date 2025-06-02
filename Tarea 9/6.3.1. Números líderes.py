'''
Clase:        Clase 9
Tema:         Set
Ejercicio:    Eliminando valores inmutables
Descripción:  Ejercicio de clase numeros lideres.

Autor:        Diego Roberto Carpio Flamenco
Fecha:        2025-06-02
Estado:       [ En progreso | Terminado ]
'''

import os

os.system('cls')

entrada = (input('Ingresa una lista de numeros: '))

numeros = [int(n) for n in entrada.split()]
lideres = []

for i in range(len(numeros) - 1):
        if not any(n > numeros[i] for n in numeros[i + 1:]):
            lideres.append(numeros[i])
print(" ".join(str(n) for n in lideres))