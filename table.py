import pygame


class Tabel(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((10,50))
        self.rect = self.image.get_rect(topleft = pos)
        self.image.fill('white')

    def player_input(self):
        pass

    def update(self):
        self.player_input()


class LeftTable(Tabel):
    def __init__(self, pos):
        super().__init__(pos)

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.top > 0:
            self.rect.y -= 10
        if keys[pygame.K_s] and self.rect.bottom < 400:
            self.rect.y += 10
    
class RightTable(Tabel):
    def __init__(self, pos):
        super().__init__(pos)

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= 10
        if keys[pygame.K_DOWN] and self.rect.bottom < 400:
            self.rect.y += 10