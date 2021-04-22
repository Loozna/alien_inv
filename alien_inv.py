import sys
import pygame
from settings import Settings
def run_game():
	ai_settings = Settings()
	pygame.init()
	screen = pygame.display.set_mode((
	ai_settings.screen_width,
	ai_settings.screen_height))
	pygame.display.set_caption('Inwazja obcych')
	bg_color = ai_settings.bg_color
	while True:
		screen.fill(bg_color)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		pygame.display.flip()
				
run_game()
