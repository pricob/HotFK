import pygame
import sys

from pygame.locals import *
from maintenance import clear_project
from health import healthBar

from classes.player import Player
from classes.bullet import Bullet
from classes.enemy import Enemy

# MENU LOOP
def menu_loop(mainClock):
    debug_tile_base = pygame.image.load('./resources/tiles/debug_tile.png').convert_alpha()
    debug_tile = pygame.transform.scale(debug_tile_base, (32, 32))
    
    player = Player(960, 500)

    enemy = Enemy(1200, 600, "Mage", 10000)

    imp_front_base = pygame.image.load('./resources/monsters/imp/imp_front.png').convert_alpha()
    imp_front = pygame.transform.scale(imp_front_base, (128, 256))

    running = True
    screen = pygame.display.get_surface()
    background = pygame.Surface((1920, 1080))
    
    for i in range(1920//32):
        for j in range(1080//32):
            background.blit(debug_tile, (32*i, 32*j))

    bullets = []

    player_image = player.get_oriented()
    boss_health = 1000

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
                    player_origin = [player.x + player_image.get_width()//2, player.y + player_image.get_height()//2]
                    boss_health -= 10
                    bullets.append(Bullet(*player_origin))
                
                if event.button == 3:
                    player_origin = [player.x + player_image.get_width()//2, player.y + player_image.get_height()//2]
                    boss_health -= 100
                    myBullet = Bullet(*player_origin)
                    myBullet.metadata(30, 10, (255, 0, 0), 10)
                    bullets.append(myBullet)
        
        for bullet in bullets[:]:
            bullet.update()
            if not screen.get_rect().collidepoint(bullet.pos):
                bullets.remove(bullet)

        keys = pygame.key.get_pressed()
        player.move(keys)
        
        # Reset Frame --------------------------------------------- #
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        
        # Blit Textures
        if boss_health >= 0:
            enemy.update(screen)

        player.update(screen)
        
        
        for bullet in bullets:
            bullet.draw(screen)

        # Blit UI Elements
        hp.update(boss_health)

        # Update  Frame ------------------------------------------- #
        pygame.display.flip()
        mainClock.tick(60)
