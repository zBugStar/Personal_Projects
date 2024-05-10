import pygame
from personaje import Personaje

player = Personaje(250, 250)
pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("First Game")

running = True
while running:

    player.draw(win)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    win.fill((0, 0, 0))
    pygame.display.update()

pygame.quit()
