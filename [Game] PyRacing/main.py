import pygame as pg 
from random import randint

RES = WIDTH,HEIGHT = 600,900
SCREEN = pg.display.set_mode(RES)
pg.display.set_caption('PyRacing')

blue_car = pg.image.load('images/blue_car.png')
red_car = pg.image.load('images/red_car.png')
road = pg.image.load('images/road.png')

class Block():
	def __init__(self,x,y,width=14,height=50):
		self.x,self.y = x,y
		self.width,self.height=width,height

	def draw(self):
		pg.draw.rect(SCREEN,pg.Color('white'), (self.x-self.width/2,self.y,self.width,self.height))


class Line():
	def __init__(self):
		self.line = [Block((x+1)*200-7,y*150) for x in range(2) for  y in range(10)]

	def draw(self,speed):
		for item in self.line:
			item.draw()
			if item.y > HEIGHT:
				item.y = -150
			else:
				item.y += speed

class check_change:
	def __init__(self):
		self.cur_pos = None

	def change(self, pos):
		if self.cur_pos == pos:
			return 0
		else:
			self.cur_pos = pos
			return 1

class Moving:
	def __init__(self):
		self.sum_steps = 0
		self.x = 0

	def move(self, max_steps, speed = 0.5):
		if self.sum_steps < max_steps:
			self.x += speed

			y = self.x

			self.sum_steps += y
			return y

		elif self.sum_steps > max_steps:
			prot = self.sum_steps
			self.sum_steps -= self.sum_steps - max_steps
			return -(prot - max_steps)
		return 0

ch = check_change()
move_player = Moving()


class Enemy:
	def __init__(self):
		self.x,self.y = (randint(0,2))*200+50, -200

	def draw(self,speed,a_s):
		SCREEN.blit(red_car, (self.x,self.y))
		self.y += speed+a_s

class Game:
	def __init__(self):
		self.x,self.y = WIDTH/2-50, HEIGHT-250
		self.Enemys = []
		self.line = Line()

		self.current_move = None

		self.cd = 0

		self.speed = 1
		self.apeend_speed = 1

		self.score = 0
		self.append_score = 1
		self.speed_plus = False

		self.pause = 0

		pg.font.init()

		self.font = pg.font.SysFont('Arial', 32)

	def pause_f(self):
		self.pause = 1
		self.append_score = 0
		self.apeend_speed = 0
		self.speed = 0

	def game_over(self):
		font_rend = self.font.render(('Game over'), True, pg.Color('White'))
		font_rend2 = self.font.render((f'You score:{int(self.score)}'), True, pg.Color('White'))
		font_rend3 = self.font.render(('Pressed SPACE to restart'), True, pg.Color('White'))
		font_rect = font_rend.get_rect(center=(WIDTH//2,HEIGHT//2))
		font_rect2 = font_rend2.get_rect(center=(WIDTH//2,HEIGHT//2+50))
		font_rect3 = font_rend3.get_rect(center=(WIDTH//2,HEIGHT//2+100))
		SCREEN.blit(font_rend,font_rect)
		SCREEN.blit(font_rend2,font_rect2)
		SCREEN.blit(font_rend3,font_rect3)

	def restart_game(self):
		self.__init__()

	def move(self):
		if self.current_move == 'left':
			self.x -= move_player.move(200)
			if not ch.change(self.x):
				move_player.x = 0
				move_player.sum_steps = 0
				self.current_move = None
		elif self.current_move == 'right':
			self.x += move_player.move(200)
			if not ch.change(self.x):
				move_player.x = 0
				move_player.sum_steps = 0
				self.current_move = None

	def events(self):
		for event in pg.event.get():
			if event.type == pg.QUIT:
				quit()
			if event.type == pg.KEYDOWN:
				if not self.pause:
					if not self.current_move:
						if event.key == pg.K_LEFT and self.x - 200 > 0:
							self.current_move = 'left'
						elif event.key == pg.K_RIGHT and self.x + 200 < WIDTH:
							self.current_move = 'right'

					if event.key == pg.K_UP:
						self.speed = 3
						self.speed_plus = True

				if self.pause:
					if event.key == pg.K_SPACE:
						self.restart_game()

			if event.type == pg.KEYUP:
				if not self.pause:
					if event.key == pg.K_UP:
						self.speed = 1
						self.speed_plus = False

		if self.speed_plus:
			self.score += self.append_score/100


	def spawn_enemy(self):
		if self.cd > 200:
			self.Enemys.append(Enemy())
			self.cd = 0
		else:
			self.cd += (randint(0,100)/75)+ (self.speed-1)/2

	def collide(self, enemy):
		if self.x == enemy.x and self.y <= enemy.y+200 and enemy.y <= self.y+200:
			self.pause_f()

	def text(self):
		font_rend = self.font.render('Score:'+str(int(self.score)), True, pg.Color('White'))
		SCREEN.blit(font_rend,(10,25))


	def main(self):
		while True:
			self.events()

			SCREEN.blit(road, (0,0))
			self.line.draw(self.speed)


			for en in self.Enemys:
				en.draw(self.speed, self.apeend_speed)
				self.collide(en)

				if en.y > HEIGHT+200:
					self.Enemys.remove(en)


			SCREEN.blit(blue_car,(self.x,self.y))
			self.spawn_enemy()
			if not self.pause:
				self.move()
			self.text()
			self.score += self.append_score/100

			if self.pause:
				self.game_over()

			pg.display.flip()


if __name__ == '__main__':
	Game().main()