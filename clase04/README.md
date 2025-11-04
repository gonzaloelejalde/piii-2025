# Generación y Análisis de Ondas – Clase 04

Este cuaderno de Google Colab continúa con el estudio de la **representación digital de señales**, abordando los fenómenos de **aliasing** y **cuantificación**, fundamentales en el procesamiento digital de señales.

---

## 🎧 Ejercicio 8 – Aliasing

En este ejercicio se analiza el fenómeno de **aliasing**, que ocurre cuando una señal se muestrea a una frecuencia menor que el doble de su componente de frecuencia más alta (violando el teorema de Nyquist).  

Se muestran ejemplos prácticos donde:
- En condiciones de **submuestreo**, las componentes de alta frecuencia se reflejan como frecuencias más bajas.
- Se observa cómo el aliasing distorsiona la forma de la señal original al reconstruirla.

El análisis incluye gráficos de la señal muestreada y su espectro, mostrando los efectos del aliasing visualmente.

---

## 📊 Ejercicio 9 – Cuantificación y distorsión por granularidad

Este ejercicio aborda el proceso de **cuantificación**, es decir, el redondeo de una señal continua a niveles discretos determinados por el número de bits.  

Se analizan los siguientes conceptos:
- Relación entre número de bits y resolución del cuantizador.
- **Error de cuantificación**, que oscila en torno a ±Δ/2.
- **Distorsión por granularidad**, que se hace más visible al usar pocos bits.

Se incluyen ejemplos con amplitud 1 y 8 bits, mostrando cómo el escalón de cuantización y el error afectan la señal resultante.

---

## 🧰 Herramientas utilizadas
- **Python**
- **NumPy**
- **Matplotlib**
- **Google Colab**

