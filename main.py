import random
import pygame
from pygame.locals import *
from Ground import Ground
from Bird import Bird
from Pipe import Pipe

screen_width = 400
screen_height = 720

ground_width = 2 * screen_width
ground_height = 100

pipe_width = 80
pipe_height = 500

pipe_gap = 200

game_speed = 10
speed = 10
gravity = 1

def is_off_screen(sprite):
    return sprite.rect[0] < -(sprite.rect[2])

def get_random_pipes(xpos):
    size = random.randint(100, 300)
    pipe = Pipe(False, xpos, size,pipe_width,pipe_height,screen_height)
    size = screen_height - size - pipe_gap
    pipe_inverted = Pipe(True, xpos, size,pipe_width,pipe_height,screen_height)
    return (pipe, pipe_inverted)

pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
background = pygame.image.load('imagens/fundo.png')
background = pygame.transform.scale(background,(screen_width,screen_height))

bird_group = pygame.sprite.Group()
bird = Bird(speed,screen_width/2,screen_height/2)
bird_group.add(bird)

ground_group = pygame.sprite.Group()
for i in range(2):
    ground = Ground(ground_width * i,ground_width,ground_height,screen_height)
    ground_group.add(ground)

pipe_group = pygame.sprite.Group()
for i in range(2):
    pipes = get_random_pipes(screen_width * i + 800)
    pipe_group.add(pipes[0])
    pipe_group.add(pipes[1])

clock = pygame.time.Clock()
gameover = False
while not gameover:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == QUIT:
            gameover = True
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                bird.bump(-speed)
        
    screen.blit(background,(0,0))

    if is_off_screen(ground_group.sprites()[0]):
        ground_group.remove(ground_group.sprites()[0])

        new_ground = Ground(ground_width - 20,ground_width,ground_height,screen_height)
        ground_group.add(new_ground)
    if is_off_screen(pipe_group.sprites()[0]):
        pipe_group.remove(pipe_group.sprites()[0])
        pipe_group.remove(pipe_group.sprites()[0])

        pipes = get_random_pipes(screen_width * 2)

        pipe_group.add(pipes[0])
        pipe_group.add(pipes[1])

    bird_group.update(gravity)
    ground_group.update(game_speed) #add game_speed
    pipe_group.update(game_speed)
    pipe_group.draw(screen)
    bird_group.draw(screen)
    ground_group.draw(screen)
    pygame.display.update()

    if (pygame.sprite.groupcollide(bird_group, ground_group, False, False, pygame.sprite.collide_mask) or
       pygame.sprite.groupcollide(bird_group, pipe_group, False, False, pygame.sprite.collide_mask)):
        gameover = True