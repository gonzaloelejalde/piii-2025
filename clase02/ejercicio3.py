import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la señal
f = 1000       # Frecuencia de la señal (Hz)
A = 5          # Amplitud máxima (V)
fs = 50000     # Frecuencia de muestreo (Hz)
t_total = 0.01 # Duración: 10 ms

# Señal continua (muchos puntos para que se vea suave)
t_cont = np.linspace(0, t_total, 1000)
y_cont = A * np.sin(2 * np.pi * f * t_cont)

# Señal muestreada
t_samples = np.arange(0, t_total, 1/fs)
y_samples = A * np.sin(2 * np.pi * f * t_samples)

# Primeras 50 muestras
n_samples = 50
t_first = t_samples[:n_samples]
y_first = y_samples[:n_samples]

# Cuantificación a 12 bits
bits = 12
levels = 2**bits
# Escalado a [0, levels-1]
y_quant = np.round((y_first + A) * (levels - 1) / (2*A))
# Volver a escala original
y_quant = (y_quant / (levels - 1)) * (2*A) - A

# Gráficas
plt.figure(figsize=(10, 6))

# Señal continua
plt.subplot(3, 1, 1)
plt.plot(t_cont * 1000, y_cont, label="Señal continua")
plt.title("Señal continua senoidal (1 kHz, ±5V)")
plt.xlabel("Tiempo (ms)")
plt.ylabel("Amplitud (V)")
plt.grid(True)
plt.legend()

# Primeras 50 muestras sin cuantificar
plt.subplot(3, 1, 2)
plt.stem(t_first * 1000, y_first, basefmt=" ", label="Muestras sin cuantificar")
plt.title("Primeras 50 muestras sin cuantificar")
plt.xlabel("Tiempo (ms)")
plt.ylabel("Amplitud (V)")
plt.grid(True)
plt.legend()

# Primeras 50 muestras cuantificadas
plt.subplot(3, 1, 3)
plt.stem(t_first * 1000, y_quant, basefmt=" ", label="Muestras cuantificadas (12 bits)")
plt.title("Primeras 50 muestras cuantificadas (ADC 12 bits)")
plt.xlabel("Tiempo (ms)")
plt.ylabel("Amplitud (V)")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
