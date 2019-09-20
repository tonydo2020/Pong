import pygame, sys, time, random
from pygame.locals import *


# setup pygame
pygame.init()
mainClock = pygame.time.Clock()


# setup window
WINDOWWIDTH = 600
WINDOWHEIGHT = 600
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Pong')

#Setup colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RANDOM = (123, 45, 95)

# #Setup commands
moveLeft = False
moveRight = False
moveUp = False
moveDown = False

MOVESPEED = 2
#Setup the block data structure

paddleImage = pygame.image.load('spongebob.gif')

player_middle_paddle = pygame.Rect(500, 100, 100, 100)
player_middle_paddle_stretched = pygame.transform.scale(paddleImage, (100, 100))

player_top_paddle = pygame.Rect(WINDOWWIDTH-100, 0, 100, 100)
player_top_paddle_stretched = pygame.transform.scale(paddleImage, (100, 100))

player_bottom_paddle = pygame.Rect(WINDOWWIDTH - 100, WINDOWHEIGHT - 100, 100, 100)
player_bottom_paddle_stretched = pygame.transform.scale(paddleImage, (100, 100))

AI_middle_paddle = pygame.Rect(500, 100, 100, 100)
AI_middle_paddle_stretched = pygame.transform.scale(paddleImage, (100, 100))

AI_top_paddle = pygame.Rect(WINDOWWIDTH-100, 0, 100, 100)
AI_top_paddle_stretched = pygame.transform.scale(paddleImage, (100, 100))

AI_bottom_paddle = pygame.Rect(WINDOWWIDTH - 100, WINDOWHEIGHT - 100, 100, 100)
AI_bottom_paddle_stretched = pygame.transform.scale(paddleImage, (100, 100))


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            # change the keyboard variables
            if event.key == K_LEFT:
                moveRight = False
                moveLeft = True
            if event.key == K_RIGHT:
                moveLeft = False
                moveRight = True
            if event.key == K_UP:
                moveDown = False
                moveUp = True
            if event.key == K_DOWN:
                moveUp = False
                moveDown = True
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT:
                moveLeft = False
            if event.key == K_RIGHT:
                moveRight = False
            if event.key == K_UP:
                moveUp = False
            if event.key == K_DOWN:
                moveDown = False

    windowSurface.fill(BLACK)
    windowSurface.blit(player_middle_paddle_stretched, player_middle_paddle)
    windowSurface.blit(player_bottom_paddle_stretched, player_bottom_paddle)
    windowSurface.blit(player_top_paddle_stretched, player_top_paddle)

    windowSurface.blit(AI_middle_paddle_stretched, AI_middle_paddle)
    windowSurface.blit(AI_bottom_paddle_stretched, AI_bottom_paddle)
    windowSurface.blit(AI_top_paddle_stretched, AI_top_paddle)

    if moveDown and player_middle_paddle.bottom < WINDOWHEIGHT:
        player_middle_paddle.top += MOVESPEED
    if moveUp and player_middle_paddle.top > 0:
        player_middle_paddle.top -= MOVESPEED
    if moveLeft and player_top_paddle.left > WINDOWWIDTH / 2:
        player_top_paddle.left -= MOVESPEED
        player_bottom_paddle.left -= MOVESPEED
    if moveRight and player_top_paddle.right < WINDOWWIDTH :
        player_top_paddle.right += MOVESPEED
        player_bottom_paddle.right += MOVESPEED
    pygame.display.update()