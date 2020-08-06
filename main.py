import sys
import pygame
import random
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

apple = ( 
        NODE_SIZE * random.randint(0, SCREEN_SIZE[0]//NODE_SIZE),
        NODE_SIZE * random.randint(0, SCREEN_SIZE[1]//NODE_SIZE)
        )
snake = Snake(SCREEN_SIZE, NODE_SIZE, UP) 
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            snake.change_direction(moves.get(event.key, direction))

    game_over = not snake.move()
    if not apple == snake.body[0]:    
        snake.body.pop()
    while  apple in snake.body:
        apple = (
                NODE_SIZE * random.randint(0, SCREEN_SIZE[0]//NODE_SIZE),
                NODE_SIZE * random.randint(0, SCREEN_SIZE[1]//NODE_SIZE)
                )
    
    screen.fill(DARK)
    
    pygame.draw.rect(screen, RED, (apple[0], apple[1], NODE_SIZE, NODE_SIZE))
    for node in snake.body:
        pygame.draw.rect(screen, WHITE, (node[0], node[1], NODE_SIZE, NODE_SIZE))

    pygame.draw.rect(screen, GREEN, (0, 0, SCREEN_SIZE[0], SCREEN_SIZE[1]), 1)
    
    pygame.time.delay(TIMER)
    pygame.display.update()

