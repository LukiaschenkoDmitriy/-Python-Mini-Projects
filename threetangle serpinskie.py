import pygame as pg
from random import randint
pg.init()

RES = WIDTH,HEIGHT = 1200,900
screen = pg.display.set_mode((RES))

WIDTH -= 100
HEIGHT -= 100
point1 = [(randint(0,WIDTH),randint(0,HEIGHT)),pg.Color('blue')]
point2 = [(randint(0,WIDTH),randint(0,HEIGHT)),pg.Color('red')]
point3 = [(randint(0,WIDTH),randint(0,HEIGHT)),pg.Color('green')]

currentPoint = [randint(0,WIDTH),randint(0,HEIGHT)]
randomNum = None
newDot = []

def operationOfDot():
	global currentPoint,randomNum
	for i in range(100000):
		newdotX = 0
		newdotY = 0
		randomNum = randint(0,6)
		if 0 <= randomNum <= 1: #move to first dot
			newdotX = (point1[0][0] + currentPoint[0])/2
			newdotY = (point1[0][1] + currentPoint[1])/2
			currentPoint = [newdotX,newdotY]
			newDot.append([newdotX,newdotY])

		elif 2 <= randomNum <= 3: #move to second dot
			newdotX = (point2[0][0] + currentPoint[0])/2
			newdotY = (point2[0][1] + currentPoint[1])/2
			currentPoint = [newdotX,newdotY]
			newDot.append([newdotX,newdotY])

		elif 4 <= randomNum <= 5: #move to second dot
			newdotX = (point3[0][0] + currentPoint[0])/2
			newdotY = (point3[0][1] + currentPoint[1])/2
			currentPoint = [newdotX,newdotY]
			newDot.append([newdotX,newdotY])

operationOfDot()

while True:
	screen.fill((36,36,36))
	for event in pg.event.get():
		if event.type == pg.QUIT:
			quit()

	for dot in newDot:
		pg.draw.circle(screen, pg.Color('yellow'), dot, 1)

	pg.draw.circle(screen, point1[1], point1[0],5)
	pg.draw.circle(screen, point2[1], point2[0],5)
	pg.draw.circle(screen, point3[1], point3[0],5)

	pg.draw.circle(screen, pg.Color('orange'), (currentPoint[0],currentPoint[1]),4)

	pg.display.flip()