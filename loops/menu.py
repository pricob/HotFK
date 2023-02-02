# Setup Python ----------------------------------------------- #
import pygame, sys

from maintenance import load_image, clear_project, console_push

# Menu Loop -------------------------------------------------- #
def menu_loop(game):
    
    screen = pygame.display.get_surface()
    mainClock = game.get_mainClock()

    offline_banner = load_image("resources/offline_banner.png")
    offline_banner_rect = pygame.Rect(450, 270, offline_banner.get_width(), offline_banner.get_height())

    online_banner = load_image("resources/online_banner.png")
    online_banner_rect = pygame.Rect(1070, 270, online_banner.get_width(), online_banner.get_height())

    # LOOP START
    running = True
    while running:
        # Reset Frame
        screen.fill(0)
        
        # Mouse pos
        mx, my = pygame.mouse.get_pos()

        # Events ------------------------------------------------- #
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                clear_project()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()
                    clear_project()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if offline_banner_rect.collidepoint(mx, my):
                        if game.debug_mode:
                            console_push("Clicked offline")
                    if online_banner_rect.collidepoint(mx, my):
                        if game.debug_mode:
                            console_push("Clicked online")

        # Render ------------------------------------------------- #
        screen.blit(offline_banner, offline_banner_rect)
        screen.blit(online_banner, online_banner_rect)

        # Update ------------------------------------------------- #
        pygame.display.flip()
        mainClock.tick(60)
