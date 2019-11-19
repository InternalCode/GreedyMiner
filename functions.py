import pygame, sys, random, time
from settings import Settings
from stone import Stone
from diamond import Diamond
from dirt import Dirt
from dynamite import Dynamite
from bat import Bat

def prepare_random_tiles(settings):
	tiles = list()
	tmp = list()
	for i in range(int(settings.screen_h / settings.tile_size)):
		for ii in range(int(settings.screen_w / settings.tile_size)):
			tmp.append(random.randint(0, 100))
		tiles.append(list(tmp))
		tmp.clear()
	return tiles

def generate_tile_objects(tiles, settings, dirt_group, stone_group, diamond_group, bat_group, graphics):
	for i in range(len(tiles)):
		for ii in range(len(tiles[i])):
			if tiles[i][ii] >= 0 and tiles[i][ii] <= 90 - settings.difficulity_rate:
				if check_for_empty(settings) == True:
					check_for_bat(settings, i, ii, graphics, bat_group)
					continue
				else:
					dirt = Dirt(settings, i, ii, graphics)
					dirt_group.add(dirt)
			elif tiles[i][ii] >= 91 - settings.difficulity_rate and tiles[i][ii] <= 96:
				if check_for_empty(settings) == True:
						check_for_bat(settings, i, ii, graphics, bat_group)
						continue
				else:	
					stone = Stone(settings, i, ii, graphics)
					stone_group.add(stone)
			elif tiles[i][ii] >= 97 and tiles[i][ii] <= 100:
				if check_for_empty(settings) == True:
					check_for_bat(settings, i, ii, graphics, bat_group)
					continue
				else:
					diamond = Diamond(settings, i, ii, graphics, 'blue')
					diamond_group.add(diamond)

#chanse for bat
def check_for_bat(settings, i, ii, graphics, bat_group):
	chance = random.randint(0, 100)
	if chance <= settings.chanse_for_bat:
		bat = Bat(settings, i, ii, graphics)
		bat_group.add(bat)

#chanse for empty tile:
def check_for_empty(settings):
	empty = random.randint(0, 100)
	if empty <= settings.chanse_for_empty:
		return True
	
def main_screen(main_screen):
	main_screen.draw()

def erase_old_game(settings, dirt_group, stone_group, diamond_group, dynamite_group, bat_group):
	dirt_group.empty()
	stone_group.empty()
	diamond_group.empty()
	dynamite_group.empty()
	bat_group.empty()
	
def update_tiles_draw(display, player, background, dirt_group, stone_group, diamond_group, dynamite_group, bat_group, gamecontrol):
	# draw background
	display.blit(background.image, background.rect)
	for dirt in dirt_group:
		display.blit(dirt.image, dirt.rect)
		if dirt.image_special != None:
			display.blit(dirt.image_special, dirt.rect)
	for stone in stone_group:
		display.blit(stone.image, stone.rect)
	for diamond in diamond_group:
		display.blit(diamond.image, diamond.rect)
	display.blit(player.image, player.rect)
	for dynamite in dynamite_group:
		display.blit(dynamite.image, dynamite.rect)
	for bat in bat_group:
		display.blit(bat.image, bat.rect)
	gamecontrol.print_data()
	if player.alive == False:
		gamecontrol.player_death()


def update_tiles(settings, display, player, background, dirt_group, stone_group, diamond_group, dynamite_group, bat_group, graphics, gamecontrol):
	# remove dirt by player if alive
	if player.alive:
		if pygame.sprite.spritecollideany(player, dirt_group):
			dirt_group.remove(pygame.sprite.spritecollideany(player, dirt_group))
	#deploy dynamite
	if player.deploy_dynamite == True and gamecontrol.dynamites > 0:
		gamecontrol.dynamites -= 1
		deploy_dynamite(settings, player, dynamite_group, graphics)
	# update stone tiles
	dirt_group.update(dirt_group)
	stone_group.update(player, stone_group, diamond_group, dirt_group, dynamite_group, bat_group)
	diamond_group.update(player, stone_group, diamond_group, dirt_group, dynamite_group, bat_group)
	background.update(player)
	dynamite_group.update(player, dirt_group, stone_group, diamond_group, dynamite_group)
	bat_group.update(player, dirt_group, stone_group, diamond_group, bat_group)

def player(settings, player):
	#"animation" of character
	player.update_player()
	if player.suicide == True:
		player.death()
		player.suicide = False
	if player.alive == False:
		if player.death_seq < round(time.time()):
			settings.is_active = False
			settings.need_clean = True
		
def deploy_dynamite(settings, player, dynamite_group, graphics):
	dynamite = Dynamite(settings, player, graphics)
	dynamite_group.add(dynamite)
	player.deploy_dynamite = False

def check_next_tiles(settings, player, diamond_group, stone_group, dirt_group, hiscores, bat_group):
		#var to flip avatar
		player.last_move_or_action['move'] = player.direction
		#checkers
		checker_1 = pygame.Rect(player.rect)
		checker_2 = pygame.Rect(player.rect)
		#flags
		f_1 = False
		f_2 = False
		#set checkers
		if player.direction == 'right':
			checker_1.x += settings.tile_size
			checker_2.x += settings.tile_size * 2
		elif player.direction == 'left':
			checker_1.x -= settings.tile_size
			checker_2.x -= settings.tile_size * 2
		elif player.direction == 'up':
			checker_1.y -= settings.tile_size
		elif player.direction == 'down':
			checker_1.y += settings.tile_size

		#general diamond check
		for diamond in diamond_group:
			if checker_1 == diamond.rect:
				if diamond.kind == 'blue':
					diamond_group.remove(diamond)
					#add score
					hiscores.scores += settings.score_diamond_blue
				
				elif diamond.kind == 'pink':
					diamond_group.remove(diamond)
					hiscores.scores += settings.score_diamond_pink

			elif checker_2 == diamond:
				f_2 = True
				
		#general edges check
		if checker_1.left < 0 or checker_1.right > settings.screen_w or checker_1.top < 0 or checker_1.bottom > settings.screen_h:
			return 0
			
		#vertical check
		if player.direction == 'up' or player.direction == 'down':
			player.direction = ''
			for stone in stone_group:
				if checker_1 == stone.rect:
					return 0
			player.rect = checker_1
			
		#horizontal check
		elif player.direction == 'left' or player.direction == 'right':
			player.direction = ''
			#stone check
			for stone in stone_group:
				if stone.rect == checker_1:
					f_1 = True
					this_stone = stone
				if stone.rect == checker_2:
					f_2 = True
			#dirt check
			for dirt in dirt_group:
				if dirt.rect == checker_2:
					f_2 = True
			#bat check
			for bat in bat_group:
				if bat.rect == checker_2:
					f_2 = True
			
			#check edges of the screen if pust stone
			if checker_2.left < 0 or checker_2.right > settings.screen_w:
				f_2 = True

			#logic
			if f_1 == True and f_2 == False:
				this_stone.rect = checker_2
				player.rect = checker_1
			elif f_1 == True and f_2 == True:
				return 0
			player.rect = checker_1

def key_control(settings, player):
	for e in pygame.event.get():
		if e.type == pygame.KEYDOWN:
			if e.key == pygame.K_q:
				pygame.quit()
				sys.exit()
			if player.alive:
				if settings.is_active == True:
					if e.key == pygame.K_BACKSPACE:
						player.suicide = True
					if e.key == pygame.K_SPACE:
						player.deploy_dynamite = True
					if e.key == pygame.K_UP:
						player.direction = 'up'
					if e.key == pygame.K_DOWN:
						player.direction = 'down'
					if e.key == pygame.K_LEFT:
						player.direction = 'left'
					if e.key == pygame.K_RIGHT:
						player.direction = 'right'
				if e.key == pygame.K_RETURN:
					settings.is_active = True
		if e.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		# ~ if e.type == pygame.KEYUP:
			# ~ if player.alive:
				# ~ if e.key == pygame.K_UP:
					# ~ player.direction = ''
				# ~ if e.key == pygame.K_DOWN:
					# ~ player.direction = ''
				# ~ if e.key == pygame.K_LEFT:
					# ~ player.direction = ''
				# ~ if e.key == pygame.K_RIGHT:
					# ~ player.direction = ''

