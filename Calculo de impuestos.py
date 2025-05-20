'''
Clase:        Bloque condicional
Tema:         Bloque condicional
Ejercicio:    Calculo de impuestos
Descripción:  El codigo verifica ingresos y devuelve el monto de impuestos que hay que pagar.

Autor:        DiegoRoberto Carpio Flamenco
Fecha:        2025-05-20
Estado:       [ En progreso | Terminado ]
'''

import os
os.system('cls')

consumo = float(input('Total: '))

if consumo <= 100:
    print(consumo)
    print('Sin impuestos')
elif 101 <= consumo <= 200:
    con = (consumo) * 0.5 
    print(con)
    consumo_total = consumo + con
    print(f'Tus impuestos son: {consumo_total}')
elif consumo > 201:
    cons = (consumo) * 0.7
    print(cons)
    consumo_total = consumo + cons
    print(f'Tus impuestos son: {consumo_total}')