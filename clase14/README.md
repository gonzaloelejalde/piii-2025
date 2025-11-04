# Simulador de Canal de Comunicación (Primer Parcial)

Este repositorio contiene el notebook (`PrimerParcial.ipynb`) que describe un sistema de simulación de un canal de comunicación con ruido. El sistema utiliza una PC como administrador y una placa ESP32 como un nodo intermedio (el "canal") que puede introducir errores en los mensajes de forma controlada.

El proyecto está dividido en dos componentes principales: el script de la PC Administradora y el script de la ESP-32 (nodo intermedio).

## 1. Código PC Administrador (Python)

Este script (`admin_monitor_estetico.py`) se ejecuta en una PC y actúa como el centro de control y monitoreo del canal.

* **Rol:** Servidor de control.
* **Puerto:** Escucha en el puerto `5050` (`CONTROL_PORT`).
* **Funcionalidad:**
    * `esp_acceptor()`: Espera y acepta conexiones entrantes desde la placa ESP-32.
    * `esp_receiver()`: Recibe y procesa mensajes de estado de la ESP. Imprime los mensajes "crudos" (`CANAL (crudo):`) y los mensajes de estado (`[OK]`, `[ERROR]`, `MODO_ERROR_ON`, `MODO_ERROR_OFF`).
    * `main_menu()`: Proporciona una interfaz de línea de comandos (CLI) al administrador para:
        1.  Solicitar información a la ESP.
        2.  Activar el "MODO ERROR" (para que la ESP comience a modificar mensajes).
        3.  Desactivar el "MODO ERROR".

## 2. Código ESP-32 (MicroPython)

Este script (`esp_intermedia_monitor.py`) se ejecuta en una ESP32 y actúa como el "canal" de comunicación. Recibe mensajes de un transmisor, opcionalmente los corrompe y los reenvía a un receptor final.

* **Rol:** Nodo intermedio (Canal).
* **Conectividad:**
    * Se conecta a una red WiFi (SSID y PASSWORD).
    * Se conecta a la PC Administradora (`PC_ADMIN_IP`, `CONTROL_PORT`) para recibir comandos.
    * Escucha en el puerto `5051` (`CHANNEL_PORT`) para recibir datos de un transmisor (ej. otra ESP).
    * Reenvía los datos a un receptor final (`RECEIVER_IP`, `RECEIVER_PORT`).
* **Funcionalidad Clave:**
    * **`pc_control_client()`:** Gestiona la conexión saliente hacia la PC Administradora. Recibe comandos como `MODO_ERROR_ON` y `MODO_ERROR_OFF` para activar/desactivar la simulación de ruido.
    * **`canal_server()`:** Es el servidor principal que escucha en el puerto `5051`. Cuando recibe datos:
        1.  Reporta el mensaje "crudo" a la PC.
        2.  Si `modo_error` está activo, llama a `introducir_error(data)`.
        3.  Reporta el mensaje "modulado" (potencialmente corrupto) a la PC.
        4.  Llama a `reenviar_a_esp()` para enviar el mensaje (modulado o no) al receptor final.
    * **`introducir_error(data)`:** Esta es la función de simulación de ruido.
        * Tiene una probabilidad del 30% (`PROB = 0.3`) de modificar el mensaje.
        * **Prioridad:** Intenta modificar específicamente dígitos del '0' al '7' si los encuentra en el mensaje.
        * **Alternativa:** Si no encuentra esos dígitos, intenta modificar otros caracteres imprimibles.
        * **Fallback:** Si falla lo anterior, modifica un byte aleatorio en la trama.

## 3. Análisis de Latencia (¿Por qué demora mucho?)

El notebook incluye una sección de texto que analiza por qué el sistema puede experimentar retrasos.

La conclusión es que la latencia no se debe a la falta de capacidad de procesamiento de la ESP32, sino a la **suma de pequeñas demoras** introducidas por la arquitectura del sistema, que utiliza threads simples y múltiples operaciones de red TCP (conexión, envío, desconexión) para cada mensaje:
1.  Recibir del transmisor (Socket 5051).
2.  Procesar el mensaje (buscar dígitos, modificar bytes).
3.  Enviar los logs (crudo y modulado) a la PC (Socket 5050).
4.  Crear un *nuevo* socket, conectar y enviar al receptor (Socket 5052).
5.  Overhead de MicroPython y los prints de depuración.

## Nota sobre Ejecución

Los bloques de código están destinados a entornos diferentes:
* El **Código Pc Administrador** es para una PC estándar con Python.
* El **Código Esp-32** es para una placa ESP32 con **MicroPython**. No se puede ejecutar en Google Colab (lo que resulta en el `AttributeError: module 'network' has no attribute 'WLAN'`), debe ser flasheado en el hardware real.
