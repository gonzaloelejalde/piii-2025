import numpy as np
import matplotlib.pyplot as plt

from ejercicio1 import portadora  # nuestro módulo creado antes

# --- Parte 1: Generar y modificar coseno ---
n = np.arange(50)  # primeros 50 valores
y = np.cos(n)

# Reemplazar negativos con 0
y_mod = np.array([0 if val < 0 else val for val in y])

print("Valores originales:", y)
print("Valores modificados:", y_mod)

# --- Parte 2: Graficar secuencia senoidal con 12 muestras por ciclo ---
# Esto implica una frecuencia de 1 ciclo cada 12 muestras
muestras_por_ciclo = 12
duracion_ciclos = 3  # cuántos ciclos mostrar
t = np.arange(muestras_por_ciclo * duracion_ciclos)
senal = np.sin(2 * np.pi * t / muestras_por_ciclo)

plt.figure(figsize=(8, 3))
plt.stem(t, senal)
plt.title("Secuencia senoidal con 12 muestras por ciclo")
plt.xlabel("Muestra")
plt.ylabel("Amplitud")
plt.grid(True)
plt.show()

# --- Parte 3: Usar el módulo portadora para graficar ---
# Por ejemplo, mostrar la portadora equivalente
portadora.portadora(freq=1, duration=duracion_ciclos, sample_rate=muestras_por_ciclo)
