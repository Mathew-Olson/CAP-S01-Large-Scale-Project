#this file contains all the Classes for my game
import pygame
import random
import sys
import Basic



def draw_text(surf, text, size, x, y): #for the scoreboard (will need tweaking)
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

class Player(pygame.sprite.Sprite):
    def __init__(self, bird_image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(bird_image, (70, 58))
        self.rect = self.image.get_rect()
        self.rect.center = (Basic.HEIGHT/2, Basic.HEIGHT/2)
        self.velocity = 0
        
    def update(self):
        self.rect.x += self.speedx
        
        if self.rect.bottom > screen_height:
            self.rect.bottom = Basic.HEIGHT
            self.velocity = 0
        

    