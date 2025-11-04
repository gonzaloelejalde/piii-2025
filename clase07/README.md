# Análisis de Señales: Pulsaciones (Beats) y Filtros (Clase 07)

Este repositorio contiene el notebook de Jupyter (`clase07.ipynb`) que explora dos conceptos clave del procesamiento de señales: el fenómeno de las pulsaciones acústicas (beats) y la generación de un filtro transmisor de Coseno Alzado (Raised Cosine).

## Contenido del Notebook

El notebook está dividido en dos ejercicios principales:

### Ejercicio 15: Pulsaciones (Beats)

Esta sección analiza la generación y percepción de pulsaciones acústicas mediante la suma y multiplicación de señales senoidales.

#### 1. Generación de Beats por Suma
El primer script demuestra cómo se generan las pulsaciones sumando dos tonos con frecuencias muy cercanas.
* **Proceso:** Se generan dos señales cosenoidales (`signal1` y `signal2`) con frecuencias `f1 = 440 Hz` y `f2 = 442 Hz`.
* **Señal de Pulsación:** Las señales se suman: `beats = signal1 + signal2`.
* **Salida:** Se grafica un fragmento de la señal de beats resultante en el dominio del tiempo y se genera un audio reproducible (`IPython.display.Audio`) donde se puede escuchar el "latido" acústico.

#### 2. Análisis Teórico de Pulsaciones
El notebook incluye un análisis en Markdown sobre el fenómeno:
* **Fórmula:** La frecuencia de la pulsación (el "latido" del volumen) se calcula como: `f_beats = |f1 - f2|`.
* **Percepción:**
    * **Frecuencias Cercanas:** Se percibe un solo tono cuyo volumen sube y baja lentamente (latido acústico).
    * **Frecuencias Lejanas:** La fluctuación de volumen es tan rápida que se percibe como un cambio en el timbre o como dos tonos distintos (disonancia).

#### 3. Multiplicación de Señales (Modulación AM)
Esta parte analiza qué sucede si las dos señales se multiplican en lugar de sumarse.
* **Proceso:** Se multiplican las dos señales (`s1 * s2`).
* **Análisis:** Se identifica que esta operación es una **Modulación de Amplitud de Doble Banda Lateral con Portadora Suprimida (AM-DSB-SC)**.
* **Salida:**
    * Se grafica la señal resultante en el tiempo.
    * Se calcula y grafica el espectro de frecuencia (FFT), mostrando los picos en las frecuencias de suma (`f1 + f2`) y diferencia (`|f1 - f2|`), confirmando la teoría de la AM-DSB-SC.

### Ejercicio 16: Filtro Transmisor (Coseno Alzado)

Esta sección implementa y grafica un filtro de Coseno Alzado (Raised Cosine), comúnmente usado en sistemas de telecomunicaciones para conformar pulsos.

* **Propósito:** Generar la respuesta al impulso `g[n]` de un filtro de Coseno Alzado.
* **Parámetros:**
    * `fB = 32e9` (32 GBaudios, velocidad de símbolos).
    * `M = 8` (Factor de sobremuestreo).
    * `alpha = 0.1` (Factor de roll-off).
    * `L = 20` (Define la longitud del filtro).
* **Fórmula:** Se implementa la fórmula estándar del pulso de Coseno Alzado:
    `gn = np.sinc(t / T) * np.cos(np.pi * alpha * t / T) / (1 - 4 * alpha**2 * t**2 / T**2)`.
* **Visualización:**
    * Se genera un primer gráfico (`stem`) del pulso completo `g[n]`.
    * Se genera un segundo gráfico con un zoom en la zona central del pulso, mejorando las etiquetas de los ejes para mostrar múltiplos del tiempo de símbolo `T` y añadiendo anotaciones con los valores de `M` y `alpha`.

## Requisitos

Para ejecutar este notebook, necesitarás las siguientes bibliotecas de Python:
* `numpy`
* `matplotlib`
* `IPython` (específicamente `IPython.display.Audio`)

## Cómo Usar

1.  Abre el archivo `clase07.ipynb` en un entorno compatible con Jupyter (como Google Colab o Jupyter Notebook local).
2.  Ejecuta las celdas de código en orden.
3.  Observa las gráficas generadas y escucha los audios producidos en el Ejercicio 15.
4.  Analiza las gráficas del pulso de Coseno Alzado en el Ejercicio 16.
