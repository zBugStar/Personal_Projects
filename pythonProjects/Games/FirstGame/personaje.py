import pygame


class Personaje():
    def __init__(self, x, y):
        self.shape = pygame.Rect(200, 200, 20, 20)
        self.shape.center = (x, y)

    def draw(self, win):
        pygame.draw.rect(win, (255, 0, 0), self.shape)
