import pygame

pygame.init()

DISPLAY_SURFACE = pygame.display.set_mode([800, 600])
FPS_CLOCK = pygame.time.Clock()
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    DISPLAY_SURFACE.fill((76, 250, 252))
    pygame.draw.rect(DISPLAY_SURFACE, (143, 76, 43), ())
    pygame.display.update()
    FPS_CLOCK.tick(30)
