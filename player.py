import pygame
import settings

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups) -> None:
        super().__init__(groups)
        self.image = pygame.image.load('./graphics/test/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)