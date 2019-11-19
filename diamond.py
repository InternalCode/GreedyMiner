import pygame, os, time, random, time
from stone import Stone


class Diamond(Stone):
	def __init__(self, settings, y, x, graphics, kind):
		super(Diamond, self). __init__(settings, x, y, graphics,)
		self.settings = settings
		self.graphics = graphics
		self.name = 'diamond'
		self.kind = kind
		self.rect = self.image.get_rect()
		self.rect.x = settings.tile_size * x
		self.rect.y = settings.tile_size * y
		

	def update_diamond_animation(self):
		if self.kind == 'blue':
			self.image = random.choice(self.graphics.diamond_images)
		elif self.kind == 'pink':
			self.image = random.choice(self.graphics.pink_diamond_images)

