import pygame
import sys
from table import *

pygame.init()
scr_h, scr_w = 400, 700
screen = pygame.display.set_mode((scr_w,scr_h))
clock = pygame.time.Clock()

left_table = LeftTable((10,175))
right_table = RightTable((680,175))

tables = pygame.sprite.Group()
tables.add(left_table)
tables.add(right_table)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    screen.fill((30,30,30))

    tables.draw(screen)
    tables.update()

    pygame.display.update()
    clock.tick(60)