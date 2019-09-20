import pygame, sys, time, random
from pygame.locals import *

# setup window
WINDOWWIDTH = 960
WINDOWHEIGHT = 540
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)

# Setup colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RANDOM = (123, 45, 95)


MOVESPEED = 2


class ball():
    ball_obj = pygame.Rect(WINDOWWIDTH /2, WINDOWHEIGHT /2, 100, 100)
    velocity = 0
    angle = 0
    ball_Image = pygame.image.load('ball.png')
    ball_Fixed = pygame.transform.scale(ball_Image, (100,100))


class score():
    player_Score = 0
    AI_Score = 0


ball.velocity = random.randint(-2, 2)
ball.angle = random.randint(-2,2)


def exit_game():
    pygame.quit()
    sys.exit()


def get_input():
    pressed = False
    while not pressed:
        for e in pygame.event.get():
            if e.type == QUIT:
                exit_game()
            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    exit_game()
                return  # start game for any other key down


def collision(player_rect, ball):
    if player_rect.colliderrect(ball):
        return True
    return False


def draw_text(text, font, surface, x, y):
    textobj = font.render(text, 1, (0, 0, 0))
    textrect = textobj.get_rect()
    textrect.topleft = x, y
    surface.blit(textobj, textrect)


def play():
    # setup pygame
    pygame.init()
    mainClock = pygame.time.Clock()

    pygame.display.set_caption('Pong')

    game_over_sound = pygame.mixer.Sound('game_over.wav')
    pygame.mixer.music.load('background.wav')
    font = pygame.font.Font(None, 48)

    # #Setup commands
    moveLeft = False
    moveRight = False
    moveUp = False
    moveDown = False
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
    net = pygame.Rect(WINDOWWIDTH /2 - 100, WINDOWHEIGHT /2, 150, 150)
    net_stretched = pygame.transform.scale(netImage, (150,150))


    windowSurface.fill(WHITE)
    draw_text('Pong', font, windowSurface, WINDOWWIDTH / 3, WINDOWHEIGHT / 3)
    draw_text('Press a key to start.', font, windowSurface, WINDOWWIDTH / 3 - 30,
              WINDOWHEIGHT / 3 + 50)
    pygame.display.update()
    get_input()
    top_score = 0
    play_game_again = True
    while play_game_again:
        # pygame.mixer.music.play(-1,0.0)

        play_game = True
        while play_game:
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
            ball.ball_obj.x += ball.velocity
            ball.ball_obj.y += ball.angle



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

            windowSurface.blit(player_middle_paddle_stretched, player_middle_paddle)
            windowSurface.blit(player_bottom_paddle_stretched, player_bottom_paddle)
            windowSurface.blit(player_top_paddle_stretched, player_top_paddle)

            windowSurface.blit(AI_middle_paddle_stretched, AI_middle_paddle)
            windowSurface.blit(AI_bottom_paddle_stretched, AI_bottom_paddle)
            windowSurface.blit(AI_top_paddle_stretched, AI_top_paddle)
            windowSurface.blit(ball.ball_Fixed, ball.ball_obj)
            pygame.display.update()


play()