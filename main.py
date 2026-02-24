import pygame
import sys
from ui import Boton
# Importamos la lógica desde los módulos que creamos
from componentes.resistor import calcular_resistencia_4_bandas, VALORES_BANDA, MULTIPLICADORES, TOLERANCIAS
from componentes.capacitor import calcular_capacitor_codigo, TOLERANCIAS_CAP
from componentes.inductor import calcular_inductor_4_bandas, VALORES_BANDA_IND, MULTIPLICADORES_IND, TOLERANCIAS_IND

# Inicializar Pygame
pygame.init()

# --- CAMBIO 1: AUMENTAR EL ANCHO DE PANTALLA ---
# Pasamos de 800 a 1000 pixeles de ancho para dar espacio a textos largos.
PANTALLA_ANCHO, PANTALLA_ALTO = 1000, 600
pantalla = pygame.display.set_mode((PANTALLA_ANCHO, PANTALLA_ALTO))
pygame.display.set_caption("Calculadora de Componentes Electrónicos")

# Colores (RGB)
GRIS_OSCURO = (40, 40, 40)
GRIS_MODAL = (60, 60, 60)
AZUL = (50, 100, 200)
AZUL_CLARO = (80, 150, 250)
BLANCO = (255, 255, 255)
COLOR_RES = (100, 255, 100) # Verde para resistores
COLOR_CAP = (100, 255, 255) # Cyan para capacitores
COLOR_IND = (255, 100, 255) # Magenta para inductores

# Mapa de colores para dibujar los rectángulos visuales en pantalla
MAPA_RGB = {
    "Negro": (0, 0, 0), "Café": (139, 69, 19), "Rojo": (200, 0, 0),
    "Naranja": (255, 140, 0), "Amarillo": (235, 215, 0), "Verde": (0, 150, 0),
    "Azul": (0, 0, 255), "Violeta": (148, 0, 211), "Gris": (128, 128, 128),
    "Blanco": (255, 255, 255), "Dorado": (218, 165, 32), "Plateado": (192, 192, 192),
    "Ninguna": GRIS_OSCURO # Mismo color del fondo
}

# --- FUNCIÓN AUXILIAR PARA CENTRAR TEXTO ---
def dibujar_texto_centrado(surf, texto, fuente, color, centro_x, centro_y):
    texto_surf = fuente.render(texto, True, color)
    texto_rect = texto_surf.get_rect(center=(centro_x, centro_y))
    surf.blit(texto_surf, texto_rect)

def seleccionar_item(opciones, titulo_modal, usar_colores=False):
    """Abre una ventana modal para elegir una opción de una lista."""
    reloj = pygame.time.Clock()
    fuente_titulo = pygame.font.Font(None, 40)
    
    botones = []
    ancho_btn = 160
    alto_btn = 40
    espacio_x = 180
    espacio_y = 50
    
    # La posición del modal se calcula dinámicamente según el ancho de pantalla
    inicio_x = PANTALLA_ANCHO // 2 - espacio_x + 10
    inicio_y = 100
    filas = (len(opciones) + 1) // 2
    
    rect_modal = pygame.Rect(inicio_x - 30, inicio_y - 60, espacio_x * 2 + 40, (filas + 1) * espacio_y + 90)
    
    for i, opcion in enumerate(opciones):
        col = i % 2
        fila = i // 2
        x = inicio_x + (col * espacio_x)
        y = inicio_y + (fila * espacio_y)
        botones.append((opcion, Boton(x, y, ancho_btn, alto_btn, opcion, AZUL, AZUL_CLARO)))

    btn_cancelar = Boton(inicio_x + 80, inicio_y + filas * espacio_y + 30, ancho_btn, alto_btn, "Cancelar", (200, 50, 50), (250, 80, 80))

    corriendo = True
    while corriendo:
        eventos = pygame.event.get()
        for evento in eventos:
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        # Dibujar fondo y borde del modal
        pygame.draw.rect(pantalla, GRIS_MODAL, rect_modal, border_radius=15)
        pygame.draw.rect(pantalla, AZUL_CLARO, rect_modal, width=3, border_radius=15)
        
        titulo_surf = fuente_titulo.render(titulo_modal, True, BLANCO)
        pantalla.blit(titulo_surf, (inicio_x - 10, inicio_y - 45))
        
        for opcion, btn in botones:
            btn.dibujar(pantalla)
            if usar_colores and opcion in MAPA_RGB:
                pygame.draw.rect(pantalla, MAPA_RGB[opcion], (btn.rect.x - 25, btn.rect.y + 10, 20, 20), border_radius=3)
            
            if btn.clic(eventos):
                return opcion
                
        btn_cancelar.dibujar(pantalla)
        if btn_cancelar.clic(eventos):
            return None

        pygame.display.update(rect_modal) # Solo actualizamos la zona del modal
        reloj.tick(60)

def pantalla_resistor():
    reloj = pygame.time.Clock()
    fuente_titulo = pygame.font.Font(None, 50)
    # --- CAMBIO 2: REDUCIR LIGERAMENTE LA FUENTE ---
    fuente_resultado = pygame.font.Font(None, 70) # De 80 a 70 para seguridad

    lista_b1 = list(VALORES_BANDA.keys())
    lista_mult = list(MULTIPLICADORES.keys())
    lista_tol = list(TOLERANCIAS.keys())

    c_b1, c_b2, c_mult, c_tol = "Café", "Negro", "Rojo", "Dorado"
    btn_volver = Boton(50, 500, 150, 50, "Volver", (200, 50, 50), (250, 80, 80))

    corriendo = True
    while corriendo:
        pantalla.fill(GRIS_OSCURO)
        eventos = pygame.event.get()

        for evento in eventos:
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        btn_b1 = Boton(50, 150, 300, 50, f"Banda 1: {c_b1}", AZUL, AZUL_CLARO)
        btn_b2 = Boton(50, 220, 300, 50, f"Banda 2: {c_b2}", AZUL, AZUL_CLARO)
        btn_mult = Boton(50, 290, 300, 50, f"Multiplicador: {c_mult}", AZUL, AZUL_CLARO)
        btn_tol = Boton(50, 360, 300, 50, f"Tolerancia: {c_tol}", AZUL, AZUL_CLARO)

        # --- CAMBIO 3: CENTRAR TÍTULOS Y RESULTADOS ---
        dibujar_texto_centrado(pantalla, "Resistor de 4 Bandas", fuente_titulo, BLANCO, PANTALLA_ANCHO // 2, 60)

        for btn in [btn_b1, btn_b2, btn_mult, btn_tol, btn_volver]:
            btn.dibujar(pantalla)

        pygame.draw.rect(pantalla, MAPA_RGB[c_b1], (370, 150, 50, 50), border_radius=5)
        pygame.draw.rect(pantalla, MAPA_RGB[c_b2], (370, 220, 50, 50), border_radius=5)
        pygame.draw.rect(pantalla, MAPA_RGB[c_mult], (370, 290, 50, 50), border_radius=5)
        pygame.draw.rect(pantalla, MAPA_RGB[c_tol], (370, 360, 50, 50), border_radius=5)

        resultado = calcular_resistencia_4_bandas(c_b1, c_b2, c_mult, c_tol)
        # Centramos el resultado en la mitad derecha de la nueva pantalla ancha
        dibujar_texto_centrado(pantalla, resultado, fuente_resultado, COLOR_RES, 725, 280)

        # Lógica de interacción
        if btn_b1.clic(eventos): c_b1 = seleccionar_item(lista_b1, "Elige la Banda 1", True) or c_b1
        if btn_b2.clic(eventos): c_b2 = seleccionar_item(lista_b1, "Elige la Banda 2", True) or c_b2
        if btn_mult.clic(eventos): c_mult = seleccionar_item(lista_mult, "Multiplicador", True) or c_mult
        if btn_tol.clic(eventos): c_tol = seleccionar_item(lista_tol, "Tolerancia", True) or c_tol
        if btn_volver.clic(eventos): return

        pygame.display.flip()
        reloj.tick(60)

def pantalla_capacitor():
    reloj = pygame.time.Clock()
    fuente_titulo = pygame.font.Font(None, 50)
    fuente_resultado = pygame.font.Font(None, 70) # Fuente más pequeña
    fuente_codigo = pygame.font.Font(None, 60)

    lista_digitos = [str(i) for i in range(10)]
    lista_letras = list(TOLERANCIAS_CAP.keys())

    d1, d2, mult, tol = "1", "0", "4", "K"
    btn_volver = Boton(50, 500, 150, 50, "Volver", (200, 50, 50), (250, 80, 80))

    corriendo = True
    while corriendo:
        pantalla.fill(GRIS_OSCURO)
        eventos = pygame.event.get()
        for evento in eventos:
            if evento.type == pygame.QUIT:
                pygame.quit(); sys.exit()

        btn_d1 = Boton(50, 150, 300, 50, f"Dígito 1: {d1}", AZUL, AZUL_CLARO)
        btn_d2 = Boton(50, 220, 300, 50, f"Dígito 2: {d2}", AZUL, AZUL_CLARO)
        btn_mult = Boton(50, 290, 300, 50, f"Multiplicador: {mult}", AZUL, AZUL_CLARO)
        btn_tol = Boton(50, 360, 300, 50, f"Tolerancia: {tol}", AZUL, AZUL_CLARO)

        dibujar_texto_centrado(pantalla, "Capacitor Cerámico/Poliéster", fuente_titulo, BLANCO, PANTALLA_ANCHO // 2, 60)
        
        for btn in [btn_d1, btn_d2, btn_mult, btn_tol, btn_volver]: 
            btn.dibujar(pantalla)

        # Centrar la referencia visual del código y el resultado
        dibujar_texto_centrado(pantalla, f"Código: {d1}{d2}{mult}{tol}", fuente_codigo, (200, 200, 200), 725, 180)
        resultado = calcular_capacitor_codigo(d1, d2, mult, tol)
        dibujar_texto_centrado(pantalla, resultado, fuente_resultado, COLOR_CAP, 725, 280)

        if btn_d1.clic(eventos): d1 = seleccionar_item(lista_digitos, "Dígito 1") or d1
        if btn_d2.clic(eventos): d2 = seleccionar_item(lista_digitos, "Dígito 2") or d2
        if btn_mult.clic(eventos): mult = seleccionar_item(lista_digitos, "Multiplicador") or mult
        if btn_tol.clic(eventos): tol = seleccionar_item(lista_letras, "Tolerancia") or tol
        if btn_volver.clic(eventos): return

        pygame.display.flip()
        reloj.tick(60)

def pantalla_inductor():
    reloj = pygame.time.Clock()
    fuente_titulo = pygame.font.Font(None, 50)
    fuente_resultado = pygame.font.Font(None, 70) # Fuente más pequeña

    lista_b1 = list(VALORES_BANDA_IND.keys())
    lista_mult = list(MULTIPLICADORES_IND.keys())
    lista_tol = list(TOLERANCIAS_IND.keys())

    c_b1, c_b2, c_mult, c_tol = "Gris", "Rojo", "Café", "Ninguna" # Ejemplo: 820 uH +/- 20%
    btn_volver = Boton(50, 500, 150, 50, "Volver", (200, 50, 50), (250, 80, 80))

    corriendo = True
    while corriendo:
        pantalla.fill(GRIS_OSCURO)
        eventos = pygame.event.get()

        for evento in eventos:
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        btn_b1 = Boton(50, 150, 300, 50, f"Banda 1: {c_b1}", AZUL, AZUL_CLARO)
        btn_b2 = Boton(50, 220, 300, 50, f"Banda 2: {c_b2}", AZUL, AZUL_CLARO)
        btn_mult = Boton(50, 290, 300, 50, f"Multiplicador: {c_mult}", AZUL, AZUL_CLARO)
        btn_tol = Boton(50, 360, 300, 50, f"Tolerancia: {c_tol}", AZUL, AZUL_CLARO)

        dibujar_texto_centrado(pantalla, "Inductor de 4 Bandas", fuente_titulo, BLANCO, PANTALLA_ANCHO // 2, 60)

        for btn in [btn_b1, btn_b2, btn_mult, btn_tol, btn_volver]:
            btn.dibujar(pantalla)

        pygame.draw.rect(pantalla, MAPA_RGB[c_b1], (370, 150, 50, 50), border_radius=5)
        pygame.draw.rect(pantalla, MAPA_RGB[c_b2], (370, 220, 50, 50), border_radius=5)
        pygame.draw.rect(pantalla, MAPA_RGB[c_mult], (370, 290, 50, 50), border_radius=5)
        pygame.draw.rect(pantalla, MAPA_RGB[c_tol], (370, 360, 50, 50), border_radius=5)

        resultado = calcular_inductor_4_bandas(c_b1, c_b2, c_mult, c_tol)
        # Centrar resultado
        dibujar_texto_centrado(pantalla, resultado, fuente_resultado, COLOR_IND, 725, 280)

        if btn_b1.clic(eventos): c_b1 = seleccionar_item(lista_b1, "Elige la Banda 1", True) or c_b1
        if btn_b2.clic(eventos): c_b2 = seleccionar_item(lista_b1, "Elige la Banda 2", True) or c_b2
        if btn_mult.clic(eventos): c_mult = seleccionar_item(lista_mult, "Multiplicador", True) or c_mult
        if btn_tol.clic(eventos): c_tol = seleccionar_item(lista_tol, "Tolerancia", True) or c_tol
        if btn_volver.clic(eventos): return

        pygame.display.flip()
        reloj.tick(60)

def menu_principal():
    reloj = pygame.time.Clock()
    fuente_titulo = pygame.font.Font(None, 60)
    
    # Centramos los botones del menú principal en el nuevo ancho
    centro_x = PANTALLA_ANCHO // 2 - 150
    btn_resistor = Boton(centro_x, 180, 300, 60, "Resistor", AZUL, AZUL_CLARO)
    btn_capacitor = Boton(centro_x, 270, 300, 60, "Capacitor", AZUL, AZUL_CLARO)
    btn_inductor = Boton(centro_x, 360, 300, 60, "Inductor", AZUL, AZUL_CLARO)
    
    # --- NUEVO BOTÓN PARA CERRAR ---
    # Usamos tonos rojizos para indicar la acción de salir
    btn_salir = Boton(centro_x, 480, 300, 60, "Salir", (200, 50, 50), (250, 80, 80))

    corriendo = True
    while corriendo:
        pantalla.fill(GRIS_OSCURO)
        eventos = pygame.event.get()
        
        for evento in eventos:
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        dibujar_texto_centrado(pantalla, "¿Qué deseas calcular?", fuente_titulo, BLANCO, PANTALLA_ANCHO // 2, 80)

        btn_resistor.dibujar(pantalla)
        btn_capacitor.dibujar(pantalla)
        btn_inductor.dibujar(pantalla)
        btn_salir.dibujar(pantalla) # Dibujamos el nuevo botón

        if btn_resistor.clic(eventos): pantalla_resistor()
        if btn_capacitor.clic(eventos): pantalla_capacitor()
        if btn_inductor.clic(eventos): pantalla_inductor()
        
        # --- LÓGICA PARA CERRAR ---
        if btn_salir.clic(eventos):
            pygame.quit()
            sys.exit()

        pygame.display.flip()
        reloj.tick(60)

if __name__ == "__main__":
    menu_principal()