import pygame

# initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Title and icon
pygame.display.set_caption("Space Invaders")

# https://www.flaticon.com/search?word=space&type=icon
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("img.png")
playerImg = pygame.transform.scale(playerImg, (64, 64))
playerX = 370
playerY = 480
playerX_change = 0

# blit means draw
def player(x, y):
    screen.blit(playerImg, (playerX, playerY))


# Game Loop
running = True
while running:
    # RGB red,Green,Blue
    screen.fill((100, 10, 200))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # if key stroke is pressed check whether its right or left
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            playerX_change = 0.1
        if event.key == pygame.K_LEFT:
            playerX_change = -0.1

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
            playerX_change = 0
    # 5 = 5 + -0.1 -> 5 = 5 - 0.1

    playerX += playerX_change
    player(playerX, playerY)
    pygame.display.update()
