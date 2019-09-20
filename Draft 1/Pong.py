import pygame, sys, time, random
from pygame.locals import *

def contact(ball, image):
    if ball.left == image.right or ball.right == image.left:
        ball.velocity = -ball.velocity
        ball.angle = random.randint(-10,10)

def play():
    # setup pygame
    pygame.init()
    mainClock = pygame.time.Clock()

class Ball(pygame.Rect):
    def __init__(self, velocity, *args, **kwargs):
        self.velocity = velocity
        self.angle = 0
        super().__init__(*args,**kwargs)
    def move_ball(self):
        self.x += self.velocity
        self.y += self.angle

    # setup window
    WINDOWWIDTH = 960
    WINDOWHEIGHT = 540
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

    player_middle_paddle = pygame.Rect(WINDOWWIDTH-100, WINDOWHEIGHT / 2, 100, 100)
    player_middle_paddle_stretched = pygame.transform.scale(paddleImage, (100, 100))

    player_top_paddle = pygame.Rect(WINDOWWIDTH-100, 0, 100, 100)
    player_top_paddle_stretched = pygame.transform.scale(paddleImage, (100, 100))

    player_bottom_paddle = pygame.Rect(WINDOWWIDTH - 100, WINDOWHEIGHT - 100, 100, 100)
    player_bottom_paddle_stretched = pygame.transform.scale(paddleImage, (100, 100))

    AI_middle_paddle = pygame.Rect(0, WINDOWHEIGHT /2, 200, 100)
    AI_middle_paddle_stretched = pygame.transform.scale(paddleImage, (100, 100))

    AI_top_paddle = pygame.Rect(0, 0, 100, 100)
    AI_top_paddle_stretched = pygame.transform.scale(paddleImage, (100, 100))

    AI_bottom_paddle = pygame.Rect(0, WINDOWHEIGHT - 100, 100, 100)
    AI_bottom_paddle_stretched = pygame.transform.scale(paddleImage, (100, 100))

    netImage = pygame.image.load('net.png')
    net = pygame.Rect(WINDOWWIDTH /2, WINDOWHEIGHT /2, 100, 100)
    net_stretched = pygame.transform.scale(netImage, (100,100))

    ballImage = pygame.image.load('ball.png')
    ball = pygame.Rect(WINDOWWIDTH /2, WINDOWHEIGHT /2 , 20, 20)
    ball_stretched = pygame.transform.scale(ballImage, (20, 20))


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

        windowSurface.fill(WHITE)
        windowSurface.blit(player_middle_paddle_stretched, player_middle_paddle)
        windowSurface.blit(player_bottom_paddle_stretched, player_bottom_paddle)
        windowSurface.blit(player_top_paddle_stretched, player_top_paddle)

        windowSurface.blit(AI_middle_paddle_stretched, AI_middle_paddle)
        windowSurface.blit(AI_bottom_paddle_stretched, AI_bottom_paddle)
        windowSurface.blit(AI_top_paddle_stretched, AI_top_paddle)

        windowSurface.blit(net_stretched, net)
        windowSurface.blit(ball_stretched, ball)

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

        contact(ball,player_bottom_paddle)
        pygame.display.update()


play()