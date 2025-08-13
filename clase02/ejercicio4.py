import numpy as np
import sounddevice as sd

def generador_de_tono(frecuencia, duracion, sample_rate, A=1):
    n = np.linspace(0, duracion, int(sample_rate * duracion), endpoint=False)
    return A * np.sin(2 * np.pi * frecuencia * n)

def reproducir_audio(data, sample_rate):
    sd.play(data, sample_rate)
    sd.wait()  # Espera hasta que termine la reproducción

sample_rate = 44100
duracion_nota = 0.5  # segundos

nota_base = 440  # La

# Crear lista de frecuencias para las notas (semitonos)
notas = [nota_base * 2 ** (n / 12) for n in range(13)]

# Índices para escala pentatónica menor de La
index_pentatonica_menor = [0, 3, 5, 7, 10, 12]

# Generar tonos
escala = [generador_de_tono(notas[i], duracion_nota, sample_rate) for i in index_pentatonica_menor]

# Concatenar notas en una sola señal
secuencia = np.concatenate(escala)

# Reproducir
reproducir_audio(secuencia, sample_rate)
