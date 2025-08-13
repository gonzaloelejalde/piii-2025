import numpy as np
import matplotlib.pyplot as plt

def portadora(freq=10, duration=1, sample_rate=1000):
    """
    Grafica una portadora sinusoidal.
    
    Parámetros:
    - freq        : Frecuencia de la portadora (Hz)
    - duration    : Duración de la señal (s)
    - sample_rate : Frecuencia de muestreo (Hz)
    """
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    carrier = np.sin(2 * np.pi * freq * t)

    plt.figure(figsize=(8, 3))
    plt.plot(t, carrier, 'b')
    plt.title(f"Portadora ({freq} Hz)")
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Amplitud")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    portadora()
