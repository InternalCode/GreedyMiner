import pygame
import functions
import time
from player import Player
from settings import Settings
from background import Background
from main_screen import Main_screen
from graphics import Graphics
from hiscores import Hiscores
from gamecontrol import Gamecontrol

def start():
	fps = pygame.time.Clock()
	pygame.init()
	pygame.key.set_repeat(50, 100)
	
	settings = Settings()
	#icon
	ico = pygame.image.load('graphics\\windowico\\ico.png')
	pygame.display.set_icon(ico)
	display = pygame.display.set_mode((settings.screen_w, settings.screen_h), pygame.DOUBLEBUF, 16)
	
	hiscores = Hiscores()
	pygame.display.set_caption('Greedy Miner')
	main_screen = Main_screen(display, hiscores)
	graphics = Graphics(settings)
	tiles = functions.prepare_random_tiles(settings)

	#groups
	dirt_group = pygame.sprite.Group()
	stone_group = pygame.sprite.Group()
	diamond_group = pygame.sprite.Group()
	dynamite_group = pygame.sprite.Group()
	bat_group = pygame.sprite.Group()

	functions.generate_tile_objects(tiles, settings, dirt_group, stone_group, diamond_group, bat_group, graphics)
	
	player = Player(settings, dirt_group, graphics)
	gamecontrol = Gamecontrol(display, settings, hiscores, diamond_group)
	background = Background(settings, player, graphics)
	
	
	while True:
		if settings.is_active == True:
			#draw tiles on screen
			functions.update_tiles_draw(display, player, background, dirt_group, stone_group, diamond_group, dynamite_group, bat_group, gamecontrol)
			#read keys
			functions.key_control(settings, player)
			#act player
			functions.check_next_tiles(settings, player, diamond_group, stone_group, dirt_group, hiscores, bat_group)
			#update logic
			functions.update_tiles(settings, display, player, background, dirt_group, stone_group, diamond_group, dynamite_group, bat_group, graphics, gamecontrol)
			#player
			functions.player(settings, player)
			#generate next level
			if gamecontrol.check_diamonds() and player.alive == True:
				del player
				functions.erase_old_game(settings, dirt_group, stone_group, diamond_group, dynamite_group, bat_group)
				del tiles
				tiles = functions.prepare_random_tiles(settings)
				functions.generate_tile_objects(tiles, settings, dirt_group, stone_group, diamond_group, bat_group, graphics)
				player = Player(settings, dirt_group, graphics)
		else:
			if settings.need_clean == True:
				gamecontrol.reset()
				functions.erase_old_game(settings, dirt_group, stone_group, diamond_group, dynamite_group, bat_group)
				del player
				#count point
				hiscores.check_hiscores_reset_old()
				del tiles
				tiles = functions.prepare_random_tiles(settings)
				functions.generate_tile_objects(tiles, settings, dirt_group, stone_group, diamond_group, bat_group, graphics)
				player = Player(settings, dirt_group, graphics)
				settings.need_clean = False

			#read keys
			functions.key_control(settings, player)
			#display main screen
			functions.main_screen(main_screen)

		fps.tick(30)
		pygame.display.flip()

if __name__ == '__main__':
	start()
