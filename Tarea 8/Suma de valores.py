'''
Clase:        Clase 5
Ejercicio:    Bucles
Descripción:  Se utilizan bucles para sumar todos los valores.

Autor:        Diego Roberto Carpio Flamenco
Fecha:        2025-05-31
Estado:       [ En progreso | Terminado ]
'''

import os

os.system('cls')

entrada = input('Ingresa una lista de numeros: ')

lista = entrada.split(' ')
suma = 0

for n in lista:
        suma += int(n)
        print(f'La suma de por termino es: {suma}')

print(f'Suma total: {suma}')