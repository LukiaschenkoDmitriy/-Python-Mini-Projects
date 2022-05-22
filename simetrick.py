import pygame as pg
from random import randrange
RES = WIDTH,HEIGHT = 1200, 900
screen = pg.display.set_mode(RES)
pg.display.set_caption('Create and manipulation simetrick graficks')
pg.font.init()
font = pg.font.SysFont('Arial', 32)

def Font(text, pos, *args):
	if args:
		for num in args:
			fontRender = font.render(str(text) + ':' + str(num), True, pg.Color('white'))
	else:
		fontRender = font.render(str(text), True, pg.Color('white'))
	fontRect = fontRender.get_rect(center = pos)
	screen.blit(fontRender, fontRect)
	return fontRect

class Simetriya:
	def __init__(self):
		self.centerX = WIDTH/2
		self.centerY = HEIGHT/2
		self.List = [[],[]]
		self.sides = ['vertical', 'gorizontal', 'circle']
		self.click = False
		self.test = [0,1]

		self.i = 0

	def draw(self, lineColor = pg.Color('red'), side = 'vertical', color = pg.Color('white'), width = 1, autoCleaner = False, test = 0):
		if color == 'random':
			color = (randrange(0,255), randrange(0,255), randrange(0,255))

		if side == self.sides[1] or side not in self.sides:
			pg.draw.line(screen, lineColor, (0, self.centerY), (WIDTH, self.centerY))
			if pg.mouse.get_pressed()[0]:
				mouseX, mouseY = pg.mouse.get_pos()[0], pg.mouse.get_pos()[1]
				self.List[0].append((mouseX,mouseY))
				self.List[1].append((mouseX,-mouseY + HEIGHT))
				self.click = True

		if side == self.sides[0]:
			pg.draw.line(screen, lineColor, (self.centerX, 0), (self.centerX, HEIGHT))
			if pg.mouse.get_pressed()[0]:
				mouseX, mouseY = pg.mouse.get_pos()[0], pg.mouse.get_pos()[1]
				self.List[0].append((mouseX,mouseY))
				self.List[1].append((-mouseX + WIDTH,mouseY))
				self.click = True

		if side == self.sides[2]:
			pg.draw.line(screen, lineColor, (self.centerX, 0), (self.centerX, HEIGHT))
			pg.draw.line(screen, lineColor, (0, self.centerY), (WIDTH, self.centerY))
			if pg.mouse.get_pressed()[0]:
				mouseX, mouseY = pg.mouse.get_pos()[0], pg.mouse.get_pos()[1]
				self.List[0].append((mouseX,mouseY))
				self.List[1].append((-mouseX + WIDTH,-mouseY+HEIGHT))
				self.click = True

		if autoCleaner:
			if not pg.mouse.get_pressed()[0] and len(self.List[0]) >= 2:
				obj1 = self.List[0][-1]
				obj2 = self.List[1][-1]
				self.List[0].remove(obj1)
				self.List[1].remove(obj2)
				if len(self.List[0]) <= 3:
					self.List = [[],[]]

		if pg.mouse.get_pressed()[2]:
			self.List = [[],[]]


		if len(self.List[0]) >= 2:
			pg.draw.lines(screen, color, True, self.List[0], width)
			pg.draw.lines(screen, color, True, self.List[1], width)


		if test == self.test[1]:
			for obj1 in self.List[0]:
				for obj2 in self.List[1]:
					pg.draw.line(screen, pg.Color('red'), obj2, obj1, 1)

Simetrick = Simetriya()

while True:
	screen.fill((36, 36, 36))
	[quit() for event in pg.event.get() if event.type == pg.QUIT]

	Simetrick.draw(width = 3, autoCleaner = True, color = pg.Color('red'), side = 'gorizontal')

	#Functions
	pg.display.flip()