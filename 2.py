import matplotlib.pyplot as plt
import numpy as np

# Datos del piso 4
distancia_piso4 = [1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4, 4.8, 5.6, 6.4, 7.2, 8, 8.8, 9.6, 10.4, 11.2, 12, 12.8, 13.6, 14.4, 15.2, 16, 16.8, 17.6, 18.4, 19.2]
path_loss_piso4 = [66.2, 66.1, 67.1, 67, 68, 68.2, 68, 70.7, 71.3, 71, 71.3, 71.4, 72.4, 72, 74, 75.2, 74.7, 74.6, 74.2, 74.6, 76.1, 75.8, 76.4, 76.3, 76.6, 76.2, 76, 77.5, 77.8, 78, 78.1, 76.5, 74, 73.8, 72.2, 71.8, 72.7, 71.9, 75.9, 77.3, 77.7, 79, 81.1, 81, 81.6, 81.8, 79.8, 79.4, 81, 82.3]

# Datos del piso 5
distancia_piso5 = [1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4, 4.8, 5.6, 6.4, 7.2, 8, 8.8, 9.6, 10.4, 11.2, 12, 12.8, 13.6, 14.4, 15.2, 16, 16.8, 17.6, 18.4, 19.2]
path_loss_piso5 = [64, 65, 65.5, 66.3, 66.6, 71, 69.7, 65.8, 66.4, 69.9, 67.7, 69.9, 69.6, 71.1, 69.5, 68.7, 65.8, 76.2, 72.9, 75.1, 77.8, 78.1, 80.8, 78.3, 77.3, 79.6, 75.4, 77.6, 81.3, 77.7, 78, 76.5, 75.7, 77.5, 82.1, 84.2, 74.8, 71.7, 80.3, 79.4, 76.5, 77.7, 77.3, 77.3, 82.3, 87.3, 81.8, 76.6, 81.3, 81.1]

# Crear gráfica
plt.figure(figsize=(10, 6))

# Plotear datos
plt.scatter(distancia_piso4, path_loss_piso4, label='Piso 4')
plt.scatter(distancia_piso5, path_loss_piso5, label='Piso 5')

# Calcular y plotear regresiones lineales
coef_piso4 = np.polyfit(distancia_piso4, path_loss_piso4, 1)
poly1d_fn_piso4 = np.poly1d(coef_piso4)
plt.plot(distancia_piso4, poly1d_fn_piso4(distancia_piso4), color='blue')

coef_piso5 = np.polyfit(distancia_piso5, path_loss_piso5, 1)
poly1d_fn_piso5 = np.poly1d(coef_piso5) 
plt.plot(distancia_piso5, poly1d_fn_piso5(distancia_piso5), color='orange')

# Personalizar gráfica
plt.title('Comparación de Path Loss entre Piso 4 y Piso 5')
plt.xlabel('Distancia (m)')
plt.ylabel('Path Loss (dB)')
plt.legend()
plt.grid(True)
# Mostrar gráfica
plt.show()
