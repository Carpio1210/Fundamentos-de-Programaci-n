'''
Clase:        Clase 5
Ejercicio:    Bucles
Descripción:  Se utilizan bucles para encontrar un numero secreto sino se daran pistas hasta encontrarlo.

Autor:        Diego Roberto Carpio Flamenco
Fecha:        2025-05-30
Estado:       [ En progreso | Terminado ]
'''

import os

os.system('cls')

import random

number = random.randint(1, 100) 

while True:
    try:
        enter = int(input('Ingresa un numero entre el 1 y 100: '))
        if number == enter:
            print(f'¡Felicidades! Has adivinado el numero secreto: {enter}')
            break
        elif number > enter:
            print('El numero secreto es mayor')
        elif enter > number:
            print('El numero secreto es menor')
    except ValueError:
        print('Intente un numero entero. ')