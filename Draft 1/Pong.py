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


#Setup the block data structure
paddleImage = pygame.image.load('paddles.png')

player_middle_paddle = pygame.Rect(300, 100, 40, 40)
player_middle_paddle_stretched = pygame.transform.scale(paddleImage, (40, 40))

player_top_paddle = pygame.Rect(300, 100, 40, 40)
player_top_paddle_stretched = pygame.transform.scale(paddleImage, (40, 40))

player_bottom_paddle = pygame.Rect(300, 300, 40, 40)
player_bottom_paddle_stretched = pygame.transform.scale(paddleImage, (100, 100))


while True:
    windowSurface.fill(BLACK)
    windowSurface.blit(player_bottom_paddle_stretched, player_bottom_paddle)
    time.sleep(10)