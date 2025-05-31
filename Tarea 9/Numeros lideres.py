'''
Clase:        Clase 9
Tema:         Set
Ejercicio:    Eliminando valores inmutables
Descripción:  Ejercicio de clase numeros lideres.

Autor:        Diego Roberto Carpio Flamenco
Fecha:        2025-05-31
Estado:       [ En progreso | Terminado ]
'''


import os

os.system('cls')

entrada = (input('Ingresa una lista de numeros: '))

lista = entrada.split(' ')

no_repetido = []

for n in lista:
    if n not in no_repetido:
        no_repetido.append(n)

no_repetido = [int(n) for n in no_repetido]

def ordenar(no_repetido):
    if len(no_repetido) == 0:
        return []
    else:
        mayor = max(no_repetido)
        no_repetido.remove(mayor)
        return [mayor] + ordenar(no_repetido)

ordenar = ordenar(no_repetido)

print(" ".join(str(n) for n in ordenar))