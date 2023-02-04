# Setup Python ----------------------------------------------- #
from game_engine import gameEngine
from maintenance import clear_project
from pygame import mouse
from loops.disclaimer import disclaimer_loop
from loops.menu import menu_loop

# Init ------------------------------------------------------- #
settings = {
    "fps": 60, 
    "default-width": 1920, 
    "default-height": 1080, 
    "fullscreen": True, 
    "offline": True, 
    "debug-mode": True, 
    'version': "pre-0.0.5a"
}

# Engine Instance -------------------------------------------- #
game_engine = gameEngine(settings)

# Run the game ----------------------------------------------- #
disclaimer_loop(game_engine)
menu_loop(game_engine)

# Clear the project temporary files -------------------------- #
clear_project()