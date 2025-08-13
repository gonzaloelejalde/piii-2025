import numpy as np
import matplotlib.pyplot as plt

def amplitud(carrier_freq=10, mod_freq=1, mod_index=0.5, duration=1, sample_rate=1000):
    """
    Grafica una señal modulada en amplitud (AM).
    
    Parámetros:
    - carrier_freq : Frecuencia de la portadora (Hz)
    - mod_freq     : Frecuencia de la moduladora (Hz)
    - mod_index    : Índice de modulación (0 a 1 típico)
    - duration     : Duración de la señal (s)
    - sample_rate  : Frecuencia de muestreo (Hz)
    """
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    mod_signal = np.sin(2 * np.pi * mod_freq * t)          # moduladora
    carrier = np.sin(2 * np.pi * carrier_freq * t)         # portadora
    am_signal = (1 + mod_index * mod_signal) * carrier     # señal AM

    plt.figure(figsize=(10, 6))

    plt.subplot(3, 1, 1)
    plt.plot(t, mod_signal, 'g')
    plt.title("Señal moduladora")
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Amplitud")
    plt.grid(True)

    plt.subplot(3, 1, 2)
    plt.plot(t, carrier, 'b')
    plt.title("Portadora")
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Amplitud")
    plt.grid(True)

    plt.subplot(3, 1, 3)
    plt.plot(t, am_signal, 'r')
    plt.title(f"Señal AM (Índice = {mod_index})")
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Amplitud")
    plt.grid(True)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    amplitud()
