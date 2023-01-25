import pygame

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 4

        # Player sprites
        cyclop_left_base = pygame.image.load('./resources/monsters/cyclop/cyclop_left.png').convert_alpha()
        cyclop_right_base = pygame.image.load('./resources/monsters/cyclop/cyclop_right.png').convert_alpha()
        cyclop_front_base = pygame.image.load('./resources/monsters/cyclop/cyclop_front.png').convert_alpha()
        cyclop_back_base = pygame.image.load('./resources/monsters/cyclop/cyclop_back.png').convert_alpha()

        self.left = pygame.transform.scale(cyclop_left_base, (64, 64))
        self.right = pygame.transform.scale(cyclop_right_base, (64, 64))
        self.front = pygame.transform.scale(cyclop_front_base, (64, 64))
        self.back = pygame.transform.scale(cyclop_back_base, (64, 64))

        self.sprite = self.front

        # Cleanup
        del cyclop_back_base, cyclop_front_base, cyclop_right_base, cyclop_left_base

    def get_oriented(self):
        return self.sprite

    def update(self, screen):
        screen.blit(self.sprite, (self.x, self.y))

    def move(self, keys):
        
        if keys[pygame.K_w]:
            self.y -= self.vel
            self.sprite = self.back
            
        elif keys[pygame.K_s]:
            self.y += self.vel
            self.sprite = self.front
        
        if keys[pygame.K_a]:
            self.x -= self.vel
            self.sprite = self.left

        elif keys[pygame.K_d]:
            self.x += self.vel
            self.sprite = self.right

        if keys[pygame.K_LSHIFT]:
            self.vel = 6
        else:
            self.vel = 3