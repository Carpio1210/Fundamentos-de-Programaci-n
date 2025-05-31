'''
Clase:        Clase 5
Ejercicio:    Bucles
Descripción:  Se utilizan bucles para encontrar la suma de valores de 2 digitos.

Autor:        Diego Roberto Carpio Flamenco
Fecha:        2025-05-30
Estado:       [ En progreso | Terminado ]
'''
import os

os.system('cls')
while True:
        try:
                numero = int(input('Ingresa un numero: '))
                if numero <= 1  or numero >= 10**9:
                        print('Ingresa un numero valido: ')
                else: 
                        break
        except ValueError:
                print('Ingrese un numero Valido. ')
        
print(f'\nProceso de reduccion para {numero}:')

while numero > 9:
    primero = numero
    otro = 0
    while numero > 0:
        digito = numero % 10
        numero = numero // 10
        otro += digito
    print(f'{primero} = {otro}')
    numero = otro

print(f'El resultado final es: {numero}')