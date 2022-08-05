import pygame
import settings

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites) -> None:
        super().__init__(groups)
        self.image = pygame.image.load('./graphics/test/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

        # gets direction as a 2D vector representing x and y
        # will be multiplied by some speed after setting x and y
        # to some keyboard input (up, down, left, right)
        self.direction = pygame.math.Vector2()
        self.speed = 5

        self.obstacle_sprites = obstacle_sprites
    
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
        # normalize direction vector so we have consistent speed
        # when moving diagonally 
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.rect[0] += self.direction[0] * speed
        self.collision('horizontal')
        self.rect[1] += self.direction[1] * speed
        self.collision('vertical')
        #self.rect.center += self.direction * speed

    # checks for collisions between sprites
    # determines whether horizontal or vertical
    # collision and place sprites accordingly
    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction[0] > 0: # moving right
                        self.rect.right = sprite.rect.left
                    if self.direction[0] < 0: # moving left
                        self.rect.left = sprite.rect.right

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction[1] > 0: # moving down
                        self.rect.bottom = sprite.rect.top
                    if self.direction[1] < 0: # moving up
                        self.rect.top = sprite.rect.bottom

    def update(self) -> None:
        self.input()
        self.move(self.speed)