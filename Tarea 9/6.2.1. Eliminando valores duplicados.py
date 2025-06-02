'''
Clase:        Clase 9
Tema:         Set
Ejercicio:    Eliminando valores inmutables
Descripción:  Ejercicio de clase.

Autor:        Diego Roberto Carpio Flamenco
Fecha:        2025-05-30
Estado:       [ En progreso | Terminado ]
'''


import os

os.system('cls')

entrada = (input('Ingresa una lista de numeros: '))

#lista = [int(x) for x in entrada.split (' ')]
#
#print(lista)
#
#numero = int(''.join(map(str, lista)))
#
#numero = set(str(numero))
#
#print((numero))

lista = entrada.split(' ')

no_repetido = []

for n in lista:
    if n not in no_repetido:
        no_repetido.append(n)
no_repetido =  " ".join(no_repetido)
print(no_repetido)