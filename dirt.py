import pygame, os, random

class Dirt(pygame.sprite.Sprite):
	def __init__(self, settings, y, x, graphics):
		super(Dirt, self). __init__()
		self.settings = settings
		self.name = 'dirt'
		self.graphics = graphics
		self.image = self.graphics.dirt_images[5]
		self.image_special = None
		self.rect = self.image.get_rect()
		self.rect.x = settings.tile_size * x
		self.rect.y = settings.tile_size * y
		
		#additional tile graphics
		self.special_chance()
		
	def special_chance(self):
		if random.randint(0,2000) == 0:
			self.image_special = self.graphics.dirt_images[random.randint(6, 12)]

	def update(self, dirt_group):
		#	1
		#2	x	3
		#	4
		checker_1 = pygame.Rect(self.rect)
		checker_2 = pygame.Rect(self.rect)
		checker_3 = pygame.Rect(self.rect)
		checker_4 = pygame.Rect(self.rect)
		
		f_1 = False
		f_2 = False
		f_3 = False
		f_4 = False
		
		checker_1.y -= self.settings.tile_size
		checker_2.x -= self.settings.tile_size
		checker_3.x += self.settings.tile_size
		checker_4.y += self.settings.tile_size
		
		for dirt in dirt_group:
			if checker_1 == dirt.rect:
				f_1 = True
			if checker_2 == dirt.rect:
				f_2 = True
			if checker_3 == dirt.rect:
				f_3 = True
			if checker_4 == dirt.rect:
				f_4 = True

		#sides
		if checker_1.top < 0:
			f_1 = True
		if checker_2.left < 0:
			f_2 = True
		if checker_3.right > self.settings.screen_w:
			f_3 = True
		if checker_4.bottom > self.settings.screen_h:
			f_4 = True

		#side block
		if f_1 == False and f_2 == True and f_3 == True and f_4 == True:
			self.image = pygame.transform.rotate(self.graphics.dirt_images[0], -90)
		if f_1 == True and f_2 == False and f_3 == True and f_4 == True:
			self.image = self.graphics.dirt_images[0]
		if f_1 == True and f_2 == True and f_3 == False and f_4 == True:
			self.image = pygame.transform.rotate(self.graphics.dirt_images[0], -180)
		if f_1 == True and f_2 == True and f_3 == True and f_4 == False:
			self.image = pygame.transform.rotate(self.graphics.dirt_images[0], 90)
		
		#corner block
		if f_1 == False and f_2 == False and f_3 == True and f_4 == True:
			self.image = self.graphics.dirt_images[1]
		if f_1 == False and f_2 == True and f_3 == False and f_4 == True:
			self.image = pygame.transform.rotate(self.graphics.dirt_images[1], -90)
		if f_1 == True and f_2 == True and f_3 == False and f_4 == False:
			self.image = pygame.transform.rotate(self.graphics.dirt_images[1], -180)
		if f_1 == True and f_2 == False and f_3 == True and f_4 == False:
			self.image = pygame.transform.rotate(self.graphics.dirt_images[1], 90)
		
		#pointy block
		if f_1 == True and f_2 == False and f_3 == False and f_4 == False:
			self.image = pygame.transform.rotate(self.graphics.dirt_images[2], 90)
		if f_1 == False and f_2 == True and f_3 == False and f_4 == False:
			self.image = pygame.transform.rotate(self.graphics.dirt_images[2], 180)
		if f_1 == False and f_2 == False and f_3 == True and f_4 == False:
			self.image = self.graphics.dirt_images[2]
		if f_1 == False and f_2 == False and f_3 == False and f_4 == True:
			self.image = pygame.transform.rotate(self.graphics.dirt_images[2], -90)
			
		# round one
		if f_1 == False and f_2 == False and f_3 == False and f_4 == False:
			self.image = self.graphics.dirt_images[3]
		
		# pipe alike
		if f_1 == True and f_2 == False and f_3 == False and f_4 == True:
			self.image = self.graphics.dirt_images[4]
		if f_1 == False and f_2 == True and f_3 == True and f_4 == False:
			self.image = pygame.transform.rotate(self.graphics.dirt_images[4], 90)
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
        
