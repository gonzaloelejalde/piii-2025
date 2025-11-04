# Control de LEDs con dsPIC30F4013 (Clase 12)

Este repositorio contiene un notebook (`clase12.ipynb`) con ejemplos de código en C para programar un microcontrolador dsPIC30F4013, enfocado en el control básico de pines de salida (LEDs) usando retardos.

## Contenido del Notebook

### 1. Ejemplo Básico: Parpadear un LED

El notebook comienza con un código de ejemplo estándar para hacer parpadear un LED (Blink).

* **Pin:** `RB0` (configurado como salida).
* **Lógica:** Dentro de un bucle infinito (`while(1)`), el LED en `RB0` se enciende (`LATBbits.LATB0 = 1`), espera 500ms (`Delay_ms(500)`), se apaga (`LATBbits.LATB0 = 0`), y vuelve a esperar 500ms.

### 2. Ejercicio Principal: Encendido Secuencial de LEDs

El objetivo principal es encender dos LEDs en momentos específicos después de energizar el dsPIC.

* **Objetivo:**
    * Encender LED1 a los 3 segundos.
    * Encender LED2 a los 11 segundos.
* **Conexiones Hardware:**
    * **LED1:** Conectado al pin `RB0`.
    * **LED2:** Conectado al pin `RB1`.

#### Solución (Código C para dsPIC)

El código principal implementa la lógica de encendido secuencial:

1.  **Configuración de Fuses y Reloj:**
    * Se configura el oscilador para usar `XT_PLL8` (Oscilador externo con PLL x8).
    * Se deshabilita el Watchdog Timer (`WDT_OFF`).
    * Se define la frecuencia de ciclo de instrucción `FCY` en `8000000UL` (8 MHz).
2.  **Programa Principal (`main`):**
    * Se configuran los pines `RB0` y `RB1` como salidas digitales (`TRISBbits.TRISB0 = 0` y `TRISBbits.TRISB1 = 0`).
    * Se inicializan ambos LEDs en estado apagado (`LATBbits.LATB0 = 0` y `LATBbits.LATB1 = 0`).
    * Se ejecuta un primer retardo de 3 segundos: `__delay_ms(3000)`.
    * Se enciende el LED1: `LATBbits.LATB0 = 1`.
    * Se ejecuta un segundo retardo de 8 segundos (para un total de 3 + 8 = 11 segundos desde el inicio): `__delay_ms(8000)`.
    * Se enciende el LED2: `LATBbits.LATB1 = 1`.
    * El programa entra en un bucle infinito (`while(1);`) para mantener los LEDs encendidos.

### 3. Cómo Implementarlo en la Placa

El notebook finaliza con instrucciones detalladas para programar el microcontrolador:

1.  Abrir **MPLAB X IDE** y crear un proyecto para el **dsPIC30F4013**.
2.  Seleccionar el compilador **XC16**.
3.  Crear un archivo `main.c` y pegar el código C proporcionado.
4.  Verificar que la definición `FCY` coincida con la configuración del reloj (8 MHz en el ejemplo).
5.  Compilar el proyecto.
6.  Programar el dsPIC (usando PICkit, ICD3, etc.).
7.  Conectar el hardware (LEDs a RB0 y RB1 con sus resistencias a GND).
8.  Energizar la placa y observar el resultado: LED1 se enciende a los 3s y LED2 a los 11s.

### Nota sobre el Entorno

El código de las celdas es C (para el compilador XC16) y no Python. No está diseñado para ejecutarse directamente en el entorno de Google Colab (lo cual explica el `SyntaxError` en la salida de la celda 5, ya que el kernel de Python no entiende la sintaxis de C). El código debe ser copiado a un IDE de microcontroladores como MPLAB X.
