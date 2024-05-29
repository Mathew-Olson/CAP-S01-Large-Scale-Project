
import pygame
import random
from MagicNumbers import Basic
from MagicNumbers import Class


# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((Basic.WIDTH, Basic.HEIGHT))
pygame.display.set_caption("")
clock = pygame.time.Clock()

#all sprites
all_sprites = pygame.sprite.Group()
player = Class.Player()
all_sprites.add(player)

#game graphics
bird_image = pygame.image.load(path.join(img_dir, 'bird.png')).convert()

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