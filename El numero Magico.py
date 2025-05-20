'''
Clase:        Bloque condicional
Tema:         Bloque condicional
Ejercicio:    Numero magico
Descripción:  Ingresar un numero y que te diga el programa si cumple las condiciones para que sea un numero magico.

Autor:        DiegoRoberto Carpio Flamenco
Fecha:        2025-05-20
Estado:       [ En progreso | Terminado ]
'''


import os

os.system('cls')

number = int(input('Pruebas del numero: '))

if number % 7 == 0:
    if number % 5 != 0:
        print('Numero magico')
    elif number % 5 == 0:
        print('Numero no magico')
elif number % 7 != 0:
    print('Numero no magico')