# Guía y Calculadora de Componentes Electrónicos 

Calculadora interactiva con interfaz gráfica desarrollada en Python para facilitar la interpretación y el cálculo de valores nominales de componentes pasivos. 

Este proyecto fue desarrollado originalmente como herramienta de apoyo computacional para el Laboratorio de Electrónica (Facultad de Ciencias, UNAM), permitiendo comprobar de manera rápida los valores teóricos obtenidos en la práctica.

##  Características Principales

* **Resistores:** Cálculo del valor óhmico y tolerancia mediante código de colores (soporta lectura por bandas).
* **Capacitores:** Interpretación de códigos numéricos (ej. 104, 473) para obtener la capacitancia en unidades escaladas (µF, nF, pF).
* **Inductores:** Lectura de inductancia mediante bandas de colores.
* **Formato Inteligente:** El algoritmo ajusta automáticamente el resultado a la escala de ingeniería más legible (kΩ, MΩ, mH, etc.).
* **Navegación Intuitiva:** Interfaz separada por módulos y menús interactivos construidos con `pygame`.

---

##  Cómo usar el programa

Tienes dos formas de ejecutar esta herramienta, dependiendo de si eres usuario final o desarrollador.

### Opción 1: Usar el Ejecutable (.exe) - *Recomendado para Windows*
No necesitas instalar Python ni configurar nada. 
1. Ve a la sección de **Releases** (a la derecha de esta página).
2. Descarga el archivo `.exe` más reciente.
3. Haz doble clic en el archivo descargado para abrir la calculadora.

### Opción 2: Ejecutar desde el código fuente
Si deseas ver el código, modificarlo o ejecutarlo en otro sistema operativo (Linux/macOS):

1. Clona este repositorio:
   ```bash
   git clone [https://github.com/ZhuFer/Guia-de-componentes.git](https://github.com/ZhuFer/Guia-de-componentes.git)
   
2. Dentro de la carpeta, instala las dependencias y corre el juego:
   ```bash
   pip install pygame
   python main.py
