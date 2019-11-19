import pygame, random, time

class Player(pygame.sprite.Sprite):
	def __init__(self, settings, dirt_group, graphics):
		super(Player, self). __init__()
		self.settings = settings
		self.graphics = graphics
		self.dirt_group = dirt_group
		self.images = list()
		self.direction = str()
		#dict, because more actions planned
		self.last_move_or_action = {'face': 0}
		self.deploy_dynamite = False
		self.alive = True
		self.suicide = False
		self.death_seq = 0

		self.image = self.graphics.player_images[0]
		self.rect = self.image.get_rect()
		self.randomize_start_position()
		#player delay
		self.time_delay = 0.0
		self.timer = 0.0

	def update_player(self):
		if self.alive:
			if self.last_move_or_action['move'] == 'left':
				if self.last_move_or_action['face'] == 0:
					self.image = pygame.transform.flip(self.graphics.player_images[0], True, False)
					self.last_move_or_action['face'] = 1
				else:
					self.image = pygame.transform.flip(self.graphics.player_images[1], True, False)
					self.last_move_or_action['face'] = 0
			elif self.last_move_or_action['move'] == 'right':
				if self.last_move_or_action['face'] == 0:
					self.image = self.graphics.player_images[0]
					self.last_move_or_action['face'] = 1
				else:
					self.image = self.graphics.player_images[1]
					self.last_move_or_action['face'] = 0

	def death(self):
		self.alive = False
		pygame.event.clear()
		self.rect.inflate_ip(100,100)
		self.image = pygame.transform.scale(self.graphics.player_images[2], (self.settings.tile_size * 3, self.settings.tile_size * 3))
		self.death_seq = round(time.time()) + self.settings.player_gone_time
			
	def randomize_start_position(self):
		player_start_dirt = True
		while player_start_dirt:
			self.rect.x = int(random.randint(1, self.settings.screen_w / self.settings.tile_size) - 1) * self.settings.tile_size
			self.rect.y = int(random.randint(1, self.settings.screen_h / self.settings.tile_size) - 1) * self.settings.tile_size
			for dirt in self.dirt_group:
				if self.rect == dirt.rect:
					player_start_dirt = False

		# ~ print('player start location x{}, y{}'.format (self.rect.x, self.rect.y))



