import pygame as pg
RES = 1200,900

screen = pg.display.set_mode(RES)
pg.display.set_caption('SideBar')
pg.font.init()

class SideBar:
	def __init__(self, num = 0, minProgress = 0, maxProgress = 600, anim = True, speed = 1):
		self.x, self.y = centerX,centerY = RES[0]/2, RES[1]/2
		self.progress = minProgress
		self.maxProgress = maxProgress
		self.font = pg.font.SysFont('Arial', 32)
		if num < 0:
			num = 0
		self.num = num
		self.anim = anim
		self.speed = speed

	def line(self):
		pg.draw.line(screen, pg.Color('black'), (self.x - 310,self.y), (self.x + 310, self.y), 30)
		pg.draw.line(screen, pg.Color('white'), (self.x - 300,self.y), (self.x -300 + self.num, self.y), 20)
		if self.anim:
			self.num += self.speed
		if self.num >= self.maxProgress:
			self.num = 0

	def info(self):
		renderText = self.font.render(str(int(self.num/self.maxProgress*100)) + '%', True, pg.Color('white'))
		renderRect = renderText.get_rect(center = (self.x, self.y - 40))
		screen.blit(renderText,renderRect)


sb = SideBar(anim = True, speed = 1)

while True:
	screen.fill((37,37,37))
	for event in pg.event.get():
		if event.type == pg.QUIT:
			quit()

	sb.line()
	sb.info()
	pg.display.flip()

