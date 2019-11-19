import pygame, random, time

class Main_screen():
	def __init__(self, display, hiscores):
		self.display = display
		self.hiscores = hiscores
		self.display_size = display.get_size()
		#background
		self.background_image = pygame.image.load('graphics\\menu\\back.png').convert_alpha()
		self.background_rect = self.background_image.get_rect()
		
		#background 1 coords and sets
		self.background_rect.centerx = int(self.display_size[0] / 2)
		self.background_rect.centery = int(self.display_size[1] / 2)
		self.background_go_left_right = True
		self.background_go_up_down = True

		#background 2
		self.background_image_2 = pygame.image.load('graphics\\menu\\front.png').convert_alpha()
		self.background_rect_2 = self.background_image_2.get_rect()
		#background 2 coords and sets
		self.background_rect_2.centerx = int(self.display_size[0] / 2)
		self.background_rect_2.centery = int(self.display_size[1] / 2)

		#fonts
		self.font_big = pygame.font.Font('font\\font.ttf', 32)
		self.font_small = pygame.font.Font('font\\font.ttf', 16)

	def draw(self):
		self.display.fill((100,100,100))
		self.draw_background()
		self.draw_background_2()
		self.display_name()
		self.display_version()
		self.display_instrunctions()
		self.display_hiscores()

	def draw_background(self):

		if self.background_go_left_right == True:
			self.background_rect.centerx += random.randint(0,1)
			if self.background_rect.centerx > (self.display_size[0] / 2) + 3:
				self.background_go_left_right = False
		else:
			self.background_rect.centerx -= random.randint(0,1)
			if self.background_rect.centerx < (self.display_size[0] / 2) - 3:
				self.background_go_left_right = True
				
		if self.background_go_up_down == True:
			self.background_rect.centery += random.randint(0,1)
			if self.background_rect.centery > (self.display_size[1] / 2) + 3:
				self.background_go_up_down = False
		else:
			self.background_rect.centery -= random.randint(0,1)
			if self.background_rect.centery < (self.display_size[1] / 2) - 3:
				self.background_go_up_down = True
				
		self.display.blit(self.background_image, self.background_rect)
	
	def draw_background_2(self):
		self.display.blit(self.background_image_2, self.background_rect_2)
		
	def display_name(self):
		text = self.font_big.render('Greedy Miner', True, (250,250,250))
		text_rect = text.get_rect()
		text_rect.x = int(self.display_size[0] * 0.05)
		text_rect.y = int(self.display_size[1] * 0.1)
		self.display.blit(text, text_rect)

	def display_version(self):
		text = self.font_small.render('v. beta 2', True, (250,250,250))
		text_rect = text.get_rect()
		text_rect.x = int(self.display_size[0] * 0.9)
		text_rect.y = int(self.display_size[1] * 0.9)
		self.display.blit(text, text_rect)
		
	def display_instrunctions(self):
		text = self.font_big.render('Press Enter to start...', True, (250,250,250))
		text_rect = text.get_rect()
		text_rect.x = int(self.display_size[0] * 0.05)
		text_rect.y = int(self.display_size[1] * 0.75)
		self.display.blit(text, text_rect)
		
	def display_hiscores(self):
		text = self.font_big.render('HiScores:  %s' %self.hiscores.hiscores , True, (250,250,250))
		text_rect = text.get_rect()
		text_rect.x = int(self.display_size[0] * 0.75)
		text_rect.y = int(self.display_size[1] * 0.75)
		self.display.blit(text, text_rect)
		
		
		
		
		
		
		
		
		
		
