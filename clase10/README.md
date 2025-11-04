# Simulación de Transmisor/Receptor 4D-PAM5 (Clase 10)

Este repositorio contiene el notebook de Jupyter (`clase10.ipynb`) que implementa un sistema completo de transmisión y recepción digital. El sistema codifica un mensaje de texto a símbolos 4D-PAM5, los conforma con un filtro de Coseno Alzado, y los transmite a través de un socket TCP. Un script receptor escucha en el socket, recibe la señal, la decodifica y recupera el mensaje original.

## Componentes Clave del Notebook

El notebook define todos los parámetros y funciones necesarios para la simulación:

* **Parámetros de Red:**
    * `HOST`: Define la IP del receptor (ej. "10.0.0.203").
    * `PORT`: Define el puerto de comunicación (ej. 5000).
* **Parámetros de Modulación (4D-PAM5):**
    * `PAM5_LEVELS`: Define los 5 niveles de amplitud `[-2, -1, 0, 1, 2]`.
    * `ENC_MAP` (Mapa de Codificación): Un diccionario que mapea grupos de bits a los niveles PAM5 para la modulación 4D.
    * `DEC_MAP` (Mapa de Decodificación): El inverso del `ENC_MAP` para la decodificación.
* **Parámetros del Filtro (Coseno Alzado):**
    * `fB = 32e9` (Velocidad de símbolos).
    * `M = 8` (Factor de sobremuestreo).
    * `alpha = 0.1` (Factor de roll-off).
* **Funciones Principales:**
    * `string_to_bits(s)` y `bits_to_string(b)`: Convierten texto a bits y viceversa.
    * `bits_to_pam5(bits)` y `pam5_to_bits(simbolos)`: Mapean bits a símbolos 4D-PAM5 y viceversa, usando `ENC_MAP` y `DEC_MAP`.
    * `generar_pulso_rrc(...)`: Genera la respuesta al impulso `g[n]` del filtro Coseno Alzado.
    * `sobremuestrear(simbolos, M)`: Inserta `M-1` ceros entre cada símbolo.
    * `visualizar_senal(sn, ...)`: Grafica la señal en el tiempo.
    * `detectar_offset(senal, M)`: Encuentra el punto óptimo de muestreo para la sincronización en el receptor.
    * `decision_por_umbral(muestras, niveles)`: Compara la amplitud de la señal recibida con los niveles PAM5 para decidir el símbolo.

---

## Flujo del Sistema

El notebook está dividido en dos scripts principales que deben ejecutarse en terminales (o celdas) separadas.

### 1. Transmisión (Tx)

El script del transmisor realiza las siguientes acciones:

1.  **Codificación:** Define un `MENSAJE` (ej. "Hola Compañera").
2.  El mensaje se convierte a una secuencia de bits (`string_to_bits`).
3.  Los bits se agrupan y mapean a símbolos 4D-PAM5 (`bits_to_pam5`).
4.  **Conformado de Pulso:**
    * Se genera el filtro Coseno Alzado (`g[n]`).
    * Los símbolos PAM5 se sobremuestrean (`xn`).
    * La señal sobremuestreada se convoluciona con el filtro `g[n]` para crear la señal analógica a transmitir (`sn = convolve(xn, gn)`).
5.  **Transmisión por Socket:**
    * La señal `sn` se visualiza gráficamente.
    * Se establece una conexión TCP (`socket.SOCK_STREAM`) con el `HOST` y `PORT`.
    * La señal (`sn`) se envía como bytes a través del socket (`s.sendall(sn.tobytes())`).

### 2. Recepción (Rx)

El script del receptor actúa como un servidor que espera la conexión del transmisor:

1.  **Escucha de Socket:**
    * Se bindea al `PORT` y se pone en modo escucha (`s.listen()`).
    * Espera y acepta una conexión entrante (`conn, addr = s.accept()`).
2.  **Recepción de Señal:**
    * Recibe el flujo de bytes en un bucle (`conn.recv(1024)`) y lo almacena en `data`.
    * La señal de bytes se reconstruye en un array de numpy (`señal_recibida`).
3.  **Decodificación y Recuperación:**
    * Se visualiza la señal recibida.
    * Se detecta el offset de sincronización (`detectar_offset`) para encontrar el mejor instante de muestreo.
    * La señal se muestrea usando el offset y el factor `M`.
    * Se aplica `decision_por_umbral` para decodificar los niveles de amplitud a los símbolos PAM5 más cercanos.
    * Los símbolos se convierten de nuevo a bits (`pam5_to_bits`).
    * Los bits se reconvierten en el mensaje de texto original (`bits_to_string`), que se imprime en la consola.

## Requisitos

* `numpy`
* `matplotlib`
* `socket`
* `datetime`
* `random`
* `scipy` (para `convolve`)
