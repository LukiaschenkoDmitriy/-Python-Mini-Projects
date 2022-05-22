import pygame as pg
import re

RES = WIDTH,HEIGHT = 1200, 900
screen = pg.display.set_mode(RES)
pg.display.set_caption('PyOs')
pg.font.init()

class Mouse:
	def __init__(self):
		self.MouseBar.__init__(self)
		self.mouseSelection.__init__(self)

	class mouseSelection:
		def __init__(self):
			self.mouseEvent = False
			self.mousePos1 = -10,-10
			self.mousePos2 = -10,-10
			self.colorSelection = (100,100,100)
			self.rect = None

			self.selectFiles = []
			self.selectionObjects = False

		def selection(self):
			self.pressed = pg.mouse.get_pressed()[0]
			if self.pressed and not self.mouseEvent:
				self.mousePos1 = pg.mouse.get_pos()
				self.mouseEvent = True

			#presseds
			if self.pressed and self.mouseEvent:
				self.mousePos2 = pg.mouse.get_pos()

			if not self.pressed:
				self.mouseEvent = False
				self.mousePos2 = -10,-10
				self.mousePos1 = -10,-10
				self.selectFiles = []
				self.selectionObjects = False

			#Selection
			if self.pressed and not self.selectionObjects:
				(x1,y1) = self.mousePos1
				(x2,y2) = self.mousePos2
				self.rect = pg.draw.polygon(screen, self.colorSelection, ([(x1,y1),(x2,y1),(x2,y2),(x1,y2)]))

		def selectionFiles(self, files):
			#Selection FIles
			if not self.mouseEvent and self.rect:
				for file in files:
					pos = file.get('position')
					size = file.get('size')
					fileRect = pg.Rect((pos[0] - 1, pos[1] - 1), (size + 3, size + 3))
					if fileRect.colliderect(self.rect):
						pg.draw.rect(screen, pg.Color('red'), fileRect, 2)
						if file not in self.selectFiles:
							self.selectFiles.append(file)
						
			#Move files
			if self.selectFiles:
				for obj in self.selectFiles:
					rect = pg.Rect(obj['position'], (obj['size'], obj['size']))
					if self.pressed and rect.collidepoint(pg.mouse.get_pos()):
						obj['position'] = (pg.mouse.get_pos()[0] - 25, pg.mouse.get_pos()[1] - 25)
						self.selectionObjects = True

	class MouseBar:
		def __init__(self):
			self.open = False
			self.bgColor = (47, 94, 89)
			self.fontColor = (255,255,255)
			self.font = pg.font.SysFont('Arial', 20)
			self.mousePos = 0,0

			self.rightbar = ['defaultFile']
			self.rightbarFile = ['removeFile', 'renameFile']

			lenGadgets = 1 if not self.rightbar else len(self.rightbar)
			lenGadgets2 = 1 if not self.rightbarFile else len(self.rightbarFile)
			self.sizeForOneGadget = 35 * lenGadgets
			self.sizeForOneGadget2 = 35 * lenGadgets2
			self.gadgetRect = None

		def summonBar(self):
			self.rightMouse = pg.mouse.get_pressed()[2]
			if self.rightMouse:
				if not self.open:
					self.open = True
					self.mousePos = pg.mouse.get_pos()

			if self.rect and self.gadgetRect:
				if self.pressed and not self.gadgetRect.collidepoint(pg.mouse.get_pos()):
					self.open = False

			if self.open:
				if not self.selectFiles:
					self.gadgetRect = pg.draw.rect(screen, (self.bgColor), (self.mousePos[0] + 10, self.mousePos[1], 200, self.sizeForOneGadget))
					Mouse.MouseBar.autoBuild(self,name = 'New File', pos = self.mousePos, nameFunction = 'defaultFile')
				else:
					self.gadgetRect = pg.draw.rect(screen, (self.bgColor), (self.mousePos[0] + 10, self.mousePos[1], 200, self.sizeForOneGadget2))
					posX = self.mousePos[0]
					posY = self.mousePos[1]
					Mouse.MouseBar.autoBuild(self, name = 'Remove File', pos = (posX, posY), nameFunction = 'removeFile')
					posY += 35
					Mouse.MouseBar.autoBuild(self, name = 'Rename File', pos = (posX, posY), nameFunction = 'renameFile')

		def autoBuild(self, name, pos, nameFunction):
			fontRender = self.font.render(name, True, self.fontColor)
			fontRect = fontRender.get_rect(topleft = (pos[0] + 25, pos[1] + 3))
			screen.blit(fontRender, fontRect)
			if self.pressed and fontRect.collidepoint(pg.mouse.get_pos()):
				if nameFunction == 'defaultFile':
					Files.createFile(self, pos = (150,150))

				if self.selectFiles:
					if nameFunction == 'removeFile':
						Files.removeFile(self, self.selectFiles)

					if nameFunction == 'renameFile':
						KeyBoard.__init__(self,SInput = True, operation = 'renameFile', files = self.selectFiles)

				self.open = False

class KeyBoard:
	def __init__(self, SInput = False, operation = None, files = None):
		self.files = files
		self.operation = operation
		self.SInput = SInput

		self.KeyEvent = None
		self.textInput = ''
		self.localFont = pg.font.SysFont('Arial', 34)

	def getEvent(self, event):
		if event.type == pg.KEYDOWN:
			self.KeyEvent = event.__dict__['unicode']
			if self.KeyEvent == '\x08':
				self.KeyEvent = 'clear'
			if self.KeyEvent == '\r':
				self.KeyEvent = 'enter'

	def input(self):
		if self.SInput:
			if self.KeyEvent and self.KeyEvent != 'clear' and len(self.textInput) < 20 and self.KeyEvent and self.KeyEvent != 'enter':
				self.textInput += self.KeyEvent
			if self.KeyEvent == 'clear' and self.textInput:
				self.textInput = self.textInput[:-1]
			if self.KeyEvent == 'enter':
				if self.operation == 'renameFile':
					Files.renameFile(self, str(self.textInput), self.files)
				self.SInput = False

			self.KeyEvent = None

			pg.draw.rect(screen, (168, 62, 50), (0,850, 1200, 50))
			renderFont = self.localFont.render(self.textInput, True, (255,255,255))
			screen.blit(renderFont, (10, 850))

	def getTextInput(self):
		return self.textInput

class Files:
	def __init__(self):
		self.sizeFile = 50
		self.arrayFiles = []
		self.font = pg.font.SysFont('Arial', 22)

	def createFile(self, pos, title = 'New File', icon = None, color = (143,195,100), type = 'default'):
		if icon:
			self.arrayFiles.append({'title' : title, 'position' : pos, 'icon' : icon, 'size' : self.sizeFile, 'type' : type})
		else:
			self.arrayFiles.append({'title' : title, 'position' : pos, 'color' : color, 'size' : self.sizeFile, 'type' : type})

	def renameFile(self, newName, selectFiles):
		for file in selectFiles:
			for file2 in self.arrayFiles:
				if file2['title'] == file['title']:
					file2['title'] = newName

	def removeFile(self, selectFiles):
		for file in selectFiles:
			if file['type'] == 'default':
				self.arrayFiles.remove(file)
			else:
				print('File unposible remove')


	def drawFiles(self):
		if self.arrayFiles:
			for file in self.arrayFiles:
				title = file.get('title')
				pos = file.get('position')
				if file.get('icon'):
					icon = file.get('icon')
					screen.blit(icon, pos)
				else:
					color = file.get('color')
					pg.draw.rect(screen, color, (pos[0], pos[1], self.sizeFile, self.sizeFile))
				titleRender = self.font.render(title, True, pg.Color('white'))
				titleRect = titleRender.get_rect(center = (pos[0] + self.sizeFile/2, pos[1] + 70))
				screen.blit(titleRender, titleRect)

class Folder:
	def __init__(self):
		self.open = False
		self.x, self.y = 300, 200
		self.defaultWidth = 500
		self.defaultHeight = 600

	def openFolder(self):
		if self.open:
			pg.draw.rect(screen, (217, 217, 217), (self.x, self.y, self.defaultWidth, self.defaultHeight))


class mainOs(Files, Mouse):
	def __init__(self):
		Mouse.__init__(self)
		Files.__init__(self)
		KeyBoard.__init__(self)
		Files.createFile(self, (100,100), 'Desktop', type = 'dekstop')
		Files.createFile(self, (1100,800), 'Basket', type = 'basket')

	def event(self):
		for event in pg.event.get():
			#QUIT
			quit() if event.type == pg.QUIT else None
			KeyBoard.getEvent(self.event)

	def main(self):
		while True:
			screen.fill((36, 36, 36))
			self.event()

			#Mouse
			self.mouseSelection.selection(self)
			self.mouseSelection.selectionFiles(self, self.arrayFiles)

			#Files
			Files.drawFiles(self)

			self.MouseBar.summonBar(self)
			KeyBoard.input(self)
			#Update desktop
			pg.display.flip()

mainOs().main()