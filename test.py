import random

largura = 640
altura = 480
margem = 10



def Aleatory():
    resultX = 0
    resultY = 0
    bol = True

    randX = (largura - altura) / 10

    print(randX)

    randY = (altura - largura) / 10

    print(randY)

    # while randX < -7 and randY < (altura - 10) and randX < largura and randY < (altura - 10):

    if randX < 0:
        resultX = (random.randint(randX, largura))
        bol = True
        while bol == True:
            resultX = (random.randint(randX, largura))
            if resultX < -7:
                bol = False
    if randX > 0:
        resultX = (random.randint(0, randX))
        bol = True
        while bol == True:
            resultX = (random.randint(0, randX))
            if resultX < largura:
                bol = False
    if randY > 0:
        resultY = (random.randint(0, randY))
        bol = True
        while bol == True:
            resultY = (random.randint(0, randY))
            if resultY <= (altura - 10):
                bol = False
    if randY < 0:
        resultY = (random.randint(randY, altura))
        bol = True
        while bol == True:
            resultY = (random.randint(randY, altura))
            if resultY <= (altura - 10):
                bol = False

    return {'rX': resultX, 'rY': resultY}


x = -42
y = -42

print('x = ', x, 'y = ', y)

x = Aleatory()['rX']
y = Aleatory()['rY']

print('rand x = ', x, "\nrand y = ", y)
