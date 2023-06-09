import numpy as np
import matplotlib.pyplot as plt

# Datos de distancia
distancia = [1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4, 4.8, 5.6, 6.4, 7.2, 8, 8.8, 9.6, 10.4, 11.2, 12, 12.8, 13.6, 14.4, 15.2, 16, 16.8, 17.6, 18.4, 19.2]
path_loss = [64, 65, 65.5, 66.3, 66.6, 71, 69.7, 65.8, 66.4, 69.9, 67.7, 69.9, 69.6, 71.1, 69.5, 68.7, 65.8, 76.2, 72.9, 75.1, 77.8, 78.1, 80.8, 78.3, 77.3, 79.6, 75.4, 77.6, 81.3, 77.7, 78, 76.5, 75.7, 77.5, 82.1, 84.2, 74.8, 71.7, 80.3, 79.4, 76.5, 77.7, 77.3, 77.3, 82.3, 87.3, 81.8, 76.6, 81.3, 81.1]

# Cálculo de la regresión lineal
coeficientes = np.polyfit(distancia, path_loss, 1)
pendiente = coeficientes[0]
interseccion = coeficientes[1]

# Generación de los valores estimados de path loss
path_loss_estimado = np.polyval(coeficientes, distancia)

# Gráfico de distancia vs. path loss
plt.scatter(distancia, path_loss, color='red', label='Datos')
# plt.plot(distancia, path_loss_estimado, color='blue', label='Regresión Lineal')
plt.xlabel('Distancia (m)')
plt.ylabel('Path Loss')
plt.legend()
plt.grid(True)
plt.show()

# Imprimir los coeficientes de la regresión lineal
print('Pendiente: {:.4f}'.format(pendiente))
print('Intersección: {:.4f}'.format(interseccion))
