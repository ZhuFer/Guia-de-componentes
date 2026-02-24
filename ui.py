import pygame

class Boton:
    def __init__(self, x, y, ancho, alto, texto, color_base, color_hover):
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.texto = texto
        self.color_base = color_base
        self.color_hover = color_hover
        self.fuente = pygame.font.Font(None, 36)
        self.presionado = False

    def dibujar(self, pantalla):
        # Cambiar de color si el mouse está encima
        pos_mouse = pygame.mouse.get_pos()
        color_actual = self.color_hover if self.rect.collidepoint(pos_mouse) else self.color_base
        
        pygame.draw.rect(pantalla, color_actual, self.rect, border_radius=10)
        
        # Renderizar texto centrado
        texto_surf = self.fuente.render(self.texto, True, (255, 255, 255))
        texto_rect = texto_surf.get_rect(center=self.rect.center)
        pantalla.blit(texto_surf, texto_rect)

    def clic(self, eventos):
        for evento in eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if self.rect.collidepoint(evento.pos):
                    return True
        return False