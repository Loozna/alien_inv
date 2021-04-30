import sys
import pygame
from obstacles import Obstacle
from settings import Settings
def check_events(ship,obstacles,ai_settings,screen):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				ship.moving_right = True
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:
				ship.moving_right = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				ship.moving_left = True
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				ship.moving_left = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				ship.moving_up = True
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_UP:
				ship.moving_up = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_DOWN:
				ship.moving_down = True
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_DOWN:
				ship.moving_down = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				new_obstacle = Obstacle(ai_settings,screen)
				obstacles.add(new_obstacle)
				
			
def update_screen(ai_settings,screen,ship,obstacles):
	screen.fill(ai_settings.bg_color)
	ship.blitme()
	pygame.display.flip()
	ship.update()
	for obstacle in obstacles.sprites():
	
		obstacle.draw_obstacle()
