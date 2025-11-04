# Filtro Transmisor y Generador de Símbolos (Clase 09)

Este repositorio contiene el notebook de Jupyter (`clase09.ipynb`) que demuestra el diseño de un filtro transmisor, la generación de símbolos PAM2 y PAM4, la simulación de una señal transmitida y la generación de un diagrama de ojo.

## Contenido del Notebook

El notebook está dividido en las siguientes secciones principales:

### 1. Filtro Transmisor (Coseno Alzado)

Esta sección implementa y grafica un filtro de Coseno Alzado (Raised Cosine).

* **Parámetros:**
    * `fB = 32e9` (Velocidad de símbolos o baud rate).
    * `M = 8` (Factor de sobremuestreo).
    * `alpha = 0.1` (Factor de roll-off).
    * `L = 20` (Define la longitud del filtro).
* **Proceso:** Se calcula la respuesta al impulso `g[n]` del filtro usando la fórmula estándar del Coseno Alzado:
    `gn = np.sinc( t / T ) * np.cos( np.pi * alpha * t / T ) / ( 1 - 4 * alpha**2 * t**2 / T**2 )`.
* **Visualización:** Se grafica la respuesta al impulso `g[n]` usando `ax.stem`.

### 2. Ejercicio 17: Generación de Símbolos (PAM2 y PAM4)

Esta sección genera secuencias aleatorias de símbolos para modulaciones PAM2 y PAM4, utilizando una semilla (seed) basada en `datetime.datetime.now().timestamp()` para asegurar resultados diferentes en cada ejecución.

* **Generación PAM2:**
    * El notebook implementa la generación de 1000 símbolos PAM2 (niveles -1 y +1) usando `randrange( -1, 2, 2 )`.
    * También incluye una explicación detallada (marcada como Ejercicio 17) que describe el método alternativo `np.random.choice([-1, 1], size=1000)`.
* **Generación PAM4:**
    * Se generan 1000 símbolos PAM4 utilizando los niveles `[-3, -1, 1, 3]`.
    * Se utiliza `np.random.choice(niveles_PAM4, size=1000)`.

### 3. Ejercicio 18: Señal Transmitida (PAM2)

Este ejercicio simula la transmisión de la señal PAM2 generada a través del filtro Coseno Alzado.

* **Sobremuestreo:** Se crea una nueva señal `xn` insertando `M-1` ceros entre cada símbolo PAM2 (`xn[ i * M ] = simbolos_PAM2[ i ]`).
* **Visualización (Chupetines):** Se grafica la señal sobremuestreada `xn` (usando `ax.stem`) para mostrar los impulsos en los instantes de símbolo.
* **Convolución:** Se filtra la señal sobremuestreada `xn` haciéndola pasar por el filtro `gn` mediante la convolución: `sn = convolve( xn, gn )`.
* **Visualización (Señal Transmitida):** Se grafica la señal filtrada resultante `sn` (usando `ax.plot`).

### 4. Diagrama de Ojo (PAM4)

La sección final genera un diagrama de ojo para una señal PAM4 transmitida.

* **Proceso:** De manera similar al Ejercicio 18, se generan símbolos PAM4, se realiza el sobremuestreo (`xn`) y se convolucionan con el filtro `gn` para obtener la señal `sn`.
* **Generación del Diagrama:** El script itera sobre la señal transmitida `sn`, tomando segmentos de longitud `M` (con un delay `d=4` para centrar).
* **Visualización:** Todos los segmentos se superponen en una misma gráfica (`plt.plot(np.arange(-3, 4), sn_p[1:8])`) para formar el "Diagrama de ojo – PAM4".

## Requisitos

Para ejecutar este notebook, necesitarás las siguientes bibliotecas de Python:
* `numpy`
* `matplotlib.pyplot`
* `random` (para `randrange` y `seed`)
* `datetime`
* `scipy.signal` (para `convolve`)
