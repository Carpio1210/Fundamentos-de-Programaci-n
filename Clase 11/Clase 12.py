import os

os.system('cls')

def encontrar_entrada(mapa):
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if mapa[i][j] == 'S':
                return i, j
            return None, None
def encontrar(mapa, i, j):
    if i < 0 or i >= len(mapa) or j < 0 or j >= len(mapa):
        return False
    
    celda = mapa[i][j]
    if celda == 'X' or celda == 'v':
        return False

    if celda == 'A':
        return True

    mapa[i][j] == 'V' 

    
mapa = [
    ['S', '.', '.', 'X', '.', '.', '.', 'X', '.', '.', '.', '.'],
    ['X', 'X', '.', 'X', '.', 'X', '.', '.', 'X', 'X', '.', '.'],
    ['.', '.', '.', '.', '?', '.', 'X', '.', '.', '.', '?', '.'],
    ['.', 'X', 'X', '.', 'X', '.', 'X', 'X', '.', 'X', '.', '.'],
    ['.', '.', '?', '.', '.', '.', '.', '.', '.', '?', 'X', '.'],
    ['X', '.', 'X', 'X', '.', 'X', 'X', '.', 'X', '.', '.', '.'],
    ['.', '.', '.', '.', '?', '.', '.', '?', '.', 'X', '.', '.'],
    ['X', 'X', '.', 'X', '.', 'X', '.', 'X', '.', '.', 'X', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', 'X', '?', '.', '.'],
    ['X', '.', 'X', '.', '?', '.', 'X', '.', '.', '.', '.', 'A']
]
print(encontrar_entrada(mapa))