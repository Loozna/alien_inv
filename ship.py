import pygame
import sys
class Ship():
	def __init__(self,screen,x,y):
		self.path = sys.path[0]
		self.screen = screen
		self.image = pygame.image.load(f'{self.path}/objects/ship.bmp')
		self.image = pygame.transform.scale(self.image,(100,100))
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		self.rect.centerx = x
		self.rect.bottom = y
		
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False
		self.rot_left = False
		
		self.speed = 1
		
	def blitme(self):
		self.screen.blit(self.image,self.rect)
		
	def update(self):
		if self.moving_right:
			self.rect.centerx += self.speed
		if self.moving_left:
			self.rect.centerx -= self.speed
		if self.moving_up:
			self.rect.bottom -= self.speed
		if self.moving_down:
			self.rect.bottom += self.speed
	
	def border_check(self):
		if self.rect.bottom >= 800:
			self.rect.bottom = 800
		if self.rect.top <= 0:
			self.rect.top = 0
		if self.rect.left <= 0:
			self.rect.left = 0
		if self.rect.right >= 1200:
			self.rect.right = 1200
		
