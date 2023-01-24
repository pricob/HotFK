# Setup Python ----------------------------------------------- #
from engine import gameEngine, fontEngine
from menu import menu_loop
from options import options_loop

from maintenance import build, clear_project

# Init ------------------------------------------------------- #
settings = {"fps": 60, "default-width": 1920, "default-height": 1080, "fullscreen": False, "offline": True, "DEBUG": True}
available_res = [(384, 216), (768, 432), (1154, 648), (1536, 684), (1920, 1080)]

# Engine instance
game = gameEngine()

game.config(settings, available_res)
# game.update_resolution(available_res[4])

font_sml = fontEngine('./fonts/small_font_alpha.png')
font_big = fontEngine('./fonts/large_font_alpha.png')

# FIRST ENTRY
# Run the game
game.run(font_sml, font_big)
mainClock = game.get_clock()

# DEBUG ? TESTING
menu_loop(mainClock)



# Clean the project's temporary files
clear_project()