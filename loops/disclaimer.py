# Setup Python ----------------------------------------------- #
import time
import pygame
import sys

from maintenance import clear_project

def disclaimer_loop(game_engine):

    screen = pygame.display.get_surface()
    progress = 0

    previous_time = time.time()
    
    # LOOP START
    running = True
    while running:
        
        # Background
        screen.fill((0,0,0))
        
        # Time 
        dt = time.time() - previous_time
        previous_time = time.time()

        # Graphics
        pygame.draw.line(screen, (60, 60, 60), (530, 200), (1300, 200), 5)
        pygame.draw.line(screen, (60, 60, 60), (200, 900), (1700, 900), 5)
        pygame.draw.rect(screen, (60, 60, 60), pygame.Rect(0, 1070, 1920, 10))
        pygame.draw.rect(screen, (148, 0, 25), pygame.Rect(0, 1070, 1920//100 * progress, 10))

        progress += 25 * dt
        if progress >= 103:
            break
    
        # Events ------------------------------------------------- #
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                clear_project()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    progress = 103
        
        game_engine.mainClock.tick(60)
        # Update ------------------------------------------------- #
        pygame.display.update()