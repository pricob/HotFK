import math
import pygame
import sys

from math import atan2
from pygame.locals import *
from maintenance import clear_project
from health import healthBar

class Bullet:
    def __init__(self, x, y):
        self.pos = (x, y)
        mx, my = pygame.mouse.get_pos()
        self.dir = (mx - x, my - y)
        length = math.hypot(*self.dir)
        if length == 0.0:
            self.dir = (0, -1)
        else:
            self.dir = (self.dir[0]/length, self.dir[1]/length)
        angle = math.degrees(math.atan2(-self.dir[1], self.dir[0]))

        self.bullet = pygame.Surface((14, 4)).convert_alpha()
        self.bullet.fill((255, 255, 255))
        self.bullet = pygame.transform.rotate(self.bullet, angle)
        self.speed = 30

    def changed(self):
        self.bullet = pygame.Surface((50, 10)).convert_alpha()
        angle = math.degrees(math.atan2(-self.dir[1], self.dir[0]))
        self.bullet.fill((255, 0, 0))
        self.bullet = pygame.transform.rotate(self.bullet, angle)
        self.speed = 10

    def update(self):
        self.pos = (self.pos[0]+self.dir[0]*self.speed, 
                    self.pos[1]+self.dir[1]*self.speed)

    def draw(self, surf):
        bullet_rect = self.bullet.get_rect(center = self.pos)
        surf.blit(self.bullet, bullet_rect)

    def get_rect(self):
        return self.bullet.get_rect(center = self.pos)

def menu_loop(mainClock):
    debug_tile_base = pygame.image.load('./resources/tiles/debug_tile.png').convert_alpha()
    debug_tile = pygame.transform.scale(debug_tile_base, (32, 32))
    cyclop_left_base = pygame.image.load('./resources/monsters/cyclop/cyclop_left.png').convert_alpha()
    cyclop_right_base = pygame.image.load('./resources/monsters/cyclop/cyclop_right.png').convert_alpha()
    cyclop_front_base = pygame.image.load('./resources/monsters/cyclop/cyclop_front.png').convert_alpha()
    cyclop_back_base = pygame.image.load('./resources/monsters/cyclop/cyclop_back.png').convert_alpha()

    cyclop_left = pygame.transform.scale(cyclop_left_base, (64, 64))
    cyclop_right = pygame.transform.scale(cyclop_right_base, (64, 64))
    cyclop_front = pygame.transform.scale(cyclop_front_base, (64, 64))
    cyclop_back = pygame.transform.scale(cyclop_back_base, (64, 64))

    # DEBUG boss
    imp_front_base = pygame.image.load('./resources/monsters/imp/imp_front.png').convert_alpha()
    imp_front = pygame.transform.scale(imp_front_base, (128, 256))
    imp_pos = [1200, 600]

    running = True
    screen = pygame.display.get_surface()
    background = pygame.Surface((1920, 1080))
    for i in range(1920//32):
        for j in range(1080//32):
            background.blit(debug_tile, (32*i, 32*j))

    bullets = []
    player_pos = [960, 500]

    player_image = cyclop_front
    speed = 4

    # DEBUG Health Bar
    boss_health = 10000
    hp = healthBar("blue", boss_health)
    hp.create(screen, 150, 0)

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                pygame.quit()
                clear_project()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                    pygame.quit()
                    clear_project()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    player_origin = [player_pos[0] + player_image.get_width()//2, player_pos[1] + player_image.get_height()//2]
                    boss_health -= 10
                    bullets.append(Bullet(*player_origin))
                
                if event.button == 3:
                    player_origin = [player_pos[0] + player_image.get_width()//2, player_pos[1] + player_image.get_height()//2]
                    boss_health -= 100
                    myBullet = Bullet(*player_origin)
                    myBullet.changed()
                    bullets.append(myBullet)
        for bullet in bullets[:]:
            bullet.update()
            if not screen.get_rect().collidepoint(bullet.pos):
                bullets.remove(bullet)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_pos[1] -= speed
            player_image = cyclop_back
            
        elif keys[pygame.K_s]:
            player_pos[1] += speed
            player_image = cyclop_front
        
        if keys[pygame.K_a]:
            player_pos[0] -= speed
            player_image = cyclop_left

        elif keys[pygame.K_d]:
            player_pos[0] += speed
            player_image = cyclop_right

        if keys[pygame.K_LSHIFT]:
            speed = 6
        else:
            speed = 3

        # Reset Frame --------------------------------------------- #
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        # Blit Textures
        if boss_health >= 0:
            screen.blit(imp_front, (imp_pos[0], imp_pos[1]))

        screen.blit(player_image, (player_pos[0], player_pos[1]))
        
        for bullet in bullets:
            bullet.draw(screen)

        # Blit UI Elements
        hp.update(boss_health)

        # Update  Frame ------------------------------------------- #
        pygame.display.flip()
        mainClock.tick(60)
