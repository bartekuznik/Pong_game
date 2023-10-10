import pygame
import sys

pygame.init()
scr_h, scr_w = 400, 700
screen = pygame.display.set_mode((scr_w,scr_h))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    screen.fill((30,30,30))

    pygame.display.update()
    clock.tick(60)