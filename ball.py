from typing import Any
import pygame
from pygame.sprite import AbstractGroup 

class Ball(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((5,5))
        self.rect = self.image.get_rect(topleft = pos)
        self.image.fill('white')
        self.x_speed = 3
        self.y_speed = 3

    def movement(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

    def update(self):
        self.movement()