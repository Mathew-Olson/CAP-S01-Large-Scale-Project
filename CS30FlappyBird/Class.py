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
        self.radius = 20
        self.image.set_colorkey(Basic.PINK)
        #pygame.draw.circle(self.image, Basic.RED, self.rect.center, self.radius)
        self.rect.centerx = 100
        self.rect.bottom = Basic.HEIGHT /2
        self.speedy = 0
        
        
    def update(self):
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP]:
            self.speedy = -8
            #print(self.rect.bottom)
        if keystate[pygame.K_DOWN]:
            self.speedy = 8
            #print(self.rect.bottom)
        self.rect.y += self.speedy
        if self.rect.bottom > Basic.HEIGHT:
            self.rect.bottom = Basic.HEIGHT
        if self.rect.top < 0:
            self.rect.top  = 0



class Top_Pipe(pygame.sprite.Sprite):
    def __init__(self, top_pipe_image):
        pygame.sprite.Sprite.__init__(self)
        self.image = top_pipe_image
        self.rect = self.image.get_rect()
        self.rect.x = Basic.WIDTH - 100
        self.speedx = Basic.GAME_SPEED
        self.rect.y = -150
    
    def update(self):
        self.rect.x += self.speedx * -1
            
        

    