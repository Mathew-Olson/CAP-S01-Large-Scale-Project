from os import path
import pygame
import random
import Basic
import Class
import sys
import time

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((Basic.WIDTH, Basic.HEIGHT))
pygame.display.set_caption("Fappy Bird")
clock = pygame.time.Clock()

#game graphics
bird_image = pygame.image.load(path.join(Basic.img_dir, 'bird.png')).convert()
pipe_top = pygame.image.load(path.join(Basic.img_dir, 'pipe_top.png')).convert()
pipe_bot = pygame.image.load(path.join(Basic.img_dir, 'pipe_top.png')).convert()

#all sprites
all_sprites = pygame.sprite.Group()
player = Class.Player(bird_image)
all_sprites.add(player)


# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(Basic.FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Update
    

    # Draw / render
    screen.fill(Basic.BLACK)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()