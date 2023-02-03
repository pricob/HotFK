# Setup Python ----------------------------------------------- #
import pygame
import sys

from maintenance import clear_project

def disclaimer_loop(game_engine):

    screen = pygame.display.get_surface()
    mainClock = game_engine.get_mainClock()
    progress = 0

    # LOOP START
    running = True
    while running:
        
        # Background
        screen.fill((0,0,0))

        pygame.draw.line(screen, (60, 60, 60), (530, 200), (1300, 200), 5)
        pygame.draw.line(screen, (60, 60, 60), (200, 900), (1700, 900), 5)

        # loading bar
        progress += 0.5
        pygame.draw.rect(screen, (60, 60, 60), pygame.Rect(0, 1070, 1920, 10))
        pygame.draw.rect(screen, (148, 0, 25), pygame.Rect(0, 1070, 1920//100 * progress, 10))

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
                    
        # Update ------------------------------------------------- #
        pygame.display.update()
        mainClock.tick(60)