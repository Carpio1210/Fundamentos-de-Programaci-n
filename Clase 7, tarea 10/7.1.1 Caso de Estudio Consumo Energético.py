'''
Clase:        Clase 10
Ejercicio:    Numpy
Descripción:  Ejercicio de caso de consumo electrico, primera practica Numpy.

Autor:        Diego Roberto Carpio Flamenco
Fecha:        2025-06-02
Estado:       [Terminado]
'''

import os

os.system('cls')

import numpy as np

consumo = np.array([
    [12.5, 13.2, 11.9, 14.0, 13.5, 15.0, 14.3],
    [10.1, 10.5, 10.0, 11.2, 11.5, 12.0, 11.8],
    [14.0, 14.2, 13.9, 15.5, 15.1, 16.0, 15.8],
    [9.0, 9.2, 8.9, 9.5, 9.8, 10.0, 9.7],
    [16.2, 16.5, 16.0, 17.1, 17.4, 18.0, 17.8],
    [11.0, 11.3, 11.1, 12.0, 12.4, 12.8, 12.5],
    [13.5, 13.8, 13.2, 14.1, 14.6, 15.0, 14.9],
    [10.8, 11.0, 10.6, 11.5, 11.8, 12.2, 12.0],
    [15.1, 15.5, 15.0, 16.0, 16.4, 17.0, 16.7],
    [8.5, 8.7, 8.4, 9.0, 9.2, 9.5, 9.3],
])

# Exploración inicial de los datos
print("Dimensiones:", consumo.ndim)
print("Forma:", consumo.shape)
print("Tipo de datos:", consumo.dtype)
print("Consumo primer hogar:", consumo[0])
print("Consumo el miércoles (día 3):", consumo[:, 2])

promedio_por_hogar = np.mean(consumo, axis=1)

promedio_por_dia = np.mean(consumo, axis=0)

total_consumo = np.sum(consumo)

print(promedio_por_hogar)
print(promedio_por_dia)
print(total_consumo)

# Máximo por hogar
maximos = np.max(consumo, axis=1)

# Mínimo por día
minimos = np.min(consumo, axis=0)

# Desviación estándar global
desviacion = np.std(consumo)

print(maximos)
print(minimos)
print(desviacion)

# Suma por hogar (semana)
consumo_total_hogar = np.sum(consumo, axis=1)

# Índice del hogar con mayor consumo
hogar_mayor_consumo = np.max(consumo_total_hogar)

# Índice del hogar con mejor consumo
hogar_mas_eficiente = np.argmin(consumo_total_hogar)

print(consumo_total_hogar)
print(hogar_mayor_consumo)
print(hogar_mas_eficiente)


# Suma por hogar (semana)
consumo_total_hogar = np.sum(consumo, axis=1)
print(f"Consumo total de cada hogar durante la semana: {consumo_total_hogar}")

# Compara cada hogar con un valor mayor a 100
altos = consumo_total_hogar > 100
# Filtrando hogares que cumplen la condición:
consumo_mayor_100 = np.where(altos)[0]

print(f"IDs de hogares con consumo mayor a 100: {consumo_mayor_100}")


# Aplicando normalización MinMax al conjunto de datos
consumo_normalizado = (consumo - consumo.min()) / (consumo.max() - consumo.min())

# Resultado
print(f'{consumo_normalizado}\n')

#5. Cuestionario de trabajo:
print('5. Cuestionario de trabajo:\n')
#Instrucciones:
#Responde cada pregunta escribiendo el código necesario para obtener la respuesta.
#Agrega también comentarios o respuestas escritas cuando se solicite explicación.
#No borres las secciones anteriores del archivo python desarrollado para esta guía de trabajo, simplemente agrega tus respuestas al final.
#Puedes auxiliarte de tu herramienta IA preferida, pero recuerda las buenas prácticas para su uso. Somos responsables de comprender el resultado.
#Cuestionario.
#1. ¿Cuál es el consumo del hogar 5 el viernes (día 5)?
print('1. ¿Cuál es el consumo del hogar 5 el viernes (día 5)?\n')
consumo_hogar_5_viernes = consumo[4,4]
print(f'El hogar numero 5 consumio {consumo_hogar_5_viernes} KW\n')

#2. Usando indexación, muestra el consumo de los últimos 3 hogares el domingo.
print('2. Usando indexación, muestra el consumo de los últimos 3 hogares el domingo.\n')
consumo_ultimo_3_hogares_domingo = consumo[-3: , 6]
print(f'Los ultimos 3 hogares consumieron {consumo_ultimo_3_hogares_domingo}\n')

#3. Calcula el promedio de consumo los fines de semana (sábado y domingo, columnas 5 y 6).
print('#3. Calcula el promedio de consumo los fines de semana (sábado y domingo, columnas 5 y 6).\n')
average_fin = np.mean(consumo[:, [5,6]])
print(f'El promedio de consumo de los fin de semanas es: {average_fin} KW\n')

#4. ¿Qué día de la semana tiene la mayor desviación estándar entre hogares? Explica qué indica esto.
print('4. ¿Qué día de la semana tiene la mayor desviación estándar entre hogares? Explica qué indica esto.\n')
mayor_desviacion = np.std(consumo, axis=0)
gran_desviacion = np.max(mayor_desviacion)
dia = np.argmax(mayor_desviacion)

print(f'El dia de mayor desviacion es el {dia}, esto indica que el dia {dia}, es el cual las personas mas consumen energia electrica.\n')
print(f'La desviacion es: {gran_desviacion} \n')

#5. Identifica los 3 hogares con menor consumo total durante la semana. Muestra sus índices y valores.
print('5. Identifica los 3 hogares con menor consumo total durante la semana. Muestra sus índices y valores.\n')
menor_consumo = np.sum(consumo, axis=1)
menores_consumidores = np.argsort(menor_consumo)[:3]
menores = menor_consumo[menores_consumidores]

print(f'Indice de los 3 hogares con menor consumo total de toda la semana, {menores_consumidores}\n')
print(f'Valores del consumo total: {menores}\n')

#6. Si el hogar 3 aumenta su consumo en un 10% cada día, ¿cuál sería su nuevo consumo total semanal?
print('6. Si el hogar 3 aumenta su consumo en un 10 prociento cada día, ¿cuál sería su nuevo consumo total semanal?\n')
consumo_hogar_tres = consumo[2]
consumo_aumentado = consumo_hogar_tres * 1.1
total = np.sum(consumo_aumentado)

print(f'Su nuevo consumo total seria: {total}')