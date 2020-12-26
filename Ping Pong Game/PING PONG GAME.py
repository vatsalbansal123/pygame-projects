import pygame
import random
import os
pygame.init()

sw = 800
sh = 600

screen = pygame.display.set_mode((sw,sh))
pygame.display.set_caption("PING-PONG")
clock = pygame.time.Clock()
bg_color = pygame.Color('grey12')
game_font = pygame.font.Font('freesansbold.ttf', 60)

level = 1
opponent_speed = 6
running = True
score_time = None
paddle = True
start = False
colour = 1
color = (200, 200, 200)


def paddle_colour():
    global paddle, running, screen, bg_color, WelcomeScreen, start, colour, color
    if paddle == True:
        screen.fill(bg_color)
        if colour == 1:
            pygame.draw.rect(screen, (255, 255, 255), (44, 95, 161, 80))
        if colour == 2:
            pygame.draw.rect(screen, (255, 255, 255), (44, 195, 161, 80))
        if colour == 3:
            pygame.draw.rect(screen, (255, 255, 255), (44, 295, 161, 80))
        if colour == 4:
            pygame.draw.rect(screen, (255, 255, 255), (44, 395, 161, 80))
        if colour == 5:
            pygame.draw.rect(screen, (255, 255, 255), (44, 495, 161, 80))
        if colour == 6:
            pygame.draw.rect(screen, (255, 255, 255), (314, 95, 161, 80))
        if colour == 7:
            pygame.draw.rect(screen, (255, 255, 255), (314, 195, 161, 80))
        if colour == 8:
            pygame.draw.rect(screen, (255, 255, 255), (314, 295, 161, 80))
        if colour == 9:
            pygame.draw.rect(screen, (255, 255, 255), (314, 395, 161, 80))
        if colour == 10:
            pygame.draw.rect(screen, (255, 255, 255), (314, 495, 161, 80))
        if colour == 11:
            pygame.draw.rect(screen, (255, 255, 255), (584, 95, 161, 80))
        if colour == 12:
            pygame.draw.rect(screen, (255, 255, 255), (584, 195, 161, 80))
        if colour == 13:
            pygame.draw.rect(screen, (255, 255, 255), (584, 295, 161, 80))
        if colour == 14:
            pygame.draw.rect(screen, (255, 255, 255), (584, 395, 161, 80))
        if colour == 15:
            pygame.draw.rect(screen, (255, 255, 255), (584, 495, 161, 80))
        font = pygame.font.Font('freesansbold.ttf', 40)
        Welcome_Message = font.render("CHOOSE THE COLOUR OF THE PADDLE", True, (200, 200, 200))
        screen.blit(Welcome_Message, (4, 20))
        pygame.draw.rect(screen, (200, 200, 200), (50, 100, 150, 70))
        number_one = font.render("A", True, (0, 0, 0))
        screen.blit(number_one, (110, 110))
        pygame.draw.rect(screen, (255, 0, 0), (50, 200, 150, 70))
        number_one = font.render("B", True, (0, 0, 0))
        screen.blit(number_one, (110, 210))
        pygame.draw.rect(screen, (0, 255, 0), (50, 300, 150, 70))
        number_one = font.render("C", True, (0, 0, 0))
        screen.blit(number_one, (110, 310))
        pygame.draw.rect(screen, (0, 0, 255), (50, 400, 150, 70))
        number_one = font.render("D", True, (0, 0, 0))
        screen.blit(number_one, (110, 410))
        pygame.draw.rect(screen, (255, 153, 255), (50, 500, 150, 70))
        number_one = font.render("E", True, (0, 0, 0))
        screen.blit(number_one, (110, 510))
        pygame.draw.rect(screen, (255, 255, 0), (320, 100, 150, 70))
        number_one = font.render("F", True, (0, 0, 0))
        screen.blit(number_one, (380, 110))
        pygame.draw.rect(screen, (0, 255, 255), (320, 200, 150, 70))
        number_one = font.render("G", True, (0, 0, 0))
        screen.blit(number_one, (380, 210))
        pygame.draw.rect(screen, (255, 0, 102), (320, 300, 150, 70))
        number_one = font.render("H", True, (0, 0, 0))
        screen.blit(number_one, (380, 310))
        pygame.draw.rect(screen, (255, 102, 102), (320, 400, 150, 70))
        number_one = font.render("I", True, (0, 0, 0))
        screen.blit(number_one, (380, 410))
        pygame.draw.rect(screen, (204, 51, 0), (320, 500, 150, 70))
        number_one = font.render("J", True, (0, 0, 0))
        screen.blit(number_one, (375, 510))
        pygame.draw.rect(screen, (255, 255, 153), (590, 100, 150, 70))
        number_one = font.render("K", True, (0, 0, 0))
        screen.blit(number_one, (645, 110))
        pygame.draw.rect(screen, (153, 51, 153), (590, 200, 150, 70))
        number_one = font.render("L", True, (0, 0, 0))
        screen.blit(number_one, (645, 210))
        pygame.draw.rect(screen, (0, 102, 0), (590, 300, 150, 70))
        number_one = font.render("M", True, (0, 0, 0))
        screen.blit(number_one, (645, 310))
        pygame.draw.rect(screen, (255, 255, 255), (590, 400, 150, 70))
        number_one = font.render("N", True, (0, 0, 0))
        screen.blit(number_one, (645, 410))
        pygame.draw.rect(screen, (153, 51, 51), (590, 500, 150, 70))
        number_one = font.render("O", True, (0, 0, 0))
        screen.blit(number_one, (645, 510))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                paddle = False
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paddle = False
                    start = True
                if event.key == pygame.K_a:
                    color = (200, 200, 200)
                    colour = 1
                if event.key == pygame.K_b:
                    color = (255, 0, 0)
                    colour = 2
                if event.key == pygame.K_c:
                    color = (0, 255, 0)
                    colour = 3
                if event.key == pygame.K_d:
                    color = (0, 0, 255)
                    colour = 4
                if event.key == pygame.K_e:
                    color = (255, 153, 255)
                    colour = 5
                if event.key == pygame.K_f:
                    color = (255, 255, 0)
                    colour = 6
                if event.key == pygame.K_g:
                    color = (0, 255, 255)
                    colour = 7
                if event.key == pygame.K_h:
                    color = (255, 0, 102)
                    colour = 8
                if event.key == pygame.K_i:
                    color = (255, 102, 102)
                    colour = 9
                if event.key == pygame.K_j:
                    color = (204, 51, 0)
                    colour = 10
                if event.key == pygame.K_k:
                    color = (255, 255, 153)
                    colour = 11
                if event.key == pygame.K_l:
                    color = (153, 51, 153)
                    colour = 12
                if event.key == pygame.K_m:
                    color = (0, 102, 0)
                    colour = 13
                if event.key == pygame.K_n:
                    color = (255, 255, 255)
                    colour = 14
                if event.key == pygame.K_o:
                    color = (153, 51, 51)
                    colour = 15


def Start_Game(OS):
    global score_time, running, start, color
    sw = 800
    sh = 600
    screen = pygame.display.set_mode((sw,sh))

    ball = pygame.Rect(sw//2-15, sh//2-15, 30, 30)
    player = pygame.Rect(sw-20, sh//2-60, 10, 120)
    opponent = pygame.Rect(10, sh//2-60, 10, 120)

    bg_color = pygame.Color('grey12')

    ball_speed_x = 6 * random.choice((-1,1))
    ball_speed_y = 6 * random.choice((-1,1))

    player_speed = 0
    opponent_speed = OS
    ball_colour = [200, 200, 200]
    player_score = 0
    opponent_score = 0
    game_font = pygame.font.Font('freesansbold.ttf',32)

    def ball_restart():
        global ball_speed_x, ball_speed_y, sw, sh, score_time, color

        ball.center = (sw//2, sh//2)
        current_time = pygame.time.get_ticks()

        if current_time - score_time < 700:
            ball_speed_x = 0
            ball_speed_y = 0
            number_three = game_font.render("3", False, color)
            screen.blit(number_three, (sw//2-8, sh//2+50))

        elif 700 < current_time - score_time < 1400:
            ball_speed_x = 0
            ball_speed_y = 0
            number_two = game_font.render("2", False, color)
            screen.blit(number_two, (sw//2-8, sh//2+50))

        elif 1400 < current_time - score_time < 2100:
            ball_speed_x = 0
            ball_speed_y = 0
            number_one = game_font.render("1", False, color)
            screen.blit(number_one, (sw//2-8, sh//2+50))

        elif current_time - score_time > 2100:
            ball_speed_x = 7*random.choice((-1,1))
            ball_speed_y = 7*random.choice((-1,1))
            score_time = None

    running = True
    while running:
        paddle_colour()
        if start == True:
            screen.fill(bg_color)
            msg = game_font.render("COMPUTER", True,color)
            screen.blit(msg, (80, 80))
            msg_two = game_font.render("YOU", True, color)
            screen.blit(msg_two, (550, 80))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        player_speed += 7
                    if event.key == pygame.K_UP:
                        player_speed -= 7

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_DOWN:
                        player_speed -= 7
                    if event.key == pygame.K_UP:
                        player_speed += 7

            # ball movement
            ball.x += ball_speed_x
            ball.y += ball_speed_y
            if ball.top <= 0 or ball.bottom >= sh:
                ball_speed_y *= -1

            if ball.left <= 0:
                player_score += 1
                # ball_speed_x += 0.5
                score_time = pygame.time.get_ticks()

            if ball.right >= sw:
                opponent_score += 1
                # ball_speed_x += 0.5
                score_time = pygame.time.get_ticks()
            if player.top < ball.top and player.bottom > ball.bottom and ball.right > player.left:
                ball_colour[0] = random.randint(0, 255)
                ball_colour[1] = random.randint(0, 255)
                ball_colour[2] = random.randint(0, 255)
                ball_speed_x *= -1
            if opponent.top < ball.top and opponent.bottom > ball.bottom and ball.left < opponent.right:
                ball_colour[0] = random.randint(0, 255)
                ball_colour[1] = random.randint(0, 255)
                ball_colour[2] = random.randint(0, 255)
                ball_speed_x *= -1

            if score_time:
                ball_restart()

            # player movement
            player.y += player_speed
            if player.top <= 0:
                player.top = 0
            if player.bottom >= sh:
                player.bottom = sh

            # opponent movement
            if opponent.bottom < ball.y:
                opponent.bottom += opponent_speed
            if opponent.top > ball.y:
                opponent.top -= opponent_speed

            if opponent.top <= 0:
                opponent.top = 0
            if opponent.bottom >= sh:
                opponent.bottom = sh

            pygame.draw.rect(screen, color, player)
            pygame.draw.rect(screen, color, opponent)
            pygame.draw.ellipse(screen, ball_colour, ball)
            pygame.draw.aaline(screen, color, (sw/2,0), (sw/2,sh))

            player_text = game_font.render(f"{player_score}", False, color)
            screen.blit(player_text, (sw//2+20, sh//2-16))

            opponent_text = game_font.render(f"{opponent_score}", False, color)
            screen.blit(opponent_text, (sw//2-42, sh//2-16))

        pygame.display.update()
        clock.tick(60)


WelcomeScreen = True
while WelcomeScreen:
    screen.fill(bg_color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            WelcomeScreen = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                WelcomeScreen = False
                paddle = True
                Start_Game(opponent_speed)
            if event.key == pygame.K_1:
                opponent_speed = 6
                level = 1
            if event.key == pygame.K_2:
                opponent_speed = 10
                level = 2
            if event.key == pygame.K_3:
                opponent_speed = 15
                level = 3

    if level == 1:
        pygame.draw.rect(screen, (255,0,0), pygame.Rect(sw//2-190, sh-410, 350, 70),  2)
    elif level == 2:
        pygame.draw.rect(screen, (255,0,0), pygame.Rect(sw//2-190, sh-310, 350, 70),  2)
    elif level == 3:
        pygame.draw.rect(screen, (255,0,0), pygame.Rect(sw//2-190, sh-210, 350, 70),  2)

    Welcome_Message = game_font.render("PING - PONG", True, (200,200,200))
    screen.blit(Welcome_Message, (sw//2-170, 20))

    Select_Level = game_font.render("SELECT LEVEL", True, (200,200,200))
    screen.blit(Select_Level, (sw//2-200, sh-500))

    Easy = game_font.render("EASY", True, (200,200,200))
    screen.blit(Easy, (sw//2-90, sh-400))

    Medium = game_font.render("MEDIUM", True, (200,200,200))
    screen.blit(Medium, (sw//2-130, sh-300))

    Hard = game_font.render("HARD", True, (200,200,200))
    screen.blit(Hard, (sw//2-90, sh-200))

    Start = game_font.render("PRESS SPACE TO START", True, (200,200,200))
    screen.blit(Start, (sw//2-360, sh-100))

    clock.tick(60)
    pygame.display.update()

