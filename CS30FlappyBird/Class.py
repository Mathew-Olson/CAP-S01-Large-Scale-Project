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

class Player(pygame.sprite.Sprite): #makes the bird
    def __init__(self, bird_image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(bird_image, (70, 58))
        self.rect = self.image.get_rect()
        self.radius = 20
        self.image.set_colorkey(Basic.PINK)
        #pygame.draw.circle(self.image, Basic.RED, self.rect.center, self.radius) #Shows the player hitbox
        self.rect.centerx = 100
        self.rect.bottom = Basic.HEIGHT /2
        self.speedy = 0
        
    def update(self):
        keystate = pygame.key.get_pressed() 
        if keystate[pygame.K_UP]: #increases the birds upward velocity
           self.speedy -= 2
        if keystate[pygame.K_DOWN] and self.speedy < 0: #decreases the birds upward velocity only if it has any
            self.speedy += 2
        self.speedy += 1
        self.rect.y += self.speedy
        if self.rect.bottom > Basic.HEIGHT:
            self.rect.bottom = Basic.HEIGHT
            self.speedy = 0
        if self.rect.top < 0:
            self.rect.top  = 0
            self.speedy = 0
        #print(self.speedy) #shows the speed of the bird
        #print(self.rect.bottom) #shows the location of the bird
        


class Top_Pipe(pygame.sprite.Sprite):
    def __init__(self, top_pipe_image, pipe_choice):
        pygame.sprite.Sprite.__init__(self)
        self.image = top_pipe_image
        self.rect = self.image.get_rect()
        self.rect.x = Basic.WIDTH + 100
        self.speedx = Basic.GAME_SPEED
        self.rect.y = pipe_choice
    
    def update(self):
        self.rect.x += self.speedx * -1


class Bot_Pipe(pygame.sprite.Sprite):
    def __init__(self, pipe_bot_image, pipe_choice):
        pygame.sprite.Sprite.__init__(self)
        self.image = pipe_bot_image
        self.rect = self.image.get_rect()
        self.rect.x = Basic.WIDTH + 100
        self.speedx = Basic.GAME_SPEED
        self.rect.y = pipe_choice
    
    def update(self):
        self.rect.x += self.speedx * -1    
        

    