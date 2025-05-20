'''
Clase:        Variables, tipos, entradas y salidas
Tema:         Variables, tipos, entradas y salidas
Ejercicio:    Contrasena segura
Descripción:  Encontrar una solucion que brinde una respuesta a una contrasena dada.

Autor:        DiegoRoberto Carpio Flamenco
Fecha:        2025-05-20
Estado:       [ En progreso | Terminado ]
'''

import os
os.system('cls')

password = input('Ingresa contrasena: ')
uper = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
number = ('0123456789')
if len(password) < 8:
    print('Necesitas que la contrasena tenga minimo 8 caracteres')
else:
    mayus = False
    num = False
    if len(password) >= 8:
        for i in password:
            if i in uper: 
                mayus = True
            if i in number:
                num = True
    if mayus and num:
        print(('Contrasena segura'))
    else: 
        print('Contrasena insegura')