import sys
import pygame
from constant import *
from snake import Snake

#Surface
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('Snake')

direction = UP
rect1 = [200, 200]

moves = { 
    pygame.K_UP: UP, 
    pygame.K_DOWN: DOWN, 
    pygame.K_LEFT: LEFT, 
    pygame.K_RIGHT: RIGHT
    }

snake = Snake(SCREEN_SIZE, NODE_SIZE, UP) 
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            snake.change_direction(moves.get(event.key, direction))

    snake.move() 
    
    screen.fill(DARK)
    for node in snake.body:
        pygame.draw.rect(screen, WHITE, (node[0], node[1], NODE_SIZE, NODE_SIZE))

    pygame.draw.rect(screen, GREEN, (0, 0, SCREEN_SIZE[0], SCREEN_SIZE[1]), 1)
    
    clock.tick(30)
    pygame.display.update()
