import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
	
	ai_settings = Settings()
	pygame.init()
	screen = pygame.display.set_mode((
	ai_settings.screen_width,
	ai_settings.screen_height))
	ship = Ship(screen,550,1200)
	pygame.display.set_caption('Inwazja obcych')
	bg_color = ai_settings.bg_color
	obstacles = Group()
	while True:
		ship.update()
		ship.border_check()
		gf.check_events(ship,obstacles,ai_settings,screen)
		gf.update_screen(ai_settings,screen,ship,obstacles)
run_game()
