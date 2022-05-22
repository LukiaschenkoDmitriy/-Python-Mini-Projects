import pygame as pg
import math

pg.font.init()

class App:
	def __init__(self):
		self.RES = self.WIDTH,self.HEIGHT = 1200,900
		self.screen = pg.display.set_mode(self.RES)
		self.tick = pg.time.Clock()

		self.points = 1

		self.circle = self.createCircle(self.points,300)
		self.cardioida = self.createCardioida()

		self.pressed = []

		self.font = pg.font.SysFont('Arial',40)

	def createCircle(self,points,radius):
		circle = []
		
		for angle in range(0,int(360/points),1):
			angle *= points
			circle.append((self.WIDTH/2 + math.cos(math.radians(angle-90))*radius,self.HEIGHT/2 + math.sin(math.radians(angle-90))*radius))

		return circle

	def createCardioida(self):
		cardioida = []
		for num in range(len(self.circle)):
			if num*2 < len(self.circle):
				cardioida.append((self.circle[num],self.circle[num*2]))
			else:
				cardioida.append((self.circle[num],self.circle[int((num-(len(self.circle)/2))*2)]))


		return cardioida

	def draw(self):
		#for pos in self.circle:
			#pg.draw.circle(self.screen, pg.Color('orange'), (pos[0],pos[1]),1)

		for pos in self.cardioida:
			pg.draw.aaline(self.screen, pg.Color('orange'), (pos[0]),(pos[1]),1)

	def drawInfo(self):
		info = self.font.render('DBP:'+str(self.points),True,pg.Color('white'))
		rect = info.get_rect(center=(200,20))
		self.screen.blit(info,rect)

	def run(self):
		while True:
			self.screen.fill(pg.Color('darkslategray'))
			for event in pg.event.get():
				if event.type == pg.QUIT:
					quit()

				if event.type == pg.KEYDOWN:
					if event.key not in self.pressed:
						if event.key == pg.K_LEFT:
							self.pressed.append(event.key)

						elif event.key == pg.K_RIGHT:
							self.pressed.append(event.key)

						elif event.key == pg.K_UP:
							self.pressed = []

			if pg.K_LEFT in self.pressed:
				if self.points > 0.5:
					self.points -= .01
					self.circle = self.createCircle(self.points,300)
					self.cardioida = self.createCardioida()

			elif pg.K_RIGHT in self.pressed:
				self.points += .01
				self.circle = self.createCircle(self.points,300)
				self.cardioida = self.createCardioida()


			self.draw()
			self.drawInfo()

			pg.display.flip()
			self.tick.tick(60)

			pg.display.set_caption('cardioida')


if __name__ == "__main__":
	app = App()
	app.run()