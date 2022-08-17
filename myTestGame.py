from math import pi
import pygame
from pygame.locals import *
import random

window_sz = (1024, 768)
pixel_sz = 10
#spawn apple
def rand():
    x = random.randint(0,window_sz[0])
    y = random.randint(0,window_sz[1])
    return x // pixel_sz * pixel_sz, y // pixel_sz * pixel_sz

#colisao
def col(pos1, pos2):
    return pos1 == pos2

def limit(pos):
    if 0 <= pos[0] < window_sz[0] and 0 <= pos[1] < window_sz[1]:
        return False
    else:
        return True

pygame.init()
screen = pygame.display.set_mode(window_sz)
pygame.display.set_caption('Cobrinha')

#croba
snake_position = [(250, 50), (260, 50), (270,50)]
snake_surface = pygame.Surface((pixel_sz, pixel_sz))
snake_surface.fill((15, 94, 18))
snake_moves = K_LEFT

#maca
apple_surface = pygame.Surface((pixel_sz, pixel_sz))
apple_surface.fill((255, 0, 0))
apple_position = rand()

#reiniciar game
def restart():
    global snake_position
    global apple_position
    global snake_moves
    snake_position = [(250, 50), (260, 50), (270,50)]
    snake_moves = K_LEFT
    apple_position = rand()

while True:
    pygame.time.Clock().tick(30)
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
        elif event.type == KEYDOWN:
            if event.key in [K_UP, K_DOWN, K_LEFT, K_RIGHT]:
                snake_moves = event.key

    screen.blit(apple_surface, apple_position)

    if col(apple_position, snake_position[0]):
        snake_position.append((0, 0))
        apple_position = rand()

    for pos in snake_position:
        screen.blit(snake_surface, pos)
    
    for i in range(len(snake_position)-1, 0, -1):
        if col(snake_position[0], snake_position[i]):
            restart()
        snake_position[i] = snake_position[i-1]
    
    if limit(snake_position[0]):
        restart()

    if snake_moves == K_UP:
        snake_position[0] = (snake_position[0][0], snake_position[0][1] - pixel_sz)
    elif snake_moves == K_DOWN:
        snake_position[0] = (snake_position[0][0], snake_position[0][1] + pixel_sz)
    elif snake_moves == K_LEFT:
        snake_position[0] = (snake_position[0][0] - pixel_sz, snake_position[0][1])
    elif snake_moves == K_RIGHT:
        snake_position[0] = (snake_position[0][0] + pixel_sz, snake_position[0][1])
    
    pygame.display.update()