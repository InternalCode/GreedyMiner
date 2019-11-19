import pygame, random, time

class Stone(pygame.sprite.Sprite):
	def __init__(self, settings, y ,x, graphics):
		super(Stone, self). __init__()
		self.next_move = int()
		self.name = 'stone'
		self.movement = False
		self.settings = settings
		self.image = pygame.transform.rotate(graphics.stone_images[random.randint(0,2)], random.choice([0, 90, 180]))
		self.rect = self.image.get_rect()
		self.rect.x = settings.tile_size * x
		self.rect.y = settings.tile_size * y

	def update(self, player, stone_group, diamond_group, dirt_group, dynamite_group, bat_group):
		if self.next_move_delay():
			self.vertical_fall(player, stone_group, diamond_group, dirt_group, dynamite_group, bat_group)
			self.horizontal_fall(player, stone_group, diamond_group, dirt_group, dynamite_group)
		if self.name == 'diamond':
			self.update_diamond_animation()

	def next_move_delay(self):
		if self.next_move == 0:
			self.next_move = round(time.time(), 2) + self.settings.delay
		elif self.next_move < round(time.time(), 2):
			self.next_move = 0
			return True

	def vertical_fall(self, player, stone_group, diamond_group, dirt_group, dynamite_group, bat_group):
		check_rect = pygame.Rect(self.rect)
		check_rect.y += self.settings.tile_size
		is_dirt_f = False
		is_stone_f = False
		is_diamond_f = False
		is_player_f = False
		is_dynamite_f = False
		#check for dirt
		for dirt in dirt_group:
			if dirt.rect == check_rect:
				is_dirt_f = True
		#check for stone
		for stone in stone_group:
			if stone.rect == check_rect:
				is_stone_f = True
		#check for diamond
		for diamond in diamond_group:
			if diamond.rect == check_rect:
				is_diamond_f = True
		#check for dynamite
		for dynamite in dynamite_group:
			if dynamite.rect == check_rect:
				is_dynamite_f = True
		#check for player and check for death
		if player.rect == check_rect:
			if self.movement == True:
				player.death()
			else:
				is_player_f = True
		#check bat and bat death with stone
		#check bat and bat death with diamond
		for bat in bat_group:
			if pygame.sprite.spritecollideany(bat, diamond_group):
				bat.death()
			if pygame.sprite.spritecollideany(bat, stone_group):
				bat.death()
		
		
		
		
		# fall and check bottom line of screen
		if is_dirt_f == False and is_stone_f == False and is_diamond_f == False and is_player_f == False and is_dynamite_f == False:
			if self.rect.y + self.settings.tile_size < self.settings.screen_h:
				self.rect.y += self.settings.tile_size
				self.movement = True
		else:
			self.movement = False

	def horizontal_fall(self, player, stone_group, diamond_group, dirt_group, dynamite_group):
		#	flags:
		#	1 - x - 2
		#	3 - 4 - 5
		
		f_1 = False
		f_2 = False
		f_3 = False
		f_4 = False
		f_5 = False
		
		check_1 = pygame.Rect(self.rect)
		check_2 = pygame.Rect(self.rect)
		check_3 = pygame.Rect(self.rect)
		check_4 = pygame.Rect(self.rect)
		check_5 = pygame.Rect(self.rect)

		check_1.x -= self.settings.tile_size
		check_2.x += self.settings.tile_size
		check_3.x -= self.settings.tile_size
		check_3.y += self.settings.tile_size
		check_4.y += self.settings.tile_size
		check_5.x += self.settings.tile_size
		check_5.y += self.settings.tile_size

		#check screen edges
		if check_1.left < 0:
			f_1 = True
		if check_2.right > self.settings.screen_w:
			f_2 = True

		for dirt in dirt_group:
			if dirt.rect == check_1:
				f_1 = True
			if dirt.rect == check_2:
				f_2 = True
			if dirt.rect == check_3:
				f_3 = True
			if dirt.rect == check_4:
				f_4 = False
			if dirt.rect == check_5:
				f_5 = True

		for stone in stone_group:
			if stone.rect == check_1:
				f_1 = True
			if stone.rect == check_2:
				f_2 = True
			if stone.rect == check_3:
				f_3 = True
			if stone.rect == check_4:
				f_4 = True
			if stone.rect == check_5:
				f_5 = True
				
		for diamond in diamond_group:
			if diamond.rect == check_1:
				f_1 = True
			if diamond.rect == check_2:
				f_2 = True
			if diamond.rect == check_3:
				f_3 = True
			if diamond.rect == check_4:
				f_4 = True
			if diamond.rect == check_5:
				f_5 = True

		if player.rect == check_1:
			f_1 = True
		if player.rect == check_2:
			f_2 = True
		if player.rect == check_3:
			f_3 = True
		if player.rect == check_4:
			f_4 = False
		if player.rect == check_5:
			f_5 = True
			
		for dynamite in dynamite_group:
			if dynamite.rect == check_1:
				f_1 = True
			if dynamite.rect == check_2:
				f_2 = True
			if dynamite.rect == check_3:
				f_3 = True
			if dynamite.rect == check_4:
				f_4 = False
			if dynamite.rect == check_5:
				f_5 = True

		if f_1 == False and f_2 == False and f_3 == False and f_5 == False and f_4 == True:
			if random.randint(0, 100) > 50:
				self.rect.x -= self.settings.tile_size
			else:
				self.rect.x += self.settings.tile_size
		if f_1 == False and f_3 == False and f_4 == True:
				self.rect.x -= self.settings.tile_size
		if f_2 == False and f_5 == False and f_4 == True:
				self.rect.x += self.settings.tile_size

















