

class Settings():
	def __init__(self):
		self.screen_w = 1200
		self.screen_h = 700
		self.tile_size = 50
		self.delay = 0.15
		self.background_speed = 3
		self.player_gone_time = 2
		self.bat_gone_time = 1
		
		self.is_active = False
		self.need_clean = False
		
		#difficulity rate
		self.difficulity_rate = 4
		self.chanse_for_bat = 3
		self.chanse_for_empty = 3
		
		# dynamites amount
		self.dynamites = 4
		#scores
		self.score_diamond_blue = 1
		self.score_diamond_pink = 5
		
