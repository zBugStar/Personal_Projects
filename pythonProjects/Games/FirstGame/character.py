import pygame
import constant


class Character():
    def __init__(self, x, y):
        self.shape = pygame.Rect(200, 200, constant.widthCharacter, constant.heightCharacter)
        self.shape.center = (x, y)

    def draw(self, window):
        pygame.draw.rect(window, constant.colorCharacter, self.shape)

    def move(self, deltaX, deltaY):
        self.shape.x = self.shape.x + deltaX
        self.shape.y = self.shape.y + deltaY
