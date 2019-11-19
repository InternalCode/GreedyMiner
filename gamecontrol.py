import pygame, time

class Gamecontrol():
	def __init__(self, display, settings, hiscores, diamond_group):
		self.display = display
		self.hiscores = hiscores
		self.settings = settings
		self.dynamites = self.settings.dynamites
		self.display_size = self.display.get_size()
		
		self.diamond_group = diamond_group
		self.level = 1
		self.difficulity_rate = self.settings.difficulity_rate
		
		self.finished = False
		self.timer = 0
		
		#font settings
		self.font_big = pygame.font.Font('font\\font.ttf', 64)
		self.font_small = pygame.font.Font('font\\font.ttf', 18)
		#level complete
		self.text_level_complete = self.font_big.render('Level Complete', True, (250,250,250))
		self.text_level_complete_rect = self.text_level_complete.get_rect()
		self.text_level_complete_rect.centerx = int(self.display_size[0] * 0.5)
		self.text_level_complete_rect.centery = int(self.display_size[1] * 0.5)
		#scores
		self.text_scores = self.font_small.render('Scores %s' %self.hiscores.scores, True, (250,250,250))
		self.text_scores_rect = self.text_scores.get_rect()
		self.text_scores_rect.left = 10
		self.text_scores_rect.top = 20
		#dynamites
		self.text_dynamites = self.font_small.render('Dynamites %s' %self.hiscores.scores, True, (250,250,250))
		self.text_dynamites_rect = self.text_dynamites.get_rect()
		self.text_dynamites_rect.left = 110
		self.text_dynamites_rect.top = 20
		#level
		self.text_level = self.font_small.render('Level %s' %self.level, True, (250,250,250))
		self.text_level_rect = self.text_level.get_rect()
		self.text_level_rect.left = 220
		self.text_level_rect.top = 20
		#dead
		self.text_player_death = self.font_big.render('Player died', True, (250,250,250))
		self.text_player_death_rect = self.text_level_complete.get_rect()
		self.text_player_death_rect.centerx = int(self.display_size[0] * 0.5)
		self.text_player_death_rect.centery = int(self.display_size[1] * 0.5)
		

	def print_data(self):
		#scores
		self.text_scores = self.font_small.render('Scores %s' %self.hiscores.scores, True, (250,250,250))
		self.display.blit(self.text_scores, self.text_scores_rect)
		#dynamites
		self.text_dynamites = self.font_small.render('Dynamites %s' %self.dynamites, True, (250,250,250))
		self.display.blit(self.text_dynamites, self.text_dynamites_rect)
		#level
		self.text_level = self.font_small.render('Level %s' %self.level, True, (250,250,250))
		self.display.blit(self.text_level, self.text_level_rect)
		

	def check_diamonds(self):
		if self.finished == False:
			if len(self.diamond_group) == 0:
				self.timer = int(time.time()) + 3
				self.finished = True
		else:
			self.display.blit(self.text_level_complete, self.text_level_complete_rect)
			if self.timer < int(time.time()):
				self.finished = False
				#reset dynamie per level amount
				self.dynamites = self.settings.dynamites
				self.difficulity_rate += 5
				#add level
				self.level += 1
				return True
	
	def player_death(self):
		self.display.blit(self.text_player_death, self.text_player_death_rect)
		

	#reset settings
	def reset(self):
		self.difficulity_rate = self.settings.difficulity_rate
		self.level = 1
		
