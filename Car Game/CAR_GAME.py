import os
import pygame
import random
import time
pygame.init()


def draw_road():
    global y, y_change
    game_Display.blit(background, (0, y))
    game_Display.blit(background, (0, y - display_height))
    if road_state == 1:
        y_change = 8
    if road_state == 2:
        y_change = 10
    if road_state == 3:
        y_change = 14
    y += y_change
    if y >= +display_height:
        y = 0


def message_to_screen(msg, colour):
    font = pygame.font.Font(None, 75)
    scree_text = font.render(msg, True, colour)
    game_Display.blit(scree_text, (420-(scree_text.get_width()/2), display_height/2))


def events():
    global car_x_change, enemy_car_x, enemy_car_y, enemy_car_change, coin_y_change, y_change
    global run
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                car_x_change = -10
            if event.key == pygame.K_RIGHT:
                car_x_change = 10
            if event.key == pygame.K_SPACE:
                y_change = 15
                enemy_car_change = 20
                coin_y_change = 15
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                car_x_change = 0
            if event.key == pygame.K_RIGHT:
                car_x_change = 0
            if event.key == pygame.K_SPACE:
                y_change = 10
                enemy_car_change = 10
                coin_y_change = 10


def game_end_line():
    global gameFinish, car_x, car_y, car_x_change, key_y, key_x, key_collect, enemy_car, enemy_car_y, enemy_car_change, enemy_car_x, coin_x, coin_y, coin_y_change
    global run, trophy, coin_collect, gameOver, welcome_five, coin_time, score
    while gameFinish:
        message = "SCORE:" + str(score)
        font = pygame.font.Font(None, 55)
        screen = font.render(message, True, (0, 0, 0))
        game_Display.blit(background, (0, 0))
        game_Display.blit(enemy_car, (enemy_car_x, enemy_car_y))
        game_Display.blit(car, (car_x, car_y))
        game_Display.blit(screen, (0, 0))
        font = pygame.font.Font(None, 75)
        message_to_screen("YOU WON!", (0, 0, 0))
        font = pygame.font.Font(None, 55)
        message = "COINS:" + str(coin_collect)
        screen = font.render(message, True, (0, 0, 0))
        game_Display.blit(screen, (0, 50))
        game_Display.blit(trophy, (330, 100))
        game_Display.blit(screen, (0, 50))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                gameFinish = False


def game_over():
    global gameOver, car_x, car_y, car_x_change, enemy_car_x, enemy_car_y, enemy_car_change, key_collect, key_two, key_three
    global run, score, coin_collect, coin_y, buttons, welcome, welcome_five, welcome_two, coin_x, coin_y, coin_y_change, coin_time
    while gameOver:  # I have changed gameOver == True to gameOver only.
        message = "SCORE:" + str(score)
        font = pygame.font.Font(None, 55)
        screen = font.render(message, True, (0, 0, 0))
        game_Display.blit(background, (0, 0))
        game_Display.blit(enemy_car, (enemy_car_x, enemy_car_y))
        game_Display.blit(car, (car_x, car_y))
        game_Display.blit(screen, (0, 0))
        game_Display.blit(coin, (coin_x, coin_y))
        font = pygame.font.Font(None, 55)
        message = "COINS:" + str(coin_collect)
        screen = font.render(message, True, (0, 0, 0))
        game_Display.blit(screen, (0, 50))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed(3)
        if key_collect >= 1:
            game_Display.blit(buttons, (220, 280))
            if 287 + 265 > mouse[0] > 287 and 347 + 65 > mouse[1] > 347:
                font = pygame.font.SysFont("freesansbold.ttf", 45, True)
                msg = font.render("RESTART", True, (0, 0, 0))
                game_Display.blit(msg, (340, 364))
                if click[0] == 1:
                    key_collect = 0
                    gameOver = False
                    welcome_five = True
                    car_x = 355
                    score = 0
                    coin_collect = 0
                    coin_y = -300
                    car_y = display_height / 2 + 130
                    enemy_car_x = 300
                    enemy_car_y = -700
                    enemy_car_change = 10
                    car_x_change = 0
                    car_x = 300
                    coin_x = 200
                    coin_y = -1000
                    coin_y_change = 10
                    coin_time = 0
            else:
                font = pygame.font.SysFont("freesansbold.ttf", 55, True)
                msg = font.render("RESTART", True, (0, 0, 0))
                game_Display.blit(msg, (320, 360))
            # quit button
            if 287 + 265 > mouse[0] > 287 and 552 + 65 > mouse[1] > 552:
                font = pygame.font.SysFont("freesansbold.ttf", 45, True)
                msg2 = font.render("QUIT", True, (0, 0, 0))
                game_Display.blit(msg2, (378, 565))
                if click[0] == 1:
                    gameOver = False
                    welcome = False
                    run = False
            else:
                font = pygame.font.SysFont("freesansbold.ttf", 55, True)
                msg2 = font.render("QUIT", True, (0, 0, 0))
                game_Display.blit(msg2, (365, 560))
            # level button
            if 287 + 265 > mouse[0] > 287 and 445 + 65 > mouse[1] > 445:
                font = pygame.font.SysFont("freesansbold.ttf", 45, True)
                msg2 = font.render("USE", True, (0, 0, 0))
                game_Display.blit(msg2, (350, 467))
                game_Display.blit(key_three, (440, 465))
                if click[0] == 1:
                    key_collect = 0
                    gameOver = False
                    welcome_five = True
                    coin_y = -300
                    car_y = display_height / 2 + 130
                    enemy_car_x = 300
                    enemy_car_y = -700
                    enemy_car_change = 10
                    car_x_change = 0
                    car_x = 300
                    coin_x = 200
                    coin_y = -1000
                    coin_y_change = 10
                    coin_time = 0
            else:
                font = pygame.font.SysFont("freesansbold.ttf", 55, True)
                msg2 = font.render("USE", True, (0, 0, 0))
                game_Display.blit(msg2, (335, 460))
                game_Display.blit(key_two, (430, 455))
        else:
            game_Display.blit(buttons_two, (220, 280))
            if 287 + 265 > mouse[0] > 287 and 347 + 65 > mouse[1] > 347:
                font = pygame.font.SysFont("freesansbold.ttf", 45, True)
                msg = font.render("RESTART", True, (0, 0, 0))
                game_Display.blit(msg, (340, 364))
                if click[0] == 1:
                    key_collect = 0
                    gameOver = False
                    welcome_five = True
                    car_x = 355
                    score = 0
                    coin_collect = 0
                    coin_y = -300
                    car_y = display_height / 2 + 130
                    enemy_car_x = 300
                    enemy_car_y = -700
                    enemy_car_change = 10
                    car_x_change = 0
                    coin_x = 200
                    coin_y = -1000
                    coin_y_change = 10
                    coin_time = 0
            else:
                font = pygame.font.SysFont("freesansbold.ttf", 55, True)
                msg = font.render("RESTART", True, (0, 0, 0))
                game_Display.blit(msg, (320, 360))
            if 287 + 265 > mouse[0] > 287 and 445 + 65 > mouse[1] > 445:
                font = pygame.font.SysFont("freesansbold.ttf", 45, True)
                msg2 = font.render("QUIT", True, (0, 0, 0))
                game_Display.blit(msg2, (368, 458))
                if click[0] == 1:
                    gameOver = False
                    welcome = False
                    run = False
            else:
                font = pygame.font.SysFont("freesansbold.ttf", 55, True)
                msg2 = font.render("QUIT", True, (0, 0, 0))
                game_Display.blit(msg2, (360, 455))
        font = pygame.font.Font(None, 70)
        msg = font.render("YOU CRASHED !", True, (0, 0, 0))
        game_Display.blit(msg, (420 - msg.get_width()/2, display_height/2 - 100))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                gameOver = False


def score_display():
    hit_box = [car_x + 5, car_y, 90, 200]
    global score, flag_x, flag_y, flag_change, enemy_car_change, gameFinish, pointSound
    if enemy_car_y > 670:
        score = score + 1
        pointSound.play()
    if score == 15:
        game_Display.blit(flag, (flag_x, flag_y))
        enemy_car_change = 0
        flag_change = 10
        flag_y += flag_change
        game_Display.blit(car, (car_x, car_y))
        if hit_box[1] + hit_box[3] < flag_y:
            gameFinish = True
    font = pygame.font.Font(None, 55)
    message = "SCORE:" + str(score)
    screen = font.render(message, True, (0, 0, 0))
    game_Display.blit(screen, (0, 0))


def enemy_car_display():
    global enemy_car_y, enemy_car_x, enemy_car_change, road_state
    if enemy_car_y > 670:
        enemy_car_x = random.randint(135, 550)
        enemy_car_y = -450
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    enemy_car_change = 15
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    enemy_car_change = 10
    game_Display.blit(enemy_car, (enemy_car_x, enemy_car_y))
    if road_state == 1:
        enemy_car_change = 8
    if road_state == 2:
        enemy_car_change = 10
    if road_state == 3:
        enemy_car_change = 14
    enemy_car_y += enemy_car_change


def player_car_display():
    global car_x
    game_Display.blit(car, (car_x, car_y))
    car_x += car_x_change


def collision():
    global gameOver
    hit_box = [car_x + 5, car_y, 90, 200]
    enemy_hit_box = [enemy_car_x + 10, enemy_car_y, 78, 170]
    # car collision
    if hit_box[0] + hit_box[2] > enemy_hit_box[0] and hit_box[0] < enemy_hit_box[0] + enemy_hit_box[2]:
        if hit_box[1] + hit_box[3] > enemy_hit_box[1] and hit_box[1] < enemy_hit_box[1] + enemy_hit_box[3]:
            gameOver = True
    # boundary collision
    if hit_box[0] <= 135 or hit_box[0] + 125 >= 710:
        gameOver = True


def coin_display():
    global coin_y,  coin_y_change, coin_x, score, coin_collect, road_state
    hit_box = [car_x + 5, car_y, 90, 200]
    coin_hit_box = [coin_x, coin_y + 8, 64, 58]
    font = pygame.font.Font(None, 55)
    message = "COINS:" + str(coin_collect)
    screen = font.render(message, True, (0, 0, 0))
    game_Display.blit(screen, (0, 50))
    game_Display.blit(coin, (coin_x, coin_y))
    coin_y += coin_y_change
    if road_state == 1:
        coin_y_change = 8
    if road_state == 2:
        coin_y_change = 10
    if road_state == 3:
        coin_y_change = 14
    if coin_y > 670:
        coin_x = random.randint(135, 550)
        coin_y = -450
        if road_state == 1:
            coin_y_change = 8
        if road_state == 2:
            coin_y_change = 10
        if road_state == 3:
            coin_y_change = 14


def welcome_page():
    global run, welcome_two, welcome, welcome_five, buttons, level, level_state, y_change, road_state, score_time
    if welcome_two:
        y_change = 10
        font = pygame.font.SysFont("freesansbold.ttf", 64, True)
        message = font.render("Welcome To ROAD FIGHTER !", True, (0, 0, 0))
        message_coord = (400 - message.get_width()/2, 150)
        game_Display.blit(message, message_coord)
        font = pygame.font.SysFont("freesansbold.ttf", 40, True)
        moves = font.render("Press Left Key or Right Key to move Left or Right", True, (0, 0, 0))
        moves_coord = (400 - moves.get_width()/2, 200)
        game_Display.blit(moves, moves_coord)
        font = pygame.font.SysFont("freesansbold.ttf", 40, True)
        moves_two = font.render("Collect coins and keys to revive on the way !", True, (0, 0, 0))
        moves_coor_two = (400 - moves_two.get_width() / 2, 250)
        game_Display.blit(moves_two, moves_coor_two)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed(3)
        game_Display.blit(buttons, (220, 280))

        # start button
        if 287 + 265 > mouse[0] > 287 and 347 + 65 > mouse[1] > 347:
            font = pygame.font.SysFont("freesansbold.ttf", 45, True)
            msg = font.render("START", True, (0, 0, 0))
            game_Display.blit(msg, (360, 364))
            if click[0] == 1:
                score_time = pygame.time.get_ticks()
                welcome_five = True
                welcome = True
                welcome_two = False
                if road_state == 1:
                    y_change = 10
                if road_state == 2:
                    y_change = 15
                if road_state == 3:
                    y_change = 20
        else:
            font = pygame.font.SysFont("freesansbold.ttf", 55, True)
            msg = font.render("START", True, (0, 0, 0))
            game_Display.blit(msg, (350, 360))
        # quit button
        if 287 + 265 > mouse[0] > 287 and 552 + 65 > mouse[1] > 552:
            font = pygame.font.SysFont("freesansbold.ttf", 45, True)
            msg2 = font.render("QUIT", True, (0, 0, 0))
            game_Display.blit(msg2, (378, 565))
            if click[0] == 1:
                run = False
                welcome_two = False
        else:
            font = pygame.font.SysFont("freesansbold.ttf", 55, True)
            msg2 = font.render("QUIT", True, (0, 0, 0))
            game_Display.blit(msg2, (365, 560))
        # level button
        if 287 + 265 > mouse[0] > 287 and 445 + 65 > mouse[1] > 445:
            font = pygame.font.SysFont("freesansbold.ttf", 45, True)
            msg2 = font.render("LEVEL", True, (0, 0, 0))
            game_Display.blit(msg2, (360, 467))
            if click[0] == 1:
                time.sleep(0.2)
                level_state = True
                welcome_two = False
        else:
            font = pygame.font.SysFont("freesansbold.ttf", 55, True)
            msg2 = font.render("LEVEL", True, (0, 0, 0))
            game_Display.blit(msg2, (350, 460))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                welcome_two = False


def countdown():
    global background, car_y, car_x, coin_collect, score, welcome_four, welcome, welcome_five, welcome_two, start_sound
    if welcome_five:
        welcome_two = False
        game_Display.blit(background, (0, y))
        game_Display.blit(car, (car_x, car_y))
        message = "SCORE:" + str(score)
        font = pygame.font.Font(None, 55)
        screen = font.render(message, True, (0, 0, 0))
        game_Display.blit(screen, (0, 0))
        message = "COINS:" + str(coin_collect)
        coin_msg = font.render(message, True, (0, 0, 0))
        game_Display.blit(coin_msg, (0, 50))
        game_Display.blit(background, (0, 0))
        game_Display.blit(car, (car_x, car_y))
        message = "SCORE:" + str(score)
        font = pygame.font.Font(None, 55)
        screen = font.render(message, True, (0, 0, 0))
        game_Display.blit(screen, (0, 0))
        message = "COINS:" + str(coin_collect)
        coin_msg = font.render(message, True, (0, 0, 0))
        game_Display.blit(coin_msg, (0, 50))
        pygame.display.update()
        start_sound.play()
        time.sleep(2)
        welcome_four = True
        welcome_five = False


def difficulty_levels():
    global level_state, run, welcome_two, welcome_five, welcome, y_change, road_state
    if level_state:
        welcome_two = False
        font = pygame.font.SysFont("freesansbold.ttf", 64, True)
        message = font.render("Welcome To ROAD FIGHTER !", True, (0, 0, 0))
        message_coord = (400 - message.get_width() / 2, 150)
        game_Display.blit(message, message_coord)
        font = pygame.font.SysFont("freesansbold.ttf", 40, True)
        moves = font.render("Press Left Key or Right Key to move Left or Right", True, (0, 0, 0))
        moves_coord = (400 - moves.get_width() / 2, 200)
        game_Display.blit(moves, moves_coord)
        font = pygame.font.SysFont("freesansbold.ttf", 40, True)
        moves_two = font.render("Collect coins and keys to revive on the way !", True, (0, 0, 0))
        moves_coor_two = (400 - moves_two.get_width() / 2, 250)
        game_Display.blit(moves_two, moves_coor_two)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed(3)
        game_Display.blit(buttons, (220, 280))
        if 287 + 265 > mouse[0] > 287 and 347 + 65 > mouse[1] > 347:
            font = pygame.font.SysFont("freesansbold.ttf", 45, True)
            msg = font.render("EASY", True, (0, 0, 0))
            game_Display.blit(msg, (367, 364))
            if click[0] == 1:
                road_state = 1
                time.sleep(0.1)
                level_state = False
                welcome_two = True
                # welcome_five = True
                # welcome = True
                # welcome_two = False
                # level_state = False
        else:
            font = pygame.font.SysFont("freesansbold.ttf", 55, True)
            msg = font.render("EASY", True, (0, 0, 0))
            game_Display.blit(msg, (360, 360))
        # quit button
        if 287 + 265 > mouse[0] > 287 and 552 + 65 > mouse[1] > 552:
            font = pygame.font.SysFont("freesansbold.ttf", 45, True)
            msg2 = font.render("HARD", True, (0, 0, 0))
            game_Display.blit(msg2, (365, 565))
            if click[0] == 1:
                road_state = 3
                time.sleep(0.1)
                level_state = False
                welcome_two = True
        else:
            font = pygame.font.SysFont("freesansbold.ttf", 55, True)
            msg2 = font.render("HARD", True, (0, 0, 0))
            game_Display.blit(msg2, (360, 560))
        # level button
        if 287 + 265 > mouse[0] > 287 and 445 + 65 > mouse[1] > 445:
            font = pygame.font.SysFont("freesansbold.ttf", 45, True)
            msg2 = font.render("MEDIUM", True, (0, 0, 0))
            game_Display.blit(msg2, (350, 467))
            if click[0] == 1:
                time.sleep(0.1)
                road_state = 2
                level_state = False
                welcome_two = True
        else:
            font = pygame.font.SysFont("freesansbold.ttf", 55, True)
            msg2 = font.render("MEDIUM", True, (0, 0, 0))
            game_Display.blit(msg2, (335, 460))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                level_state = False
                run = False
                welcome_two = False


def life_key():
    global key, key_x, key_y, key_y_change, road_state, coin_time, car_y, car_x, key_collect, key_two
    key_hit_box = [key_x + 6, key_y + 4, 96, 85]
    hit_box = [car_x + 5, car_y, 90, 200]
    print(key_collect)
    if key_collect >= 1:
        game_Display.blit(key_two, (780, 20))
    if key_collect == 2:
        game_Display.blit(key_two, (720, 20))
    if key_hit_box[1] > hit_box[1] and key_hit_box[1] + key_hit_box[3] > hit_box[1]:
        if key_hit_box[0] > hit_box[0] and key_hit_box[0] + key_hit_box[2] > hit_box[0]:
            key_collect += 1
            coin_time += 1
            key_y = -10000
            key_x = random.randint(135, 550)
            key_y_change = 10
        elif key_hit_box[0] + key_hit_box[2] > hit_box[0] and hit_box[0] > key_hit_box[0]:
            key_collect += 1
            coin_time += 1
            key_y = -10000
            key_x = random.randint(135, 550)
            key_y_change = 10
        elif hit_box[0] < key_hit_box[0] and hit_box[0] + hit_box[2] > key_hit_box[0] + key_hit_box[2]:
            key_collect += 1
            coin_time += 1
            key_y = -10000
            key_x = random.randint(135, 550)
            key_y_change = 10
    if coin_time < 2:
        game_Display.blit(key, (key_x, key_y))
    if road_state == 1:
        key_y_change = 8
    if road_state == 2:
        key_y_change = 10
    if road_state == 3:
        key_y_change = 14
    if key_y >= 670:
        coin_time += 1
        key_x = random.randint(135, 550)
        key_y = -500000000
        if road_state == 1:
            key_y_change = 8
        if road_state == 2:
            key_y_change = 10
        if road_state == 3:
            key_y_change = 14
    key_y += key_y_change


def is_collision_coin():
    global coin_collect, coin_y, coin_x, coin_y_change
    hit_box = [car_x + 5, car_y, 90, 200]
    coin_hit_box = [coin_x, coin_y + 8, 64, 58]
    if coin_hit_box[1] > hit_box[1] and coin_hit_box[1] + coin_hit_box[3] > hit_box[1]:
        if hit_box[0] < coin_hit_box[0] and hit_box[0] + hit_box[2] > coin_hit_box[0] + coin_hit_box[2]:
            coin_collect += 2
            coin_x = random.randint(135, 550)
            coin_y = -450
            coin_y_change = 10
        elif hit_box[0] > coin_hit_box[0] and coin_hit_box[0] + coin_hit_box[2] > hit_box[0]:
            coin_collect += 2
            coin_x = random.randint(135, 550)
            coin_y = -450
            coin_y_change = 10
        elif hit_box[0] < coin_hit_box[0] and hit_box[0] + hit_box[2] > coin_hit_box[0]:
            coin_collect += 2
            coin_x = random.randint(135, 550)
            coin_y = -450
            coin_y_change = 10


trophy = pygame.image.load(os.path.join("Car Game Assets", "trophy 2.png"))
trophy = pygame.transform.scale(trophy, (200, 200))
key_collect = 0
key = pygame.image.load(os.path.join("Car Game Assets", "key 2.png"))
key = pygame.transform.scale(key, (100, 100))
key_two = pygame.transform.scale(key, (50, 50))
key_three = pygame.transform.scale(key, (40, 40))
score_time = None
road_state = 0
level_state = False
buttons = pygame.image.load(os.path.join("Car Game Assets", "BUTTONS.png"))
buttons = pygame.transform.scale(buttons, (400, 400))
buttons_two = pygame.image.load(os.path.join("Car Game Assets", "BUTTONS_TWO.png"))
buttons_two = pygame.transform.scale(buttons_two, (380, 250))
y_change = 10
welcome_five = False
welcome_four = False
welcome_three = False
welcome_two = True
welcome = False
coin = pygame.image.load(os.path.join("Car Game Assets", "dollar.png"))
car = pygame.image.load(os.path.join("Car Game Assets", "car5.png"))
enemy_car = pygame.image.load(os.path.join("Car Game Assets", "car op 4.png"))
start_sound = pygame.mixer.Sound(os.path.join("Car Game Assets", "car start.wav"))
pointSound = pygame.mixer.Sound(os.path.join("Car Game Assets", "point.wav"))
car = pygame.transform.rotate(car, 270)
car = pygame.transform.scale(car, (100, 200))
enemy_car = pygame.transform.rotate(enemy_car, 270)
enemy_car = pygame.transform.scale(enemy_car, (100, 194))
flag = pygame.image.load(os.path.join("Car Game Assets", "finish3.png"))
flag = pygame.transform.scale(flag, (570, 300))
FPS = 100
display_width = 840
display_height = 670
clock = pygame.time.Clock()
game_Display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("ROAD FIGHTER")
pygame.display.set_icon(car)
background = pygame.image.load(os.path.join("Car Game Assets", "background.png"))
background = pygame.transform.scale(background, (840, 670))
coin_x = 200
coin_y = -1000
coin_y_change = 10
coin_time = 0
key_x = 300
key_y = -7000
key_y_change = 10
car_x = 355
car_y = display_height / 2 + 130
enemy_car_x = 300
enemy_car_y = -700
enemy_car_change = 10
car_x_change = 0
run = True
y = 0
gameOver = False
gameFinish = False
score = 0
flag_x = 140
flag_y = -250
flag_change = 0
coin_collect = 0
while run:
    draw_road()
    welcome_page()
    difficulty_levels()
    game_over()
    if welcome:
        countdown()
        events()
        game_end_line()
        score_display()
        enemy_car_display()
        player_car_display()
        collision()
        coin_display()
        is_collision_coin()
        life_key()
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
quit()