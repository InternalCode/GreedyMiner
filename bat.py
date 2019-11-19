import pygame, time, random
from diamond import Diamond

class Bat(pygame.sprite.Sprite):
	def __init__(self, settings, y, x, graphics):
		super(Bat, self). __init__()
		self.settings = settings
		self.graphics = graphics
		#frame of animation
		self.frame = 0
		#animation time delay
		self.time_animation = 0.0
		#last move direction
		self.last_move_direction = ''
		#next move time
		self.time_move = 0.0
		#first image loaded & rect
		self.image = self.graphics.bat_images[self.frame]
		self.rect = self.image.get_rect()
		self.rect.x = self.settings.tile_size * x
		self.rect.y = self.settings.tile_size * y
		#is alive?
		self.alive = True
		self.collision = False
		self.plof_time = 0
		
	def update(self, player, dirt_group, stone_group, diamond_group, bat_group):
		self.animation()
		if self.next_move_time():
			self.next_move(player, dirt_group, stone_group, diamond_group)
		if self.collision == True:
			self.death_blow(player, dirt_group, stone_group, diamond_group, bat_group)
		if self.rect == player.rect:
			player.death()

		#animation times
	def animation(self):
		if 	self.alive == True:
			if self.time_animation < round(time.time(), 1):
				self.time_animation = round(time.time(), 1) + 0.2
				self.image = self.graphics.bat_images[self.frame]
				self.frame += 1
				if self.frame == 4:
					self.frame = 0

		#next move times
	def next_move_time(self):
		if self.alive == True:
			if self.time_move < round(time.time(), 1):
				self.time_move = round(time.time(), 1) + self.settings.delay
				return True

	def death(self):
		self.collision = True

	def death_blow(self, player, dirt_group, stone_group, diamond_group, bat_group):
		if self.alive == True:
			#what will be destroyed
			#1,2,3
			#4,x,5
			#6,7,8
			
			rect_1 = pygame.Rect(self.rect)
			rect_2 = pygame.Rect(self.rect)
			rect_3 = pygame.Rect(self.rect)
			rect_4 = pygame.Rect(self.rect)
			rect_5 = pygame.Rect(self.rect)
			rect_6 = pygame.Rect(self.rect)
			rect_7 = pygame.Rect(self.rect)
			rect_8 = pygame.Rect(self.rect)
			rect_x = pygame.Rect(self.rect)
			
			rect_1.y -= self.settings.tile_size
			rect_1.x -= self.settings.tile_size
			rect_2.y -= self.settings.tile_size
			rect_3.y -= self.settings.tile_size
			rect_3.x += self.settings.tile_size
			rect_4.x -= self.settings.tile_size
			rect_5.x += self.settings.tile_size
			rect_6.x -= self.settings.tile_size
			rect_6.y += self.settings.tile_size
			rect_7.y += self.settings.tile_size
			rect_8.x += self.settings.tile_size
			rect_8.y += self.settings.tile_size
			
			for dirt in dirt_group:
				if rect_1 == dirt.rect or rect_2 == dirt.rect or rect_3 == dirt.rect\
				or rect_4 == dirt.rect or rect_5 == dirt.rect or rect_6 == dirt.rect\
				or rect_7 == dirt.rect or rect_8 == dirt.rect:
					dirt_group.remove(dirt)
			for stone in stone_group:
				if rect_1 == stone.rect or rect_2 == stone.rect or rect_3 == stone.rect\
				or rect_4 == stone.rect or rect_5 == stone.rect or rect_6 == stone.rect\
				or rect_7 == stone.rect or rect_8 == stone.rect or rect_x == stone.rect:
					stone_group.remove(stone)
			for diamond in diamond_group:
				if rect_1 == diamond.rect or rect_2 == diamond.rect or rect_3 == diamond.rect\
				or rect_4 == diamond.rect or rect_5 == diamond.rect or rect_6 == diamond.rect\
				or rect_7 == diamond.rect or rect_8 == diamond.rect :
					diamond_group.remove(diamond)
			
			if pygame.sprite.spritecollideany(player, bat_group):
				player.death()
			
			if rect_1 == player.rect or rect_2 == player.rect or rect_3 == player.rect\
			or rect_4 == player.rect or rect_5 == player.rect or rect_6 == player.rect\
			or rect_7 == player.rect or rect_8 == player.rect or rect_x == player.rect:
				player.death()
			
			self.alive = False
			# ~ print('creating diamond')
			diamond = Diamond(self.settings, int(self.rect.y / self.settings.tile_size), int(self.rect.x / self.settings.tile_size), self.graphics, 'pink')
			diamond_group.add(diamond)

			self.rect.inflate_ip(100,100)
			self.image = pygame.transform.scale(self.graphics.bat_images[4],
								(self.settings.tile_size *3, self.settings.tile_size *3))
			self.plof_time = round(time.time()) + self.settings.bat_gone_time
		
		if self.plof_time < round(time.time()):

			self.kill()

	def next_move(self, player, dirt_group, stone_group, diamond_group):
		#movie
		#		up
		#left	x	right
		#		down
		#checkers
		up_checker_rect = pygame.Rect(self.rect)
		left_checker_rect = pygame.Rect(self.rect)
		right_checker_rect = pygame.Rect(self.rect)
		down_checker_rect = pygame.Rect(self.rect)
		#set rects
		up_checker_rect.y -= self.settings.tile_size
		left_checker_rect.x -= self.settings.tile_size
		right_checker_rect.x += self.settings.tile_size
		down_checker_rect.y += self.settings.tile_size
		#flags
		up_f = False
		left_f = False
		right_f = False
		down_f = False
		
		directions_dir = {'up': False, 'left': False, 'right': False, 'down': False}
		
		#check for edges
		if up_checker_rect.top < 0:
			up_f = True
		if left_checker_rect.left < 0:
			left_f = True
		if right_checker_rect.right > self.settings.screen_w:
			right_f = True
		if down_checker_rect.bottom > self.settings.screen_h:
			down_f = True

		#check for dirts
		for dirt in dirt_group:
			if dirt.rect == up_checker_rect:
				up_f = True
			if dirt.rect == left_checker_rect:
				left_f = True
			if dirt.rect == right_checker_rect:
				right_f = True
			if dirt.rect == down_checker_rect:
				down_f = True

		#check for stones
		for stone in stone_group:
			if stone.rect == up_checker_rect:
				up_f = True
			if stone.rect == left_checker_rect:
				left_f = True
			if stone.rect == right_checker_rect:
				right_f = True
			if stone.rect == down_checker_rect:
				down_f = True
				
		for diamond in diamond_group:
			if diamond.rect == up_checker_rect:
				up_f = True
			if diamond.rect == left_checker_rect:
				left_f = True
			if diamond.rect == right_checker_rect:
				right_f = True
			if diamond.rect == down_checker_rect:
				down_f = True

		#put rects to dict
		if up_f == False:
			directions_dir['up'] = up_checker_rect
		if left_f == False:
			directions_dir['left'] = left_checker_rect
		if right_f == False:
			directions_dir['right'] = right_checker_rect
		if down_f == False:
			directions_dir['down'] = down_checker_rect

		#general logic
		if self.last_move_direction not in directions_dir.keys():
			x = random.choice(['up', 'down', 'left', 'right'])
			if directions_dir[x] != False:
				self.rect = directions_dir[x]
				self.last_move_direction = x

		elif self.last_move_direction in directions_dir.keys():
			if directions_dir[self.last_move_direction] != False:
				self.rect = directions_dir[self.last_move_direction]
			else:
				x = random.choice(['up', 'down', 'left', 'right'])
				if directions_dir[x] != False:
					self.rect = directions_dir[x]
					self.last_move_direction = x
		

		
		
		
