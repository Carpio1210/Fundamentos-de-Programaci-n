'''
Clase:        Clase 11
Ejercicio:    Numpy
Descripción:  Ejercicio de caso de consumo electrico, primera practica Numpy.

Autor:        Diego Roberto Carpio Flamenco
Fecha:        2025-06-02
Estado:       [Terminado]
'''
import os

import time

os.system('cls')

def load_file():
    filepath = input('Enter the path of the file: ')
    file = open(filepath, 'r', encoding='utf-8')
    lines = file.readlines()
    file.close()

    return lines

my_file = load_file()
print(my_file) #c:/Proyectos/Fundamentos-de-Programaci-n/Clase 8, tarea 11/genesis.txt

def set_enviroment(raw_file):
    env = []
    for line in raw_file:
        line = line.strip()
        env.append([int(c) for c in line])
    return env

def print_env(env):
    for row in env:
        for cell in row:
            if cell == 1:
                print('🟥', end="")
            else:
                print(' ', end='')
        print()

def count_neighboors(env,x,y):
    count = 0
    l1 = [x-1, x, x+1]
    l2 = [y-1, y, y+1]
    for i in l1:
        for j in l2:
            if i == x and j == y:
                continue
            if env[i][j] == 1:
                count += 1
    return count
my_file = load_file()
print(my_file)
env = set_enviroment(my_file)
print_env(env)

for generation in range(25):
    for i in range(1, len(env) -1):
        for j in range(1, len(env[0])-1):
            count = count_neighboors(env, i, j)
            if env[i][j] == 1:
                if count < 2 or count > 3:
                    env[i][j] = 0
                if count == 2 or count == 3:
                    env[i][j] = 1
            else: 
                if count == 3:
                    env[i][j] = 1
                    