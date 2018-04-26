import random

largura = 640
altura = 480

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

x = -42
y = -42

#print('x = ',x, 'y = ', y)

x = Aleatory()['rX']
y = Aleatory()['rY']

#print ('rand x = ',x,"\n rand y = ", y)