import pygame
import settings

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups) -> None:
        super().__init__(groups)
        self.image = pygame.image.load('./graphics/test/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

        # gets direction as a 2D vector representing x and y
        # will be multiplied by some speed after setting x and y
        # to some keyboard input (up, down, left, right)
        self.direction = pygame.math.Vector2()
        self.speed = 5
    
    # takes keyboard input and sets direction of player
    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction[1] = -1
        elif keys[pygame.K_DOWN]:
            self.direction[1] = 1
        else:
            self.direction[1] = 0
        
        if keys[pygame.K_LEFT]:
            self.direction[0] = -1
        elif keys[pygame.K_RIGHT]:
            self.direction[0] = 1
        else:
            self.direction[0] = 0
    
    # moves the center of the player according to direction and speed
    def move(self, speed):
        self.rect.center += self.direction * speed

    def update(self) -> None:
        self.input()
        self.move(self.speed)