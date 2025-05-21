<<<<<<< HEAD
'''
Clase:        Bloque condicional
Tema:         Bloque condicional
Ejercicio:    Automatizacion de la propina
Descripción:  El codigo busca automatizar la propina con respecto al monto y al porcentaje que desee el usario.

Autor:        DiegoRoberto Carpio Flamenco
Fecha:        2025-05-20
Estado:       [ En progreso | Terminado ]
'''


import os

os.system('cls')

cuenta = int(input('Ingresa la cuenta: '))
porcentaje = int(input('Ingresa el porcentaje de propina (10%, 15%, 20%): '))
propina = porcentaje/100
propina_total = cuenta*propina
cuenta_total = cuenta + propina_total
=======
'''
Clase:        Bloque condicional
Tema:         Bloque condicional
Ejercicio:    Automatizacion de la propina
Descripción:  El codigo busca automatizar la propina con respecto al monto y al porcentaje que desee el usario.

Autor:        DiegoRoberto Carpio Flamenco
Fecha:        2025-05-20
Estado:       [ En progreso | Terminado ]
'''


import os

os.system('cls')

cuenta = int(input('Ingresa la cuenta: '))
porcentaje = int(input('Ingresa el porcentaje de propina (10%, 15%, 20%): '))
propina = porcentaje/100
propina_total = cuenta*propina
cuenta_total = cuenta + propina_total
>>>>>>> c73697408dbc48848c3f69ee04f4a1c1facdc6a8
print(cuenta_total)