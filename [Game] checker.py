import pygame as pg

pg.init()
pg.font.init()

RESOL = WIDTH, HEIGHT = 1202, 802
screen = pg.display.set_mode(RESOL)
time = pg.time.Clock()

font = pg.font.SysFont('Arial', 24)

def drawFigure(x,y, color, screen = screen):
	pg.draw.circle(screen, pg.Color(color), (x + 40,y + 40), 35)

#Board
sizeCell = 80
boardSize = 800
rows,cols = boardSize//sizeCell, boardSize//sizeCell
FPS = 30

class cell():
	def __init__(self,x,y, sizeCell = sizeCell):
		self.indexSeachIn2DList = lambda x,y: y + x * rows

		self.x = x
		self.y = y
		self.size = sizeCell

		self.index = self.x if (self.y % 2) == 0 else self.x + 1
		self.parity = True if (self.index % 2) == 0 else False

		self.team = None
		self.figure = {'None' : True, 'Checker' : False, 'King' : False}
		self.object = None

		#set figures
		if not self.parity and 4 > self.y > -1:
			self.figure['Checker'] = True
			self.team = 'black'
			self.figure['None'] = False
		elif not self.parity and cols> self.y > (cols - 5):
			self.figure['Checker'] = True
			self.team = 'white'
			self.figure['None'] = False

	def cellDr(self):
		x = self.x * self.size
		y = self.y * self.size
		if self.parity:
			pg.draw.rect(screen, (242, 223, 145), (x,y, self.size, self.size))
			return False
		else:
			rect = pg.draw.rect(screen, (71, 74, 65), (x,y, self.size, self.size))
			return rect

	def drawFigure(self):
		if self.team:
			drawFigure(self.x * self.size, self.y * self.size,self.team)

	def move(self, neigborns):
		if neigborns:
			if pg.mouse.get_pressed()[0]:
				mousePos = pg.mouse.get_pos()
				for cell in neigborns:
					rect = pg.Rect(cell.x * cell.size,cell.y * cell.size, cell.size, cell.size)
					if rect.collidepoint(mousePos):
						if cell.team == None:
							if self.team == 'white':
								cell.team = 'white'
								self.team = None
							elif self.team == 'black':
								cell.team = 'black'
								self.team = None
							self.figure['None'] = True
							self.figure['Checker'] = False
							self.figure['King'] = False
							cell.figure['None'] = False
							cell.figure['Checker'] = True
							cell.figure['King'] = False
							return True

	def currentCellDr(self):
		x = self.x * self.size
		y = self.y * self.size
		pg.draw.circle(screen, pg.Color('green'), (x + 40, y + 40), 37, width = 3)

	def neigbornDr(self):
		x = self.x * self.size
		y = self.y * self.size
		pg.draw.circle(screen, pg.Color('purple'), (x + 40, y + 40), 37, width = 3)

	def neigbornDrEnemy(self):
		x = self.x * self.size
		y = self.y * self.size
		pg.draw.circle(screen, pg.Color('red'), (x + 40, y + 40), 37, width = 3)

	def setNeigborns(self, cells):
		neigborns = []
		enemy = []
		#Neigborns
		if self.team == 'white':
			#leftTop
			if self.x - 1 >= 0 and self.y - 1 >= 0:
				cellNeighborn = cells[self.indexSeachIn2DList(self.x - 1, self.y - 1)]
				if cellNeighborn.figure['None']:
					neigborns.append(cellNeighborn)
			#rightTop
			if self.x + 1 <= rows - 1 and self.y - 1 >= 0:
				cellNeighborn = cells[self.indexSeachIn2DList(self.x + 1, self.y - 1)]
				if cellNeighborn.figure['None']:
					neigborns.append(cellNeighborn)
		if self.team == 'black':
			#leftBottom
			if self.x - 1 >= 0 and self.y + 1 <= rows - 1:
				cellNeighborn = cells[self.indexSeachIn2DList(self.x - 1, self.y + 1)]
				if cellNeighborn.figure['None']:
					neigborns.append(cellNeighborn)
			#rightBottom
			if self.x + 1 <= rows - 1 and self.y + 1 <= rows - 1:
				cellNeighborn = cells[self.indexSeachIn2DList(self.x + 1, self.y + 1)]
				if cellNeighborn.figure['None']:
					neigborns.append(cellNeighborn)
		#Enemy
		if self.team == 'white':
			#leftTop
			if self.x - 2 >= 0 and self.y - 2 >= 0:
				cellNeighborn = cells[self.indexSeachIn2DList(self.x - 1, self.y - 1)]
				if cellNeighborn.team == 'black':
					if cellNeighborn.figure['Checker']:
						cellNeighborn2 = cells[self.indexSeachIn2DList(self.x - 2, self.y - 2)]
						if cellNeighborn2.figure['None']:
							enemy.append(cellNeighborn)
			#rightTop
			if self.x + 2 <= rows - 1 and self.y - 2 >= 0:
				cellNeighborn = cells[self.indexSeachIn2DList(self.x + 1, self.y - 1)]
				if cellNeighborn.team == 'black':
					if cellNeighborn.figure['Checker']:
						cellNeighborn2 = cells[self.indexSeachIn2DList(self.x + 2, self.y - 2)]
						if cellNeighborn2.figure['None']:
							enemy.append(cellNeighborn)
			#leftBottom
			if self.x - 2 >= 0 and self.y + 2 <= rows - 1:
				cellNeighborn = cells[self.indexSeachIn2DList(self.x - 1, self.y + 1)]
				if cellNeighborn.team == 'black':
					if cellNeighborn.figure['Checker']:
						cellNeighborn2 = cells[self.indexSeachIn2DList(self.x - 2, self.y + 2)]
						if cellNeighborn2.figure['None']:
							enemy.append(cellNeighborn)
			#rightBottom
			if self.x + 2 <= rows - 1 and self.y + 2 <= rows - 1:
				cellNeighborn = cells[self.indexSeachIn2DList(self.x + 1, self.y + 1)]
				if cellNeighborn.team == 'black':
					if cellNeighborn.figure['Checker']:
						cellNeighborn2 = cells[self.indexSeachIn2DList(self.x + 2, self.y + 2)]
						if cellNeighborn2.figure['None']:
							enemy.append(cellNeighborn)
		#Black
		if self.team == 'black':
			#leftBottom
			if self.x - 2 >= 0 and self.y + 2 <= rows - 1:
				cellNeighborn = cells[self.indexSeachIn2DList(self.x - 1, self.y + 1)]
				if cellNeighborn.team == 'white':
					if cellNeighborn.figure['Checker']:
						cellNeighborn2 = cells[self.indexSeachIn2DList(self.x - 2, self.y + 2)]
						if cellNeighborn2.figure['None']:
							enemy.append(cellNeighborn)
			#rightBottom
			if self.x + 2 <= rows - 1 and self.y + 2 <= rows - 1:
				cellNeighborn = cells[self.indexSeachIn2DList(self.x + 1, self.y + 1)]
				if cellNeighborn.team == 'white':
					if cellNeighborn.figure['Checker']:
						cellNeighborn2 = cells[self.indexSeachIn2DList(self.x + 2, self.y + 2)]
						if cellNeighborn2.figure['None']:
							enemy.append(cellNeighborn)
			#leftTop
			if self.x - 2 >= 0 and self.y - 2 >= 0:
				cellNeighborn = cells[self.indexSeachIn2DList(self.x - 1, self.y - 1)]
				if cellNeighborn.team == 'white':
					if cellNeighborn.figure['Checker']:
						cellNeighborn2 = cells[self.indexSeachIn2DList(self.x - 2, self.y - 2)]
						if cellNeighborn2.figure['None']:
							enemy.append(cellNeighborn)
			#rightTop
			if self.x + 2 <= rows - 1 and self.y - 2 >= 0:
				cellNeighborn = cells[self.indexSeachIn2DList(self.x + 1, self.y - 1)]
				if cellNeighborn.team == 'white':
					if cellNeighborn.figure['Checker']:
						cellNeighborn2 = cells[self.indexSeachIn2DList(self.x + 2, self.y - 2)]
						if cellNeighborn2.figure['None']:
							enemy.append(cellNeighborn)

		return (neigborns, enemy)

	def selection(self, cells, currentPlayer):
		if pg.mouse.get_pressed()[0]:
			mousePos = pg.mouse.get_pos()
			if currentPlayer == 'white' and self.team == 'white' or currentPlayer == 'black' and self.team == 'black':
				rect = pg.Rect(self.x * self.size, self.y * self.size, self.size, self.size)
				if rect.collidepoint(mousePos):
					return cells[self.indexSeachIn2DList(self.x, self.y)]

	def Info(self):
		x = self.x * self.size
		y = self.y * self.size
		teamR = font.render(self.team, True, pg.Color('orange'))
		teamRect = teamR.get_rect(center = (x + 25, y + 25))
		screen.blit(teamR, teamRect)

		figure = 'None'
		if self.figure['Checker']:
			figure = 'checker'
		elif self.figure['None']:
			figure = ''
		elif self.figure['King']:
			figure = 'King'
		figureR = font.render(figure, True, pg.Color('darkorange'))
		figureRect = figureR.get_rect(center = (x + 35, y + 50))
		screen.blit(figureR, figureRect)

class game:
	def __init__(self):
		self.cells = [cell(x,y) for x in range(rows) for y in range(cols)]
		self.current_cell = None
		self.neigborns = None
		self.enemy = None
		self.currentPlayer = 'white'
		self.indexSeachIn2DList = lambda x,y: y + x * rows

		self.scoreWhite = 0
		self.scoreBlack = 0

	def end(self):
		if self.scoreBlack == 20:
			print('White win!')
			self.cells = [cell(x,y) for x in range(rows) for y in range(cols)]
			self.scoreWhite = 0
			self.scoreBlack = 0
			self.currentPlayer = 'white'
		elif self.scoreWhite == 20:
			print('Black win')
			self.cells = [cell(x,y) for x in range(rows) for y in range(cols)]
			self.scoreWhite = 0
			self.scoreBlack = 0
			self.currentPlayer = 'white'

	def event(self):
		for event in pg.event.get():
			if event.type == pg.QUIT:
				quit()

	def currentCell(self,cell):
		if self.current_cell:
			if self.current_cell.figure['Checker'] or self.current_cell.figure['King']:
				if self.current_cell:
					self.current_cell.currentCellDr()
				self.neigbornsEnemy = self.current_cell.setNeigborns(self.cells)
				self.enemy = self.neigbornsEnemy[1]
				self.neigborns = self.neigbornsEnemy[0]
				if self.neigborns:
					for currentNeigborns in self.neigborns:
						if self.current_cell:
							currentNeigborns.neigbornDr()
							if self.current_cell.move(self.neigborns):
								if self.currentPlayer == 'black':
									self.currentPlayer = 'white'
								elif self.currentPlayer == 'white':
									self.currentPlayer = 'black'

				if self.enemy:
					for enemy in self.enemy:
						enemy.neigbornDrEnemy()
						if pg.mouse.get_pressed()[0]:
							mousePos = pg.mouse.get_pos()
							rect = pg.Rect(enemy.x * enemy.size, enemy.y * enemy.size, enemy.size, enemy.size)
							if rect.collidepoint(mousePos):
								enemy.figure['None'] = True
								enemy.figure['Checker'] = False
								enemy.figure['King'] = False
								enemy.team = None
								#Remove CEll
								self.current_cell.figure['None'] = True
								self.current_cell.figure['Checker'] = False
								self.current_cell.figure['King'] = False
								team = self.current_cell.team
								self.current_cell.team = None
								#leftTop
								if enemy.x - self.current_cell.x == -1 and enemy.y - self.current_cell.y == -1:
									self.current_cell = self.cells[self.indexSeachIn2DList(self.current_cell.x - 2, self.current_cell.y - 2)]
								#rightTop
								elif enemy.x - self.current_cell.x == 1 and enemy.y - self.current_cell.y == -1:
									self.current_cell = self.cells[self.indexSeachIn2DList(self.current_cell.x + 2, self.current_cell.y - 2)]
								#leftBottom
								elif enemy.x - self.current_cell.x == -1 and enemy.y - self.current_cell.y == 1:
									self.current_cell = self.cells[self.indexSeachIn2DList(self.current_cell.x - 2, self.current_cell.y + 2)]
								#rightBottom
								elif enemy.x - self.current_cell.x == 1 and enemy.y - self.current_cell.y == 1:
									self.current_cell = self.cells[self.indexSeachIn2DList(self.current_cell.x + 2, self.current_cell.y + 2)]

								self.current_cell.figure['None'] = False
								self.current_cell.figure['Checker'] = True
								self.current_cell.team = team
								self.current_cell = None

								if self.currentPlayer == 'black':
									self.currentPlayer = 'white'
									self.scoreBlack += 1
								elif self.currentPlayer == 'white':
									self.currentPlayer = 'black'
									self.scoreWhite += 1

				if pg.mouse.get_pressed()[2]:
					self.current_cell = None
			else:
				self.current_cell = None

		if not self.current_cell:
			self.current_cell = cell.selection(self.cells, self.currentPlayer)

	def cellOperations(self):
		for cell in self.cells:
			cell.cellDr()
			#cell.Info()
			self.currentCell(cell)
			cell.drawFigure()

	def info(self):
		font = pg.font.SysFont('Arial', 33)
		currentPlayerR = font.render(f'Current Player {self.currentPlayer}', True, pg.Color(self.currentPlayer))
		currentPlayerRect = currentPlayerR.get_rect(center = (950, 50))
		screen.blit(currentPlayerR, currentPlayerRect)

		scoreR = font.render('Score:', True, pg.Color('black'))
		scoreRect = scoreR.get_rect(center = (1000, 110))
		screen.blit(scoreR, scoreRect)

		scoreRBlack = font.render(f'Black: {self.scoreBlack}', True, pg.Color('black'))
		scoreRectBlack = scoreRBlack.get_rect(center = (900, 160))
		screen.blit(scoreRBlack, scoreRectBlack)

		scoreRWhite = font.render(f'White: {self.scoreWhite}', True, pg.Color('black'))
		scoreRectWhite = scoreRWhite.get_rect(center = (900, 200))
		screen.blit(scoreRWhite, scoreRectWhite)

	def start(self):
		while True:
			screen.fill('gray')
			self.event()
			self.cellOperations()
			self.info()
			self.end()
			pg.display.flip()
			time.tick(FPS)

if __name__ == '__main__':
	game().start()