# Setup Python ----------------------------------------------- #
import pygame, sys
from maintenance import clear_project, load_image, console_push, custom_mouse_highlight
from classes.button import Button

# Offline accounts ------------------------------------------- #
def offline_account_loop(game_engine):
    
    cursor_img, cursor_rect = custom_mouse_highlight()

    screen = pygame.display.get_surface()
    mainClock = game_engine.mainClock
    

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

        # Reset Frame -------------------------------------------- #
        screen.fill(0)
        mx, my = pygame.mouse.get_pos()
        cursor_rect.center = (mx, my)

        screen.blit(background, (mx // 50 - 38, my // 50 - 21))

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

        # Render ------------------------------------------------- #
        screen.blit(cursor_img, cursor_rect)

        # Update ------------------------------------------------- #
        pygame.display.flip()
        mainClock.tick(game_engine.fps)