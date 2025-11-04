# Análisis de Señales y Audio: Ejercicios de Google Colab

Este repositorio contiene un notebook de Jupyter (`clase06.ipynb`) con una serie de ejercicios prácticos sobre procesamiento de señales y audio. Los ejercicios cubren temas de modulación de amplitud, filtros digitales para reducción de ruido y la generación de ilusiones auditivas.

## Contenido del Notebook

El notebook está dividido en los siguientes ejercicios principales:

### Ejercicio 12: Modulación de Amplitud (AM)

Esta sección simula y visualiza diferentes tipos de Modulación de Amplitud.

#### 1. AM-DSB con Portadora (AM-DSB-FC)
El primer script simula una señal de Modulación de Amplitud de Doble Banda Lateral con Portadora (AM-DSB-FC).
* **Proceso:** Genera una señal de mensaje (senoidal de 200 Hz) y una portadora (senoidal de 5 kHz). La señal modulada se calcula usando la fórmula: `y = (1 + m) * c`.
* **Visualización:** Se grafican la señal de mensaje, la portadora, la señal modulada en el tiempo y el espectro de frecuencia (FFT) de la señal modulada.
* **Análisis:** El notebook incluye una explicación sobre el fenómeno de la **sobremodulación** (cuando el índice de modulación es > 1) y discute las características de la AM con portadora suprimida.

#### 2. Extras: Otras Modulaciones AM
Esta parte implementa y grafica otras variantes de la Modulación de Amplitud:
* **AM-DSB-SC (Doble Banda Lateral sin Portadora):** Generada por la multiplicación directa del mensaje y la portadora (`y = m * c_cos`).
* **AM-SSB-SC (Banda Lateral Única sin Portadora):** Utiliza la transformada de Hilbert (`scipy.signal.hilbert`) para generar una señal analítica y aislar una de las bandas laterales (en este caso, la Banda Lateral Superior o USB).
* **AM-SSB (Banda Lateral Única con Portadora):** Se genera añadiendo la señal de portadora nuevamente a la señal SSB-SC.

### Ejercicio 13: Filtros de Media Móvil (SMA y EMA)

Este ejercicio demuestra el uso de filtros de media móvil para suavizar una señal ruidosa.
* **Señal de Prueba:** Se genera una señal senoidal de 5 Hz a la que se le añade ruido aleatorio (gaussiano).
* **Filtros Implementados:**
    * **Media Móvil Simple (SMA):** Se implementa usando una ecuación recursiva para eficiencia y se prueba con ventanas (W) de 5, 20 y 50 muestras.
    * **Media Móvil Exponencial (EMA):** Se implementa con la fórmula `y[n] = α*x[n] + (1-α)*y[n-1]` y se prueba con valores alfa (α) de 0.6, 0.2 y 0.05.
* **Visualización:** Se comparan las señales filtradas (SMA y EMA) contra la señal ruidosa original, tanto en el dominio del tiempo como en el de la frecuencia (FFT).

### Ejercicio 14: Tono de Shepard (Ilusión Auditiva)

Esta sección (titulada "Código profe") genera la ilusión auditiva del Tono de Shepard, que parece subir (o bajar) infinitamente en tono.
* **Proceso:** El tono se crea superponiendo varias ondas senoidales (6 en el ejemplo) separadas por octavas. La amplitud de cada tono se modula con una envolvente sinusoidal, haciendo que los tonos de baja frecuencia aparezcan gradualmente, suban de tono y luego se desvanezcan al alcanzar la frecuencia más alta, creando un efecto cíclico.
* **Salida:** El script genera un audio reproducible de un solo Tono de Shepard y una Escala de Shepard ascendente utilizando `IPython.display.Audio`.

## Requisitos

Para ejecutar este notebook, necesitarás las siguientes bibliotecas de Python:
* `numpy`
* `matplotlib`
* `scipy` (específicamente `scipy.signal.hilbert`)
* `IPython` (para la reproducción de audio)

## Cómo Usar

1.  Abre el archivo `clase06.ipynb` en un entorno compatible con Jupyter (como Google Colab o Jupyter Notebook local).
2.  Ejecuta las celdas de código en orden.
3.  Observa las gráficas generadas por `matplotlib` para los Ejercicios 12 y 13.
4.  Escucha los clips de audio generados en el Ejercicio 14.
5.  Puedes modificar los parámetros (ej. `Am`, `fm`, `fc`, `W`, `alpha`) en las celdas de código para experimentar con los resultados.
