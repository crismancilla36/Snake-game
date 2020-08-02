import sys
import pygame
from constant import *

pygame.init()

#Surface
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake')

direction = UP
rect1 = [20, 20]

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = LEFT

            if event.key == pygame.K_RIGHT:
               direction = RIGHT
            
            if event.key == pygame.K_UP:
               direction = UP
            
            if event.key == pygame.K_DOWN:
               direction = DOWN
    
   
    screen.fill(DARK)

    rect1[0] += direction[0]
    rect1[1] += direction[1]

    pygame.draw.rect(screen, WHITE, (rect1[0]*NODE_SIZE, rect1[1]*NODE_SIZE, NODE_SIZE, NODE_SIZE))
    pygame.draw.rect(screen, GREEN, (0, 0, WIDTH, HEIGHT), 1)
    
    clock.tick(30)

    pygame.display.update()
