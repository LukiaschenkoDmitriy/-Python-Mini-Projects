import pygame as pg
from math import sin, cos
from random import randrange

RES = WIDTH, HEIGHT = 1600, 1000
centerX,centerY = WIDTH //2, HEIGHT //2

pg.init()
pg.font.init()
screen = pg.display.set_mode(RES, flags = pg.RESIZABLE)
time = pg.time.Clock()

drawGraph = ([])

def Button(x, y,
		   text,
		   color = pg.Color('red'),
		   font = 'Times New Roman',
		   sizeF = 22,
		   width = 0,
		   height = 0,
		   bg = pg.Color('white'),
		   cdColor = pg.Color('black'),
		   wCord = 2,
		   cdLine = False,
		   command = False):
	#Draw button
	defFont = pg.font.SysFont(font, sizeF)
	rendfFont = defFont.render(text, True, color)
	rectFont = rendfFont.get_rect(center = (x, y))
	pg.draw.rect(screen, bg, (rectFont[0] - width, rectFont[1] - height, rectFont[2] + width, rectFont[3] + height))
	if cdLine:
		pg.draw.rect(screen, cdColor, (rectFont[0] - width, rectFont[1] - height, rectFont[2] + width/2, rectFont[3] + height/2), wCord) 
	screen.blit(rendfFont, (rectFont[0] - width/2, rectFont[1] - height/2, rectFont[2], rectFont[3]))
	rectFont = pg.Rect(rectFont[0] - width/2, rectFont[1] - height/2, rectFont[2], rectFont[3])
	try:
		if pg.mouse.get_pressed()[0]:
			mouse_pos = pg.mouse.get_pos()
			if rectFont.collidepoint(mouse_pos):
				command
	except Exception as e:
		raise


def createObj(n = 1,r = 200):
	objBase = {}
	for i in range(n):
		objBase[i] = {'x' : None, 'y' : None, 'x`' : None, 'y`' : None, 'speed' : randrange(-100, 100)/100, 'appendN' : 0, 'r' : r/(i + 1)}
	return objBase, n

def fastDrawCircle(x, y, r, width = 2, color = pg.Color('white')):
	pg.draw.circle(screen, color, (x,y), r, width)

def fastDrawLine(x, y, xSh, ySh, width = 1, color = pg.Color('white')):
	pg.draw.line(screen, color, (x,y), (xSh, ySh), width)

def drawDot(xSh,ySh, r = 4, color = pg.Color('red')):
	pg.draw.circle(screen, color, (xSh, ySh), r)

def drawingGraph(listGraph):
	for n in range(len(listGraph)):
		if n != 0:
			x = listGraph[n - 1][0]
			y = listGraph[n - 1][1]
			xSh = listGraph[n][0]
			ySh = listGraph[n][1]
			pg.draw.line(screen, pg.Color('green'), (x,y), (xSh, ySh), 2)


class Graph():
	def __init__(self, r = 200, n = 4):
		pg.font.init()
		self.objects = createObj(n, r)
		self.r = r
		self.n = self.objects[1]
		self.objects = self.objects[0]
		self.drawGraph = ([])
		self.draw_on = True

	def drawObj(self):
		for obj_num in self.objects:
			obj = self.objects[obj_num]
			obj_speed = obj['speed']
			obj_r = obj['r']
			if obj_num == 0:
				#get varriables
				x = obj['x'] = int(centerX)
				y = obj['y'] = int(centerY)
				xSh = obj['x`'] = round(x + cos(obj['appendN']) * obj_r, 5)
				ySh = obj['y`'] = round(y + sin(obj['appendN']) * obj_r, 5)

			else:
				x = obj['x'] = round(self.objects[obj_num - 1]['x`'], 5)
				y = obj['y'] = round(self.objects[obj_num - 1]['y`'], 5)
				xSh = obj['x`'] = round(x + cos(obj['appendN']) * obj_r, 5)
				ySh = obj['y`'] = round(y + sin(obj['appendN']) * obj_r, 5)

			if self.draw_on:
				if obj_num == (self.n - 1):
					self.drawGraph.append([xSh,ySh])

				fastDrawCircle(x = x,y = y, r = obj_r)
				fastDrawLine(x = x, y = y, xSh = xSh, ySh = ySh,)
				drawDot(xSh = xSh, ySh = ySh)
				obj['appendN'] += obj_speed

			#Buttons
			Button(x = 150, y = 100, color = pg.Color('black'), text = 'ESP - New Graph', cdLine = True, width = 40, height=30)
			Button(x = 150, y = 200, color = pg.Color('black'), text = 'Space - Stop Drawing', cdLine = True, width = 40, height=30)
			drawingGraph(self.drawGraph)

	def event(self):
		for event in pg.event.get():
			if event.type == pg.QUIT:
				quit()

			if event.type == pg.KEYDOWN:
				if event.key == pg.K_SPACE:
					self.draw_on = False

				if event.key == pg.K_ESCAPE:
					for i in range(self.n):
						self.objects[i] = {'x' : None, 'y' : None, 'x`' : None, 'y`' : None, 'speed' : int(randrange(-10, 20)) / 10, 'appendN' : 0, 'r' : self.r/(i * 2 + 1)}
						self.drawGraph = ([])
					self.draw_on = True

	def main(self):
		while True:
			self.drawObj()
			self.event()
			pg.display.update()
			screen.fill(pg.Color('black'))

if __name__ == '__main__':
	Graph(250, 20).main()