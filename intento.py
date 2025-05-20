import os
os.system('cls')

import random
import matplotlib.pyplot as plt

# Parámetros de la simulación
neutrones_iniciales = 1               # Empezamos con 1 neutrón
probabilidad_fision = 0.7             # Probabilidad de que un neutrón cause fisión
neutrones_por_fision = (2, 3)         # Cada fisión libera de 2 a 3 neutrones
generaciones = 10                     # Número de generaciones a simular

# Para almacenar los resultados
historial_neutrones = []

# Neutrones actuales
neutrones = neutrones_iniciales

# Simulación de la reacción en cadena
for gen in range(generaciones):
    nuevos_neutrones = 0
    for _ in range(neutrones):
        if random.random() < probabilidad_fision:
            # Se produce una fisión
            nuevos_neutrones += random.randint(*neutrones_por_fision)
    historial_neutrones.append(nuevos_neutrones)
    print(f"Generación {gen + 1}: {nuevos_neutrones} neutrones")
    neutrones = nuevos_neutrones

# Gráfica de resultados
plt.figure(figsize=(10, 6))
plt.plot(range(1, generaciones + 1), historial_neutrones, marker='o', linestyle='-')
plt.title("Simulación de Fisión Nuclear del Uranio-235")
plt.xlabel("Generación")
plt.ylabel("Cantidad de Neutrones")
plt.grid(True)
plt.show()