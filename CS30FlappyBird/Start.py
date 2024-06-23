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
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()
pygame.time.set_timer(Basic.TIMEREVENT, Basic.pipe_spawn_speed)  #initilize timer number is milliseconds per event

#game graphics
bird_image = pygame.image.load(path.join(Basic.img_dir, 'bird.png')).convert()
pipe_top_image = pygame.image.load(path.join(Basic.img_dir, 'pipe_top.png')).convert()
pipe_bot_image = pygame.image.load(path.join(Basic.img_dir, 'pipe_bot.png')).convert()
background = pygame.image.load(path.join(Basic.img_dir, 'backround.jpg')).convert()
background = pygame.transform.scale(background,Basic.BACKROUND_SIZE)
background_rect = background.get_rect()


#all sprites
all_sprites = pygame.sprite.Group()
pipes = pygame.sprite.Group()
player = Class.Player(bird_image)
all_sprites.add(player)

pipe_choice = random.randrange(-450, -10)
pipe_top = Class.Top_Pipe(pipe_top_image, pipe_choice)
all_sprites.add(pipe_top)
pipes.add(pipe_top)

pipe_bot = Class.Bot_Pipe(pipe_bot_image,  650 - (pipe_choice * -1))
all_sprites.add(pipe_bot)
pipes.add(pipe_bot)



#game Loop
running = True 
while running:
    # keep loop running at the right speed
    clock.tick(Basic.FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        #check timer for adding new pipe
        elif event.type == Basic.TIMEREVENT: 
            #print('Pipe Spawned')
            pipe_choice = random.randint(-450, -10)
            pipe = Class.Top_Pipe(pipe_top_image, pipe_choice) #spawns top pipe
            all_sprites.add(pipe)
            pipes.add(pipe)
            
            pipe_bot = Class.Bot_Pipe(pipe_bot_image, 650 - (pipe_choice * -1) ) #spawns bot pipe
            all_sprites.add(pipe_bot)
            pipes.add(pipe_bot)
                        
            
    # Update
    all_sprites.update()
    
    
        
    
    #wall collisions
    collision = pygame.sprite.spritecollide(player, pipes, False)
    if collision:
        running = False
    
    # Draw / render
    screen.fill(Basic.BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()