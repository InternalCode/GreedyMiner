import pygame

class Background():
	def __init__(self, settings, player, graphics):
		self.settings = settings
		self.last_x = int()
		self.last_y = int()
		self.image = graphics.background_images[0]
		self.rect = self.image.get_rect()
		# ~ print('start self background rect %s' %self.rect)
		# ~ print('background speed: %s' %self.settings.background_speed)
		# ~ print('background get size ', self.image.get_size())

		self.rect.centerx = self.settings.screen_w / 2
		self.rect.centery = self.settings.screen_h / 2
        
		# ~ print('background rect centerx %s, center y %s' %(self.rect.centerx, self.rect.centery))

	def update(self, player):
		if self.last_x > player.rect.centerx:
			self.rect.centerx += self.settings.background_speed
		elif self.last_x < player.rect.centerx:
			self.rect.centerx -= self.settings.background_speed
		if self.last_y > player.rect.centery:
			self.rect.centery += self.settings.background_speed
		elif self.last_y < player.rect.centery:
			self.rect.centery -= self.settings.background_speed
			
			
		self.last_x = player.rect.centerx
		self.last_y = player.rect.centery
