import pygame, time, random

class Dynamite(pygame.sprite.Sprite):
	def __init__(self, settings, player, graphics):
		super(Dynamite, self). __init__()
		self.settings = settings
		self.graphics = graphics
		#time to explode
		self.time_to_explode = round(time.time(), 2) + 3
		#boom time
		self.boom_time = round(time.time(), 2) + 3.33
		#triggr
		self.trigger = True
		#set default image
		self.image = self.graphics.dynamite_images[0]
		self.rect = self.image.get_rect()
		
		#set in player position
		self.rect.centerx = player.rect.centerx
		self.rect.centery = player.rect.centery
		
		#what will be destroyed
		#1,2,3
		#4,x,5
		#6,7,8
		self.rect_1 = pygame.Rect(self.rect)
		self.rect_2 = pygame.Rect(self.rect)
		self.rect_3 = pygame.Rect(self.rect)
		self.rect_4 = pygame.Rect(self.rect)
		self.rect_5 = pygame.Rect(self.rect)
		self.rect_6 = pygame.Rect(self.rect)
		self.rect_7 = pygame.Rect(self.rect)
		self.rect_8 = pygame.Rect(self.rect)
		self.rect_x = pygame.Rect(self.rect)
		
		self.rect_1.y -= settings.tile_size
		self.rect_1.x -= settings.tile_size
		self.rect_2.y -= settings.tile_size
		self.rect_3.y -= settings.tile_size
		self.rect_3.x += settings.tile_size
		self.rect_4.x -= settings.tile_size
		self.rect_5.x += settings.tile_size
		self.rect_6.x -= settings.tile_size
		self.rect_6.y += settings.tile_size
		self.rect_7.y += settings.tile_size
		self.rect_8.x += settings.tile_size
		self.rect_8.y += settings.tile_size
		
	def update(self, player, dirt_group, stone_group, diamond_group, dynamite_group):
		
		#spark - dynamite animation
		if self.trigger:
			self.image = self.graphics.dynamite_images[random.randint(0,1)]
		if self.time_to_explode < round(time.time(), 2):
			if self.trigger:
				self.rect.inflate_ip(100, 100)
				self.image = pygame.transform.scale(self.graphics.dynamite_images[2], (self.settings.tile_size * 3, self.settings.tile_size * 3))
				self.trigger = False
			elif self.boom_time < round(time.time(), 2):

				for dirt in dirt_group:
					if self.rect_1 == dirt.rect or self.rect_2 == dirt.rect or self.rect_3 == dirt.rect\
					or self.rect_4 == dirt.rect or self.rect_5 == dirt.rect or self.rect_6 == dirt.rect\
					or self.rect_7 == dirt.rect or self.rect_8 == dirt.rect:
						dirt_group.remove(dirt)
				for stone in stone_group:
					if self.rect_1 == stone.rect or self.rect_2 == stone.rect or self.rect_3 == stone.rect\
					or self.rect_4 == stone.rect or self.rect_5 == stone.rect or self.rect_6 == stone.rect\
					or self.rect_7 == stone.rect or self.rect_8 == stone.rect:
						stone_group.remove(stone)
				for diamond in diamond_group:
					if self.rect_1 == diamond.rect or self.rect_2 == diamond.rect or self.rect_3 == diamond.rect\
					or self.rect_4 == diamond.rect or self.rect_5 == diamond.rect or self.rect_6 == diamond.rect\
					or self.rect_7 == diamond.rect or self.rect_8 == diamond.rect:
						diamond_group.remove(diamond)
				
				if self.rect_1 == player.rect or self.rect_2 == player.rect or self.rect_3 == player.rect\
				or self.rect_4 == player.rect or self.rect_5 == player.rect or self.rect_6 == player.rect\
				or self.rect_7 == player.rect or self.rect_8 == player.rect or self.rect_x == player.rect:
					player.death()
				self.kill()
		
