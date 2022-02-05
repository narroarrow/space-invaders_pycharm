import pygame
import math

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
alienImg = []
alienX = []
alienY = []
alienX_change = []
alienY_change = []
numberOfAliens = 10

for i in range(numberOfAliens):
    alienImg.append(pygame.image.load('alien.png'))
    alienX.append(random.randint(0, 735))
    alienY.append(random.randint(50, 150))
    alienX_change.append(0.2)
    alienY_change.append(40)

# Bullet Variables
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletY_change = 0.75
bullet_state = "ready"  # ready state means bullet ready to shoot

# Score Variables
scoreValue = 0
font = pygame.font.Font('PublicPixel-0W6DP.ttf', 16)
textX = 10
textY = 10

# Game Over Variables
gameOverFont = pygame.font.Font('PublicPixel-0W6DP.ttf', 64)

def gameOverText():
    gameOverText = gameOverFont.render("GAME OVER", True, (255, 255, 255))
    screen.blit(gameOverText, (150, 250))

def showScore(positionX, positionY):
    score = font.render("Score: " + str(scoreValue), True, (255, 255, 255))
    screen.blit(score, (positionX, positionY))

# Player function
def player(positionX, positionY):
    screen.blit(playerImg, (positionX, positionY))


# Alien function
def alien(positionX, positionY, i):
    screen.blit(alienImg[i], (positionX, positionY))


# Bullet function
def fire_bullet(positionX, positionY):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (positionX + 16, positionY + 5))


def isCollision(alienX, alienY, bulletX, bulletY):
    distance = math.sqrt(math.pow(alienX - bulletX, 2) + math.pow(alienY - bulletY, 2))

    if distance < 27:
        return True
    else:
        return False


# Game Loop
close_program = True
while close_program:

    # Background Color - RGB
    screen.fill((173, 216, 230))

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

    # Alien Boundaries and Movement. Bullet Collision. Game Over
    for i in range(numberOfAliens):

        # Game Over

        if alienY[i] > 450 or (alienY[i] == playerY and alienX[i] == playerX):
            for j in range(numberOfAliens):
                alienY[j] = 2000
            gameOverText()
            break

        # Alien Movement
        alienX[i] += alienX_change[i]
        if alienX[i] <= 0:
            alienX_change[i] = 0.2
            alienY[i] += alienY_change[i]
        elif alienX[i] >= 736:
            alienX_change[i] = -0.2
            alienY[i] += alienY_change[i]

        # Collision
        collision = isCollision(alienX[i], alienY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            scoreValue += 100
            alienX[i] = random.randint(0, 735)
            alienY[i] = random.randint(50, 150)

        alien(alienX[i], alienY[i], i)

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    showScore(textX, textY)

    # Updating the screen to monitor events
    pygame.display.update()
