import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
def run_game():
	ai_settings = Settings()
	pygame.init()
	screen = pygame.display.set_mode((
	ai_settings.screen_width,
	ai_settings.screen_height))
	ship = Ship(screen)
	pygame.display.set_caption('Inwazja obcych')
	bg_color = ai_settings.bg_color
	while True:
		gf.update_screen(ai_settings,screen,ship)
		gf.check_events(ship)
		ship.update()
				
run_game()
