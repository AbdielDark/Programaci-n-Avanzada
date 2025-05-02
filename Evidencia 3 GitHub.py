import pygame
import sys

# Clase Perfil
class Perfil:
    def __init__(self, x, y, alto, ancho, velocidad):
        self.x = x
        self.y = y
        self.alto = alto
        self.ancho = ancho
        self.velocidad = velocidad
        self.imagen = pygame.image.load("perfil.png")
        self.imagen = pygame.transform.scale(self.imagen, (ancho, alto))

    def mostrar(self, ventana):
        ventana.blit(self.imagen, (self.x, self.y))


# Función principal
def main():
    pygame.init()
    ancho_ventana = 600
    alto_ventana = 400
    ventana = pygame.display.set_mode((ancho_ventana, alto_ventana))
    pygame.display.set_caption("Mover Perfil")

    # Crear objeto de la clase Perfil
    perfil = Perfil(x=100, y=100, alto=80, ancho=80, velocidad=5)

    clock = pygame.time.Clock()

    # Bucle principal
    while True:
        ventana.fill((255, 255, 255))  # Fondo blanco

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Detectar teclas presionadas
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            perfil.x -= perfil.velocidad
        if teclas[pygame.K_RIGHT]:
            perfil.x += perfil.velocidad
        if teclas[pygame.K_UP]:
            perfil.y -= perfil.velocidad
        if teclas[pygame.K_DOWN]:
            perfil.y += perfil.velocidad

        # Mostrar perfil
        perfil.mostrar(ventana)

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()