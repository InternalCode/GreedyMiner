import pygame, os

class Graphics():
	def __init__(self, settings):
		self.settings = settings
		self.dirt_images = list()
		self.stone_images = list()
		self.diamond_images = list()
		
		self.dynamite_images = list()
		self.player_images = list()
		self.bat_images = list()
		self.pink_diamond_images = list()

		self.background_images = list()
		
		self.load_tiles(self.dirt_images, 'tiles')
		self.load_tiles(self.stone_images, 'stone')
		self.load_tiles(self.diamond_images, 'diamond')
		self.load_tiles(self.dynamite_images, 'dynamite')
		self.load_tiles(self.player_images, 'player')
		self.load_tiles(self.bat_images, 'bat')
		
		self.load_tiles(self.pink_diamond_images, 'pink_diamond')
		
		self.load_background(self.background_images, 'background')

	def load_tiles(self, image_list, category):
		path = os.path.join('graphics', category)
		for image in os.listdir(path):
			image_list.append(pygame.transform.scale(pygame.image.load(os.path.join(path, image)).convert_alpha(),
				(self.settings.tile_size, self.settings.tile_size)))
				
	def load_background(self, image_list, category):
		path = os.path.join('graphics', category)
		for image in os.listdir(path):
			image_list.append(pygame.image.load(os.path.join(path, image)))
