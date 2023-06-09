import numpy as np
import matplotlib.pyplot as plt

# Datos
distancia = [1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4, 4.8, 5.6, 6.4, 7.2, 8, 8.8, 9.6, 10.4, 11.2, 12, 12.8, 13.6, 14.4, 15.2, 16, 16.8, 17.6, 18.4, 19.2]
path_loss = [66.2, 66.1, 67.1, 67, 68, 68.2, 68, 70.7, 71.3, 71, 71.3, 71.4, 72.4, 72, 74, 75.2, 74.7, 74.6, 74.2, 74.6, 76.1, 75.8, 76.4, 76.3, 76.6, 76.2, 76, 77.5, 77.8, 78, 78.1, 76.5, 74, 73.8, 72.2, 71.8, 72.7, 71.9, 75.9, 77.3, 77.7, 79, 81.1, 81, 81.6, 81.8, 79.8, 79.4, 81, 82.3]

# Ajuste de la regresión lineal
coeficientes = np.polyfit(distancia, path_loss, 1)
pendiente = coeficientes[0]
intercepto = coeficientes[1]

# Crear el gráfico
plt.plot(distancia, path_loss, marker='o', linestyle='-', color='b')

# Línea de regresión lineal
regresion_lineal = np.polyval(coeficientes, distancia)
plt.plot(distancia, regresion_lineal, linestyle='--', color='r')

# Etiquetas de los ejes
plt.xlabel('Distancia (mt)')
plt.ylabel('Path Loss')

# Título del gráfico
plt.title('Gráfico de Distancia vs. Path Loss con Regresión Lineal')

# Mostrar el gráfico
plt.grid(True)
plt.show()

