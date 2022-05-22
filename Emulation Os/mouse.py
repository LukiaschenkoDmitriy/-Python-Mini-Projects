CURSOR = 'default'
SELECT_COLOR = (3, 132, 252, 122)

def draw_polygon_alpha(surface, color, points, pg):
    lx, ly = zip(*points)
    min_x, min_y, max_x, max_y = min(lx), min(ly), max(lx), max(ly)
    target_rect = pg.Rect(min_x, min_y, max_x - min_x, max_y - min_y)
    shape_surf = pg.Surface(target_rect.size, pg.SRCALPHA)
    pg.draw.polygon(shape_surf, color, [(x - min_x, y - min_y) for x, y in points])
    surface.blit(shape_surf, target_rect)
    return target_rect

class MSelect:
	def __init__(self):
		self.first_pos = None
		self.second_pos = None

		self.area = None

		self.select_files = []

	def selection(self, button_status, pg, screen):
		if button_status[0]:
			if not self.first_pos:
				self.first_pos = pg.mouse.get_pos()

			else:
				self.second_pos = pg.mouse.get_pos()
		else:
			self.first_pos,self.second_pos = None,None

		if self.first_pos and self.second_pos:
			pos = [(self.first_pos[0],self.first_pos[1]),
				   (self.second_pos[0],self.first_pos[1]),
				   (self.second_pos[0],self.second_pos[1]),
				   (self.first_pos[0],self.second_pos[1])]

			rect_ = draw_polygon_alpha(screen, SELECT_COLOR, pos, pg)
			self.area = (rect_[0],rect_[1],rect_[0]+rect_[2],rect_[1]+rect_[3])

	def select_file(self):
		pass

class Mouse(MSelect):
	def __init__(self, pg, screen):
		super().__init__()

		self.screen = screen
		self.pg = pg

		self.click = [False,False,False]

	def left_click(self):
		pass

	def event_click(self):
		pressed = self.pg.mouse.get_pressed()
		self.click = [False,False,False]

		if pressed[2]:
			self.click[2] = True
		elif pressed[1]:
			self.click[1] = True
		elif pressed[0]:
			self.click[0] = True

	def main(self):
		self.event_click()
		self.selection(self.click, self.pg, self.screen)