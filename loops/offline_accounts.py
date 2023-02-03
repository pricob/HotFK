# Setup Python ----------------------------------------------- #
import pygame, sys
from maintenance import clear_project, load_image, console_push
from classes.button import Button

# Offline accounts ------------------------------------------- #
def offline_account_loop(game_engine):
    
    screen = pygame.display.get_surface()
    mainClock = game_engine.get_mainClock()
    
    background = load_image("resources/background.png")

    accounts_list = {1: None, 2: None, 3: None, 4: None, 5: None}
    
    all_empty = False

    for i in range (1, 6):
        if accounts_list[i] == None:
            if not all_empty:
                accounts_list[i] = Button(550, 100 + i * 120, "resources/new.png", "resources/new_hover.png", 2)
                all_empty = True
            else:
                accounts_list[i] = Button(550, 100 + i * 120, "resources/empty.png", "resources/empty_hover.png", 2)


    # LOOP START
    running = True
    while running:
        # Reset Frame
        screen.fill(0)
        screen.blit(background, (0, 0))

        for i in range(1, 6):
           if accounts_list[i].draw(screen):
            console_push(f"pressed button {i}")

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

        # Update ------------------------------------------------- #
        pygame.display.flip()
        mainClock.tick(60)