import pygame
import random
import os
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("FLAPPY BIRDS")

background = pygame.image.load(os.path.join("Flappy Birds Game Assets", 'background.png'))
background = pygame.transform.scale(background, (800, 600))
base = pygame.image.load(os.path.join("Flappy Birds Game Assets", 'base.png'))
base = pygame.transform.scale(base,(800, 100))
intro = pygame.image.load(os.path.join("Flappy Birds Game Assets",'intro.png'))
intro = pygame.transform.scale(intro, (370, 450))
# bird
x = 100
y = 100
jump = 0
speed = 0.5
birdimg = pygame.image.load(os.path.join("Flappy Birds Game Assets",'bird.png'))
white = (255, 255, 255)


def draw_bird(x, y):
    screen.blit(birdimg, (x, y))


# pipes
pipeupimg = pygame.image.load(os.path.join("Flappy Birds Game Assets", 'pipe-up.png'))
pipedownimg = pygame.image.load(os.path.join("Flappy Birds Game Assets", 'pipe-down.png'))
pipe1 = [300, -170]
pipe2 = [550, -100]
pipe3 = [800, -30]
Pipes = []
Pipes.append(pipe1)
Pipes.append(pipe2)
Pipes.append(pipe3)
score_time = None


def draw_pipe(PIPE):
    screen.blit(pipeupimg, (PIPE[0], PIPE[1]))
    screen.blit(pipedownimg, (PIPE[0], PIPE[1] + 420))


# score
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)
sCoord = (10, 10)

exit_game = True
welcome_two = False
game_Exit = False


def game_Over():
    global game_Exit
    while game_Exit == True:
        screen.blit(background, (0, 0))
        font = pygame.font.SysFont("freesansbold.ttf", 64, True)
        message = font.render("Game Over!", True, (0, 0, 0))
        screen.blit(message, (0, 0))


def welcome():
    global exit_game, welcome_two, running
    while exit_game == True:
        screen.blit(background, (0, 0))
        font = pygame.font.SysFont("freesansbold.ttf", 64, True)
        message = font.render("Welcome!", True, (0, 0, 0))
        screen.blit(intro, (210, 10))
        font = pygame.font.SysFont("freesansbold.ttf", 50, True)
        message = font.render("Press SPACE To Begin !", True, (0, 0, 0))
        screen.blit(message, (170, 500))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    exit_game = False
                    welcome_two = True
            if event.type == pygame.QUIT:
                exit_game = False
                welcome_two = False
                running = False
        pygame.display.update()


def print_score(scr):
    screen.blit(font.render("Score: " + str(scr), True, (255, 255, 255)), sCoord)


# sounds
dieSound = pygame.mixer.Sound(os.path.join("Flappy Birds Game Assets", 'die.wav'))
hitSound = pygame.mixer.Sound(os.path.join("Flappy Birds Game Assets", 'hit.wav'))
swooshSound = pygame.mixer.Sound(os.path.join("Flappy Birds Game Assets", 'swoosh.wav'))
pointSound = pygame.mixer.Sound(os.path.join("Flappy Birds Game Assets", 'point.wav'))
wingSound = pygame.mixer.Sound(os.path.join("Flappy Birds Game Assets", 'wing.wav'))


def restart():
    global running, score_time, x, speed, Pipes
    for i in Pipes:
        # if i[0] < x:
        #     i[0] = x
        draw_pipe(i)
        i[0] -= 0
    current_time = pygame.time.get_ticks()
    if current_time > score_time + 500:
        running = False


running = True
while running:
    game_Over()
    screen.blit(background, (0, 0))
    welcome()
    if welcome_two == True:
        # screen.fill((120,120,255))

        # screen.blit(base, (0,410))
        if score_time:
            restart()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    wingSound.play()
                    jump = 1

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    jump = 0

        # bird movement
        draw_bird(x, y)
        if jump == 1:
            y -= 3
        else:
            y += 3

        # pipe movement
        for i in Pipes:
            draw_pipe(i)
            i[0] -= 2 # WHAT IS IT DOING??
            if i[0] <= -50:
                i[0] = 800
                i[1] = random.randint(-250, -100)

        # game over
        for i in Pipes:
            if i[0] == 100:
                if y <= i[1] + 320 or y >= i[1] + 420:
                    game_Exit = True
                    score_time = pygame.time.get_ticks()
                    hitSound.play()
                    dieSound.play()
                else:
                    # screen.blit(welcome)
                    pointSound.play()
                    score += 1

        print_score(score)
        screen.blit(base, (0, 510))
    pygame.display.update()