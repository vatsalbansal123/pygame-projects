# import modules
import pygame
import random
import math
import os
# initialize pygame
pygame.init()

# screen
screen = pygame.display.set_mode((800, 600))

# title and icon
pygame.display.set_caption("SPACE INVADERS")
playerimg = pygame.image.load(os.path.join("Space Invaders Game Assets", 'si.png'))
pygame.display.set_icon(playerimg)

# background
background = pygame.image.load(os.path.join("Space Invaders Game Assets",'background.png'))
pygame.mixer.music.load(os.path.join("Space Invaders Game Assets","background.wav"))
pygame.mixer.music.play(-1)
# player

pX = 360
pY = 480
pXchange = 0
pYchange = 0
speed = 4


def player(x, y):
    screen.blit(playerimg, (x, y))


# enemy
enemyimg = []
eX = []
eY = []
eXchange = []
eYchange = []
num_of_enemy = 10

for i in range(num_of_enemy):
    enemyimg.append(pygame.image.load(os.path.join("Space Invaders Game Assets",'alien.png')))
    eX.append(random.randint(100, 700))
    eY.append(random.randint(100, 300))
    eXchange.append(3)
    eYchange.append(15)


def enemy(x, y, i):
    screen.blit(enemyimg[i], (x, y))


score_visible = True

# bullet
bulletimg = pygame.image.load(os.path.join("Space Invaders Game Assets",'bullet.png'))
bX = pX
bY = pY
bYchange = -10
bState = 0  # READY


def fire_bullet(x, y):
    global bState
    bState = 1  # FIRING
    screen.blit(bulletimg, (x, y))


# SCORE
score = 0
font = pygame.font.SysFont("freesansbold.ttf", 64, True)
sCoor = (10, 10)
welcome = False
welcome_two = False


def score_print(scr):
    if score_visible == True:
        screen.blit(font.render("Score: "+ str(score), True, (255, 255, 255)), sCoor)


def isCollision(EX, EY, BX, BY):
    distance = math.sqrt((BX-EX) ** 2+(BY-EY) ** 2)
    if distance <= 30:
        return True
    return False


def game_over_text(scr):
    global running
    font = pygame.font.SysFont("freesansbold.ttf", 64, True)
    msg = font.render("Game Over !", True, (255, 255, 255))
    mCoor = (400 - msg.get_width()/2, 200)
    screen.blit(msg, mCoor)
    font = pygame.font.SysFont("freesansbold.ttf", 62, True)
    fs =  font.render("Final Score: " + str(scr), True, (255, 255, 255))
    fsCorr = (400- fs.get_width()/2, 300)
    screen.blit(fs, fsCorr)


def welcome_page():
    global welcome, welcome_two, running
    if welcome_two == False:
        font = pygame.font.SysFont("freesansbold.ttf", 64, True)
        message = font.render("Welcome To Space Invaders", True, (255, 255, 255))
        message_coor = (400 - message.get_width()/2, 200)
        screen.blit(message, message_coor)
        font = pygame.font.SysFont("freesansbold.ttf", 40, True)
        moves = font.render("Press Left Key or Right Key to move Left or Right", True, (255, 255, 255))
        moves_coor = (400 - moves.get_width()/2, 250)
        screen.blit(moves, moves_coor)
        font = pygame.font.SysFont("freesansbold.ttf", 40, True)
        moves_three = font.render("Press Up Key or Down Key to move Up or Down", True, (255, 255, 255))
        moves_coor_three = (400 - moves.get_width() / 2, 280)
        screen.blit(moves_three, moves_coor_three)
        font = pygame.font.SysFont("freesansbold.ttf", 40, True)
        moves_two = font.render("And press Space to shoot", True, (255, 255, 255))
        moves_two_coor =  (400 - moves_two.get_width()/2, 310)
        screen.blit(moves_two, moves_two_coor)
        font = pygame.font.SysFont("freesansbold.ttf", 40, True)
        key =  font.render("Press SPACE to continue", True, (255, 255, 255))
        key_coor = (400, 550)
        screen.blit(key, key_coor)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                welcome_two = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    welcome = True
                    welcome_two = True


running = True
while running:
    screen.fill((40, 40, 40))
    screen.blit(background, (0, 0))
    welcome_page()
    if welcome == True:
        for event in pygame.event.get():
            # QUIT
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT: pXchange = -speed
                if event.key == pygame.K_RIGHT: pXchange = speed
                if event.key == pygame.K_UP: pYchange = -speed
                if event.key == pygame.K_DOWN: pYchange = speed
                if event.key == pygame.K_SPACE:
                    bSound = pygame.mixer.Sound(os.path.join("Space Invaders Game Assets",'laser.wav'))
                    bSound.play()
                    bX, bY = pX, pY
                    fire_bullet(bX, bY)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    pXchange = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    pYchange = 0

        # player movement
        pX += pXchange
        pY += pYchange
        if pX <= 0:
            pX = 736
        elif pX >= 736:
            pX = 0
        player(pX, pY)

        # enemy movement
        for i in range(num_of_enemy):
            if eX[i] < pX and eX[i]  > pX - 64 and eY[i] < pY and eY[i] > pY - 64:
                for j in range(num_of_enemy):
                    eY[j] = 800
                game_over_text(score)
                score_visible =  False
                break
            if eY[i] >= 400:
                for j in range(num_of_enemy):
                    eY[j] = 800
                game_over_text(score)
                break
            eX[i] += eXchange[i]  # eXchange=3  eYchange=15
            if eX[i] >= 736:
                eY[i] += eYchange[i]
                eXchange[i] = -eXchange[i] + 0.002
            if eX[i] <= 0:
                eY[i] += eYchange[i]
                eXchange[i] = -eXchange[i] + 0.002

            collision = isCollision(eX[i], eY[i], bX, bY)
            if collision:
                eX[i] = random.randint(100, 700)
                eY[i] = random.randint(100, 300)
                bState = 0
                score += 1
            enemy(eX[i], eY[i], i)
        # bullet movement
        if bState == 1:
            fire_bullet(bX, bY)
            bY += bYchange  # bYchange = -10
            if bY <= 0:
                bState = 0
        score_print(score)
        pygame.draw.line(screen, (255, 0, 0), (0, 500), (800, 500), 5)
    pygame.display.update()