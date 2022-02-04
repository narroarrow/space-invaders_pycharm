import pygame

# Initializing the pygame
import random

pygame.init()

# Creating the window screen
screen = pygame.display.set_mode((800, 600))

# Window title and icon
pygame.display.set_caption("Space Invaders")
windowIcon = pygame.image.load('windowIcon.png')
pygame.display.set_icon(windowIcon)

# Player Position Variables
playerImg = pygame.image.load('shipIcon.png')
playerX = 370
playerY = 480
playerX_change = 0

# Aliens Position Variables
alienImg = pygame.image.load('alien.png')
alienX = random.randint(0, 800)
alienY = random.randint(50, 150)
alienX_change = 0.2
alienY_change = 40

# Bullet Variables
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletY_change = 0.75
bullet_state = "ready"  # ready state means bullet ready to shoot


# Player function
def player(positionX, positionY):
    screen.blit(playerImg, (positionX, positionY))


# Alien function
def alien(positionX, positionY):
    screen.blit(alienImg, (positionX, positionY))


# Bullet function
def fire_bullet(positionX, positionY):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (positionX + 16, positionY + 5))


# Game Loop
close_program = True
while close_program:

    # Background Color - RGB
    screen.fill((27, 29, 90))

    # Loop for events occurring in game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close_program = False

        # Player Inputs
        if event.type == pygame.KEYDOWN:

            # Player Movement
            if event.key == pygame.K_LEFT:
                playerX_change = -0.15
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.15
            # Shooting
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Player Ship Boundaries and Movement
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Alien Boundaries and Movement
    alienX += alienX_change
    if alienX <= 0:
        alienX_change = 0.2
        alienY += alienY_change
    elif alienX >= 736:
        alienX_change = -0.2
        alienY += alienY_change

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    alien(alienX, alienY)

    # Updating the screen to monitor events
    pygame.display.update()
