from __init__ import DEFAULT_FONT

class Text:
	def __init__(self, pg, screen):
		self.pg = pg
		self.screen = screen

		pg.font.init()

	def create(self,text, color, pos, size, 
			   df = DEFAULT_FONT, align = 'center'):

		self.font = self.pg.font.SysFont(df, size)

		self.created_font = self.font.render(str(text), True, color)

		font_size = self.created_font.get_size()
		if align.lower() == 'right':
			pos = (pos[0]-font_size[0]//2,pos[1])
		elif align.lower() == 'left':
			pos = (pos[0]+font_size[0]//2,pos[1])
		elif align.lower() == 'center':
			None
		else:
			raise ValueError(f'Аргумента align:{align}, не существует.\ncenter,left,right')

		self.created_rect = self.created_font.get_rect(center = pos)

		self.screen.blit(self.created_font,self.created_rect)