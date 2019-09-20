import pygame
import sys
import random
from pygame.locals import *

# setup window
WINDOWWIDTH = 960
WINDOWHEIGHT = 540
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)

# Setup colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RANDOM = (123, 45, 95)


MOVESPEED = 5


class Ball:
    ball_obj = pygame.Rect(WINDOWWIDTH / 2, WINDOWHEIGHT / 2, 40, 20)
    velocity = 0
    angle = 0
    ball_Image = pygame.image.load('ball.png')
    ball_Fixed = pygame.transform.scale(ball_Image, (40, 20))


class score:
    player_Score = 0
    AI_Score = 0


Ball.velocity = random.randint(-1, 1)
Ball.angle = random.randint(-5, 5)


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
                if e.key == K_p:
                    play()
                return  # start game for any other key down


def collision(player_rect, ball):
    if player_rect.colliderect(ball.ball_obj):
        return True
    return False


def ai_command(play_rect, ball):
    if play_rect.right - ball.ball_obj.x < 50:
        return True
    return False


def draw_text(text, font, surface, x, y):
    textobj = font.render(text, 1, (0, 0, 0))
    textrect = textobj.get_rect()
    textrect.topleft = x, y
    surface.blit(textobj, textrect)


def reset_ball():
    Ball.ball_obj.x = WINDOWWIDTH / 2
    Ball.ball_obj.y = WINDOWHEIGHT / 2
    Ball.velocity = random.randint(-1, 1)
    Ball.angle = random.randint(-5, 5)


def play():

    pygame.init()
    mainclock = pygame.time.Clock()

    pygame.display.set_caption('Pong')
    hit_noise = pygame.mixer.Sound('contact.wav')
    game_over_sound = pygame.mixer.Sound('game_over.wav')
    pygame.mixer.music.load('background.wav')
    font = pygame.font.Font(None, 48)

    # #Setup commands
    moveleft = False
    moveright = False
    moveup = False
    movedown = False

    paddle_image = pygame.image.load('spongebob.gif')

    player_middle_paddle = pygame.Rect(WINDOWWIDTH-100, WINDOWHEIGHT / 2, 100, 100)
    player_middle_paddle_stretched = pygame.transform.scale(paddle_image, (100, 100))

    player_top_paddle = pygame.Rect(WINDOWWIDTH-100, 0, 100, 100)
    player_top_paddle_stretched = pygame.transform.scale(paddle_image, (100, 100))

    player_bottom_paddle = pygame.Rect(WINDOWWIDTH - 100, WINDOWHEIGHT - 100, 100, 100)
    player_bottom_paddle_stretched = pygame.transform.scale(paddle_image, (100, 100))

    ai_middle_paddle = pygame.Rect(0, WINDOWHEIGHT / 2, 200, 100)
    ai_middle_paddle_stretched = pygame.transform.scale(paddle_image, (100, 100))

    ai_top_paddle = pygame.Rect(0, 0, 100, 100)
    ai_top_paddle_stretched = pygame.transform.scale(paddle_image, (100, 100))

    ai_bottom_paddle = pygame.Rect(0, WINDOWHEIGHT - 100, 100, 100)
    ai_bottom_paddle_stretched = pygame.transform.scale(paddle_image, (100, 100))

    netimage = pygame.image.load('net.png')
    net = pygame.Rect(WINDOWWIDTH / 2 - 100, WINDOWHEIGHT / 2, 150, 150)
    net_stretched = pygame.transform.scale(netimage, (150, 150))

    windowSurface.fill(WHITE)
    draw_text('Pong', font, windowSurface, WINDOWWIDTH / 3, WINDOWHEIGHT / 3)
    draw_text('Press a key to start.', font, windowSurface, WINDOWWIDTH / 3 - 30,
              WINDOWHEIGHT / 3 + 50)
    pygame.display.update()
    get_input()
    play_game_again = True
    while play_game_again:
        pygame.mixer.music.play(-1, 0.0)

        play_game = True
        while play_game:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    # change the keyboard variables
                    if event.key == K_LEFT:
                        moveright = False
                        moveleft = True
                    if event.key == K_RIGHT:
                        moveleft = False
                        moveright = True
                    if event.key == K_UP:
                        movedown = False
                        moveup = True
                    if event.key == K_DOWN:
                        moveup = False
                        movedown = True
                if event.type == KEYUP:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == K_LEFT:
                        moveleft = False
                    if event.key == K_RIGHT:
                        moveright = False
                    if event.key == K_UP:
                        moveup = False
                    if event.key == K_DOWN:
                        movedown = False

            windowSurface.fill(WHITE)
            Ball.ball_obj.x += Ball.velocity
            Ball.ball_obj.y += Ball.angle

            if movedown and player_middle_paddle.bottom < WINDOWHEIGHT:
                player_middle_paddle.top += MOVESPEED
            if moveup and player_middle_paddle.top > 0:
                player_middle_paddle.top -= MOVESPEED
            if moveleft and player_top_paddle.left > WINDOWWIDTH / 2:
                player_top_paddle.left -= MOVESPEED
                player_bottom_paddle.left -= MOVESPEED
            if moveright and player_top_paddle.right < WINDOWWIDTH:
                player_top_paddle.right += MOVESPEED
                player_bottom_paddle.right += MOVESPEED

            if collision(player_bottom_paddle, Ball) or collision(player_top_paddle, Ball) \
                    or collision(player_middle_paddle, Ball):
                Ball.velocity = -Ball.velocity
                Ball.angle = random.randint(-5, 5)
                hit_noise.play()
            if collision(ai_bottom_paddle, Ball) or collision(ai_top_paddle, Ball) or collision(ai_middle_paddle, Ball):
                Ball.velocity = -Ball.velocity
                Ball.angle = random.randint(-5, 5)
                hit_noise.play()

            windowSurface.blit(player_middle_paddle_stretched, player_middle_paddle)
            windowSurface.blit(player_bottom_paddle_stretched, player_bottom_paddle)
            windowSurface.blit(player_top_paddle_stretched, player_top_paddle)

            windowSurface.blit(ai_middle_paddle_stretched, ai_middle_paddle)
            windowSurface.blit(ai_bottom_paddle_stretched, ai_bottom_paddle)

            windowSurface.blit(net_stretched, net)
            windowSurface.blit(ai_top_paddle_stretched, ai_top_paddle)
            windowSurface.blit(Ball.ball_Fixed, Ball.ball_obj)
            draw_text(str(score.AI_Score), font, windowSurface, 100, WINDOWHEIGHT / 2)
            draw_text(str(score.player_Score), font, windowSurface, WINDOWWIDTH - 100, WINDOWHEIGHT / 2)

            if Ball.ball_obj.x > WINDOWWIDTH:
                score.AI_Score += 1
                draw_text(str(score.AI_Score), font, windowSurface, 100, WINDOWHEIGHT / 2)
                reset_ball()
            elif Ball.ball_obj.x < 0:
                score.player_Score += 1
                draw_text(str(score.AI_Score), font, windowSurface, WINDOWWIDTH - 100, WINDOWHEIGHT / 2)
                reset_ball()
            elif Ball.ball_obj.y > WINDOWHEIGHT and Ball.ball_obj.x > WINDOWWIDTH / 2:
                score.AI_Score += 1
                draw_text(str(score.AI_Score), font, windowSurface, 100, WINDOWHEIGHT / 2)
                reset_ball()
            elif Ball.ball_obj.y > WINDOWHEIGHT and Ball.ball_obj.x < WINDOWWIDTH / 2:
                score.player_Score += 1
                draw_text(str(score.player_Score), font, windowSurface, WINDOWWIDTH - 100, WINDOWHEIGHT / 2)
                reset_ball()
            elif Ball.ball_obj.y < 0 and Ball.ball_obj.x > WINDOWWIDTH / 2:
                score.AI_Score += 1
                draw_text(str(score.AI_Score), font, windowSurface, 100, WINDOWHEIGHT / 2)
                reset_ball()
            elif Ball.ball_obj.y < 0 and Ball.ball_obj.x < WINDOWWIDTH / 2:
                score.player_Score += 1
                draw_text(str(score.player_Score), font, windowSurface, WINDOWWIDTH - 100, WINDOWHEIGHT / 2)
                reset_ball()

            elif Ball.ball_obj.y < 0 and Ball.ball_obj.x == WINDOWWIDTH / 2:
                reset_ball()
            elif Ball.ball_obj.y > WINDOWHEIGHT and Ball.ball_obj.x == WINDOWWIDTH / 2:
                reset_ball()
            if score.AI_Score > 11 or score.player_Score > 11:
                if score.AI_Score - score.player_Score == 2:
                    draw_text(str("AI WINS"), font, windowSurface, WINDOWWIDTH/2 - 100, WINDOWHEIGHT / 2)
                    game_over_sound.play()
                else:
                    draw_text(str("Player WINS"), font, windowSurface, WINDOWWIDTH/2 - 100, WINDOWHEIGHT / 2)
                    game_over_sound.play()
                draw_text(str("Press P to play again"), font, windowSurface,
                          WINDOWWIDTH / 2 - 200, WINDOWHEIGHT / 2 - 200)
                draw_text(str("Press Escape to exit"), font, windowSurface, 
                          WINDOWWIDTH / 2 - 200, WINDOWHEIGHT / 2 - 300)
                pygame.display.update()
                get_input()
                pygame.display.update()

            pygame.display.update()
            mainclock.tick(60)


play()
