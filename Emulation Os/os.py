import pygame as pg
from __init__ import *
import files
import mouse
import keyboard
from font import Text

SCREEN = pg.display.set_mode(RESOLUTION, flags=16)
pg.display.set_caption(CAPTION_OS)

class OS:
	def __init__(self):
		self.mouse = mouse.Mouse(pg, SCREEN)

		self.Text = Text(pg, SCREEN)
		self.kb = keyboard.KeyBoard(pg, SCREEN, self.Text.create)

		self.Text.create('Test', (255,255,255), (100,100), 30)

	def events(self):
		for event in pg.event.get():
			if event.type == pg.QUIT:
				quit()

			if event.type == pg.KEYDOWN:
				self.kb.k_input(event)

	def main(self):
		while True:
			SCREEN.fill(BACKGROUND_OS)

			self.events()
			self.kb.draw()
			
			self.mouse.main()
			pg.display.flip()

if __name__ == '__main__':
	OS().main()

