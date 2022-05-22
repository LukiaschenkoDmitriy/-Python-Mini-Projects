import pygame as pg
import math

screen = pg.display.set_mode((1200, 800))
pg.display.set_caption('Graphic Functions')
class Sin():
	def __init__(self):
		self.SinList = []
		self.CosList = []
		self.TgList = []
		self.CtgList = []
		self.centerX = 1200 / 2 + 200
		self.centerY = 800 / 2
		self.r = 100
		self.inter = 0.01
		self.speed = 0.5
		self.i_add = math.pi/100

		pg.font.init()
		defFont = pg.font.SysFont('Times New Roman', 32)
		self.defFont = defFont
		self.renderFont = defFont.render('Cos Function', True, pg.Color('white'))
		self.renderFont2 = defFont.render('Sin Function', True, pg.Color('white'))
		self.renderFont3 = defFont.render('Tang Function', True, pg.Color('white'))
		self.renderFont4 = defFont.render('CTang Function', True, pg.Color('white'))

		self.font_rect = self.renderFont.get_rect(center = (self.centerX- 250, self.centerY - 350))
		self.font_rect2 = self.renderFont2.get_rect(center = (self.centerX- 250, self.centerY - 70))
		self.font_rect3 = self.renderFont3.get_rect(center = (150, 100)) 
		self.font_rect4 = self.renderFont4.get_rect(center = (1050, 100))

	def createSin(self):
		x = self.centerX
		y = self.centerY + math.cos(self.inter) * self.r - 200
		y2 = self.centerY + math.sin(self.inter) * self.r + 100
		y4 = self.centerY + math.sin(self.inter)/math.cos(self.inter) * self.r
		y3 = self.centerY + math.cos(self.inter)/math.sin(self.inter) * self.r
		pg.draw.circle(screen, pg.Color('green'), (x, y), 3)
		pg.draw.circle(screen, pg.Color('red'), (x,y2), 3)
		pg.draw.circle(screen, pg.Color('yellow'), (250, y3), 3)
		pg.draw.circle(screen, pg.Color('blue'), (1200 - 50, y4), 3)
		self.CosList.append([x,y])
		self.SinList.append([x,y2])
		self.TgList.append([250,y3])
		self.CtgList.append([1200 - 50, y4])
		self.inter += self.i_add

	def font(self):
		screen.blit(self.renderFont, self.font_rect)
		screen.blit(self.renderFont2, self.font_rect2)
		screen.blit(self.renderFont3, self.font_rect3)
		screen.blit(self.renderFont4, self.font_rect4)

		renderSpeed = self.defFont.render('Speed:' + str(round(self.speed, 4)), True, pg.Color('white'))
		renderInterval = self.defFont.render('Iterval:' + str(round(self.i_add, 4)), True, pg.Color('white'))

		renderSpeed_rect = renderSpeed.get_rect(center = (350,100))
		renderInterval_rect = renderInterval.get_rect(center = (760, 100))

		screen.blit(renderSpeed, renderSpeed_rect)
		screen.blit(renderInterval, renderInterval_rect)


	def drawSin(self):
		for circle in self.CosList:
			if circle[0] <= 300:
				self.CosList.remove(circle)
			pg.draw.circle(screen, pg.Color('green'), (circle[0], circle[1]), 1)
			circle[0] -= self.speed

		for circle in self.SinList:
			if circle[0] <= 300:
				self.SinList.remove(circle)
			pg.draw.circle(screen, pg.Color('red'), (circle[0], circle[1]),1)
			circle[0] -= self.speed

		for circle in self.TgList:
			if circle[0] <= 10:
				self.TgList.remove(circle)
			pg.draw.circle(screen, pg.Color('yellow'), (circle[0], circle[1]),1)
			circle[0] -= self.speed

		for circle in self.CtgList:
			if circle[0] <= 900:
				self.CtgList.remove(circle)
			pg.draw.circle(screen, pg.Color('blue'), (circle[0], circle[1]),1)
			circle[0] -= self.speed

	def update(self):
		pg.display.update()
		screen.fill(pg.Color('black'))

	def main(self):
		while True:
			for event in pg.event.get():
				if event.type == pg.QUIT:
					quit()
				if event.type == pg.MOUSEBUTTONDOWN:
					if event.__dict__['button'] == 4:
						self.speed += 0.05
					elif event.__dict__['button'] == 5:
						if self.speed >= 0.05:
							self.speed -= 0.05
				if event.type == pg.KEYDOWN:
					if event.key == pg.K_w:
						self.i_add += 0.1
					elif event.key == pg.K_s:
						self.i_add -= 0.1
				if event.type == pg.KEYDOWN:
					if event.key == pg.K_SPACE:
						self.SinList = []
						self.CosList = []
						self.TgList = []
						self.CtgList = []
						self.r = 0.1
			self.createSin()
			self.drawSin()
			self.font()
			self.update()
			if self.r <= 100:
				self.r += 0.1
			if self.r >= 100:
				self.r = 0.1


if __name__ == '__main__':
	Sin().main()