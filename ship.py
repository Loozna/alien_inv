import pygame
import sys
class Ship():
	def __init__(self,screen):
		self.path = sys.path[0]
		self.screen = screen
		self.image = pygame.image.load(f'{self.path}/objects/ship.bmp')
		self.image = pygame.transform.scale(self.image,(100,100))
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
	def blitme(self):
		self.screen.blit(self.image,self.rect)
