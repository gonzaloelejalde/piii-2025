# Clase 8 – Proyecto PAM4 con ESP32

## 🔶 Introducción

**PAM (Pulse Amplitude Modulation)** modula la amplitud de los pulsos para transmitir datos.  
En **PAM4**, se utilizan **4 niveles de amplitud distintos**, lo que significa que cada símbolo puede representar **2 bits (00, 01, 10, 11)**.

Representación típica (valores equiespaciados):

| Bits | Nivel (ejemplo lógico) | Tensión (ejemplo físico) |
|------|------------------------|---------------------------|
| 00   | -3                    | 0.5 V                    |
| 01   | -1                    | 1.0 V                    |
| 10   | +1                    | 1.5 V                    |
| 11   | +3                    | 2.0 V                    |

---

## ⚙️ Generación de símbolos PAM4 en el ESP32

### 🔸 Opción 1 – DAC analógico
El **ESP32** posee un **DAC de 8 bits** (GPIO 25 y 26 en algunos modelos).  
Se pueden generar cuatro tensiones distintas → PAM4 **analógica real**.

### 🔸 Opción 2 – Simulación digital
Generar muestras discretas con **PWM** o **I²S**, y luego reconstruir la señal en PC mediante post-procesamiento.

### ✅ Recomendación
- **Si se quiere ver la señal real en un osciloscopio:** usar DAC.  
- **Si el análisis es digital (FFT, BER, ojo):** simular PAM4 en software.

---

## ⚖️ Limitaciones del ESP32 (DAC / ADC)

| Recurso | Resolución | Frecuencia típica | Comentario |
|----------|-------------|------------------|-------------|
| DAC | 8 bits (0–255) | ~1 MS/s | Poca linealidad, ruido |
| ADC | 12 bits (teóricos) | ~6 kS/s confiables (hasta 100 kS/s con hacks) | Ruido alto, no lineal |

Para cumplir Nyquist (≥ 2 muestras/símbolo), si el ADC funciona a 10 kS/s, la tasa máxima de símbolos PAM4 ≈ 2.5 kSímbolos/s.

🔹 Conclusión:  
Para análisis preciso → usar PC.  
Para prototipo simple → ESP32 puede generar y captar PAM4 a baja velocidad.

---

## 👁️ Cálculo del diagrama de ojo

1. Se superponen muchas trazas sincronizadas con el reloj de símbolos.  
2. Permite observar:

| Parámetro | Significado |
|------------|-------------|
| **Apertura vertical** | Margen de amplitud (ruido, SNR) |
| **Apertura horizontal** | Margen temporal (jitter, ISI) |
| **Cierre del ojo** | Problemas del canal (distorsión, interferencia) |

En la PC se acomodan las muestras por ventanas del período de símbolo y se grafican superpuestas.

---

## 🔢 BER (Bit Error Rate)

**BER = (bits erróneos) / (bits totales transmitidos)**

### Medición en el proyecto:
1. Transmitir una secuencia conocida (patrón pseudoaleatorio).  
2. El receptor decodifica PAM4 → bits.  
3. Comparar bits recibidos vs enviados.  
4. Calcular la proporción de errores.

Permite evaluar la **calidad del canal**.

---

## 🌐 Envío de datos desde ESP32 a PC (Wi-Fi)

### Opciones de transmisión:
| Protocolo | Características | Uso recomendado |
|------------|----------------|----------------|
| **UDP** | Rápido, sin confirmación | Streaming de muestras |
| **TCP** | Fiable, más lento | Transferencias seguras |
| **WebSocket** | Basado en TCP | Visualización en navegador |

**Flujo recomendado:**
1. ESP32 receptor captura muestras.  
2. Las empaqueta en buffers.  
3. Envía vía **UDP** a la PC.  
4. PC reconstruye señal → analiza (FFT, ojo, BER, SNR, latencia, jitter).

---

## 🧩 Organización del proyecto

| Rol | Tarea | Integrante |
|------|--------|------------|
| **HW & Canal** | Enlace físico/simulado, cableado, niveles, protección | *Asdru* |
| **TX** | Generación de símbolos PAM4, tramas, sincronización | *Leandro* |
| **RX** | Muestreo, sincronización, decisión por umbrales, BER local | *Cande* |
| **Visualización** | Recepción en PC, graficación, métricas | *Eric* |

---

## 🔌 HW & Canal

### Enlace (analógico o simulado)
- **Analógico:**  
  Se transmiten tensiones reales (4 niveles PAM4) por cable.  
  Permite medir SNR/BER reales y ver diagrama de ojo físico.  
- **Simulado:**  
  Se envían valores numéricos; canal físico ignorado.  
  Más limpio, ideal para pruebas lógicas.

### Cableado
- **Corto (≤ 2 m):** coaxial o par trenzado con GND común.  
- **Largo/ruidoso:** usar transceptores diferenciales (RS-485) para mejorar inmunidad.

### Niveles de voltaje
4 tensiones equiespaciadas dentro de 0–3.3 V.  
Ejemplo:
| Bits | Tensión |
|------|----------|
| 00 | 0.5 V |
| 01 | 1.2 V |
| 10 | 2.0 V |
| 11 | 2.7 V |

Se pueden generar con DAC, PWM filtrado o red R-2R.

### Protección y acondicionamiento
- **Resistencias en serie (100–220 Ω):** limitan corriente.  
- **Divisores resistivos:** adaptan niveles de tensión.  
- **Filtro RC:** suaviza PWM, reduce ruido, evita aliasing.  
- **Diodos/TVS:** protegen de picos o descargas.  
- **Capacitores de desacople (100 nF):** cercanos a cada chip.

---

## 🧮 Canal ideal y canal con errores simulados

### 1️⃣ Canal ideal
- Transmisión perfecta (sin ruido).  
- BER = 0.  
- Diagrama de ojo completamente abierto.  
- Referencia base para comparación.

### 2️⃣ Canal con errores simulados
Simular efectos del canal mediante scripts en PC:

| Error simulado | Descripción | Simulación por software |
|-----------------|--------------|--------------------------|
| **Ruido gaussiano** | Interferencia aleatoria | Sumar n ∼ N(0, σ) a cada muestra |
| **Retrasos (jitter)** | Variación temporal en símbolos | Desplazar aleatoriamente muestras |
| **Errores (bit flips)** | Bits mal recibidos | Cambiar símbolos con probabilidad Pₑ |
| **Distorsión (ISI)** | Mezcla entre símbolos consecutivos | Filtrar secuencia con RC o FIR con memoria |

---

## 🎯 ¿Por qué usar un código por efecto?
- Permite **aislar y medir** el impacto de cada fenómeno.  
- Facilita **comparaciones** de métricas (BER, SNR).  
- Mejora la visualización y análisis.

---

## 📊 Ejemplo visual esperado

| Canal | Descripción | Diagrama de ojo |
|--------|--------------|-----------------|
| Ideal | Niveles definidos | Ojo totalmente abierto |
| Con ruido | Niveles difusos | Ojo con ruido vertical |
| Con jitter | Variación temporal | Ojo cerrado horizontalmente |
| Con ISI | Mezcla entre símbolos | Ojo con cruces y desplazamientos |
| Con bit flips | Errores binarios | Ojo irregular, BER > 0 |

---

## 📘 Conclusión

El proyecto permite explorar **PAM4** en hardware real y en simulación.  
El **ESP32** puede generar y recibir señales PAM4 a baja velocidad, o bien actuar como interfaz Wi-Fi para análisis digital en PC.  
El enfoque modular (canal ideal y degradado) facilita estudiar el impacto del ruido, jitter e ISI sobre el **BER** y el **diagrama de ojo**.

---
