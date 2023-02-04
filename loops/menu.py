# Setup Python ----------------------------------------------- #
import pygame, sys
import webbrowser

from maintenance import clear_project, console_push, load_image, custom_mouse_highlight
from classes.button import Button
from loops.offline_accounts import offline_account_loop

# Menu Loop -------------------------------------------------- #
def menu_loop(game_engine):

    cursor_img, cursor_rect = custom_mouse_highlight()

    screen = pygame.display.get_surface()
    mainClock = game_engine.mainClock

    offline_banner = Button(450, 270, "resources/offline_banner.png", "resources/offline_banner_hover.png", 5)
    online_banner = Button(1070, 270, "resources/online_banner.png", "resources/online_banner_hover.png", 5)

    discord = Button(400, 900, "resources/discord.png", "resources/discord_hover.png", 0)
    github = Button(260, 900, "resources/github.png","resources/github_hover.png", 0)

    background = load_image("resources/background.png")
    
    # LOOP START
    running = True
    while running:

        mx, my = pygame.mouse.get_pos()
        cursor_rect.center = (mx, my)

        # Reset Frame
        screen.fill(0)
        screen.blit(background, (mx // 50 - 38, my // 50 - 21))
        # Draw buttons
        if offline_banner.draw(screen):
            if game_engine.debug_mode:
                console_push("Offline clicked")
                offline_account_loop(game_engine)

        if online_banner.draw(screen):
            if game_engine.debug_mode:
                console_push("Online clicked")

        if discord.draw(screen):
            webbrowser.open("https://discord.gg/J5wDbVjDWc")

        if github.draw(screen):
            webbrowser.open("https://github.com/pricob/HotFK")
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
        # Render ------------------------------------------------- #
        screen.blit(cursor_img, cursor_rect)
        # Update ------------------------------------------------- #
        pygame.display.flip()
        mainClock.tick(game_engine.fps)