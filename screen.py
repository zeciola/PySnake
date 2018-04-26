import pygame
import RGBColor as rcolor
import random
from os import system

# Verificar erro

try:
    pygame.init()
except:
    print("pygame não foi iniciado com sucesso! "+pygame.init())

# display
largura = 640
altura = 480

# size
size = 10

background = pygame.display.set_mode((largura, altura))
font = pygame.font.SysFont(None, 15)

def text(msg, color):
    textInit = font.render(msg, True, color)
    background.blit(textInit, [largura/10, altura/2])


def display():
    background.fill(rcolor.white)
    pygame.display.set_caption("SnakePy")


def Snake(SnakeXY):
    for XY in SnakeXY:
        pygame.draw.rect(background, rcolor.black, [XY[0], XY[1], size, size])


def Apple(aX, aY):
    pygame.draw.rect(background, rcolor.red1, [x, y, size, size])

def Aleatory():
    resultX = 0
    resultY = 0
    
    randX = (largura - altura) / 10

    #print(randX)

    randY = (altura - largura) / 10

    #print(randY)

    #while randX < -7 and randY < (altura - 10) and randX < largura and randY < (altura - 10):

    if randX < 0:
        resultX = (random.randint(randX, 0))

    if randX > 0:
        resultY = (random.randint(0, randX))
    if randY > 0:
        resultY = (random.randint(0, randY))
    if randY < 0:
        resultY = (random.randint(randY, 0))

    return {'rX':resultX,'rY':resultY}


# def Keys(velocidadeX, velocidadeY):


# def LogicRules(x, y):


def Game():
    exit = True

    gameover = True

    
    velocidadeX = 0
    velocidadeY = 0

    clocktime = pygame.time.Clock()

    SnakeXY = []

    SnakeCont = 10

    aX = -42
    aY = -42

    #Apple(aX, aY)

    rX = (largura - altura) / 10

    rY = (altura - largura) / 10

    x = -42
    y = -42

    while x < -7 and y < -10 and x < 800 and y < 580:
        x = (random.randint(0, rX))
        y = (random.randint(rY, 600))


    x,y = Aleatory()['rX'], Aleatory()['rY']
    

    while exit:

        while gameover:
            background.fill(rcolor.white)

            text("Game Over /n Do you want to try again? ", rcolor.red4)

            pygame.display.update()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    exit = False
                    gameover = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        Game()
                    if event.key == pygame.K_n:
                        exit = False
                        gameover = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    exit = False
            if event.type == pygame.KEYDOWN:
            # corrigir bug
                if event.key == pygame.K_LEFT and velocidadeX != size:
                    velocidadeY = 0
                    velocidadeX = -size
                if event.key == pygame.K_RIGHT and velocidadeX != -size:
                    velocidadeY = 0
                    velocidadeX = size
                if event.key == pygame.K_UP and velocidadeY != size:
                    velocidadeX = 0
                    velocidadeY = -size
                if event.key == pygame.K_DOWN and velocidadeY != -size:
                    velocidadeX = 0
                    velocidadeY = size
                if event.key == pygame.K_ESCAPE:
                    exit = False

        #Keys(velocidadeX, velocidadeY)
        display()

        SnakeInit = []

        SnakeInit.append(x)
        SnakeInit.append(y)

        SnakeXY.append(SnakeInit)

        if len(SnakeXY) > SnakeCont:
            del SnakeXY[0]

        if any(Part == SnakeInit for Part in SnakeXY[:-1]):
            fimdejogo = True

        Snake(SnakeXY)

        if x == aX and y == aY:
            Apple(aX, aY)
            SnakeCont += 1

        x += velocidadeX
        y += velocidadeY

        Apple(aX, aY)
        
        clocktime.tick(15)

        pygame.display.update()

        print('x', x, ' y', y)

        system('clear')
        # Game Rules
        if x > largura:
            x = 0
        if x < 0:
            x = (largura - 10) - size
        if y > altura:
            y = 0
        if y < 0:
            y = (altura - 10) - size

# Snake


# exit loop


Game()
system('clear')
pygame.quit
