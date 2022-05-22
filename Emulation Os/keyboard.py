from __init__ import WIDTH,HEIGHT

class KeyBoard:
	def __init__(self, pg, screen, create_text):
		self.input = True
		self.create_text = create_text
		self.text = ''

		self.pg = pg
		self.screen = screen

	def k_input(self, event):
		if self.input:
			print(event.__dict__)
			sumbol = event.__dict__['unicode']
			if sumbol == '\x08' and self.text != '':
				self.text = self.text[:-1]

			elif sumbol == '\r':
				self.text = ''

			elif sumbol != '\x08' and sumbol != '\t':
				self.text += sumbol
		else:
			if self.input:
				self.input = False

	def draw(self):
		if self.input:
			bg_f = self.pg.Surface((WIDTH,30))
			bg_f.set_alpha(128)
			bg_f.fill(self.pg.Color('red'))
			self.screen.blit(bg_f, (0,HEIGHT-25))


			self.create_text(self.text, (255,255,255), (100, HEIGHT-25), 30, align='left')