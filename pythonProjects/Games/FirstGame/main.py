import pygame
import constant
from character import Character

pygame.init()

window = pygame.display.set_mode((constant.heightWindow, constant.widthWindow))
pygame.display.set_caption("First Game")

clock = pygame.time.Clock()

player = Character(constant.spawnCharacterX, constant.spawnCharacterY)



# We define motion variables
moveLeft = False
moveRight = False
moveUp = False
moveDown = False

running = True

while running:
    # We set the frame rate
    clock.tick(constant.FPS)

    # This means that when our character moves, it leaves no trace
    window.fill(constant.backGroundColor)

    # Calculate the motion of the player
    deltaX = 0
    deltaY = 0

    if moveLeft:
        deltaX = constant.velocity
    if moveRight:
        deltaX = -constant.velocity
    if moveUp:
        deltaY = -constant.velocity
    if moveDown:
        deltaY = constant.velocity

    # move the player
    player.move(deltaX, deltaY)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # Activate the movement of the player
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moveRight = True
            if event.key == pygame.K_d:
                moveLeft = True
            if event.key == pygame.K_w:
                moveUp = True
            if event.key == pygame.K_s:
                moveDown = True

        # Deactivate the movement of the player
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moveRight = False
            if event.key == pygame.K_d:
                moveLeft = False
            if event.key == pygame.K_w:
                moveUp = False
            if event.key == pygame.K_s:
                moveDown = False

    player.draw(window)
    pygame.display.update()

pygame.quit()
