'''
Clase:        Clase 12
Ejercicio:    Recursividad
Descripción:  Ejercicio de Recursividad
#
#Autor:        Diego Roberto Carpio Flamenco
#Fecha:        2025-06-12
#Estado:       [Terminado]
#'''
#
import os
import time
os.system('cls')
#
#n = 10
#
#def cuenta_regresiva_iterativa(n):
#    for i in range(n, 0, -1):
#        print(i, end='...')
#        #time.sleep(0.5)
#    print('¡Despeguen!')
#
#cuenta_regresiva_iterativa(n)
#
##print(cuenta_regresiva_iterativa(n))
#
#
#def cuenta_regresiva_recursiva(n):
#    if n <= 0:
#        print('¡Despeguen!')
#    else: 
#        print(n, end='...')
#        #time.sleep(0.5)
#        cuenta_regresiva_recursiva(n - 1)
#
#cuenta_regresiva_recursiva(n)
#
#
#
##Crea dos funciones (oterativas y recursivas) que genere y resuelva:
#
#El abecedario

def generar_alfabeto_iterativo():
    alfabeto = ''
    letra = 'a'
    for i in range(ord('a'), ord('z') +1, 1):
        alfabeto += (chr(i)) + ', '
    alfabeto = alfabeto.rstrip(', ')
    return alfabeto
print(generar_alfabeto_iterativo())

def generar_alfabeto_iterativo_recursividad(letra):
    if letra == 'z':
        return 'z'
    else:
        return letra + ', ' + generar_alfabeto_iterativo_recursividad(chr(ord(letra) + 1))

print(generar_alfabeto_iterativo_recursividad('a'))

# Crea una funcion para calcular el factorial de un numero:

def factorial(n):
    if n == 0:
        return 1
    else: 
        return n * factorial (n - 1)
    
print(factorial(5))

# Crear una funcion que cuente recursivamente los vecinos en una matriz binaria:
#Condicion: contar vecinos que se encuentren horizontal y verticalmente:

#def matrices():