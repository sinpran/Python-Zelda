import pygame
import settings
from tile import Tile
from player import Player

class Level:
    def __init__(self) -> None:
        
        # get display surface 
        self.display_surface = pygame.display.get_surface()

        # create sprite groups
        self.visibile_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

        #sprite setup
        self.create_map()

    def create_map(self):
        for row_index, row in enumerate(settings.WORLD_MAP):
            for col_index, col in enumerate(settings.WORLD_MAP[0]):
                x = col_index * settings.TILESIZE
                y = row_index * settings.TILESIZE
                if settings.WORLD_MAP[row_index][col_index] == 'x':
                    Tile((x,y), [self.visibile_sprites])
                if settings.WORLD_MAP[row_index][col_index] == 'p':
                    Player((x,y), [self.visibile_sprites])

    def run(self):
        #update and draw game
        self.visibile_sprites.draw(self.display_surface)