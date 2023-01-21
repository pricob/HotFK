# Setup Python ----------------------------------------------- #
import pygame
import sys

from pygame.locals import *
from maintenance import clear_project
# Funcs ------------------------------------------------------ #
def clip(surf, x, y, x_size, y_size):
    handle_surf = surf.copy()
    clipR = pygame.Rect(x, y, x_size, y_size)
    handle_surf.set_clip(clipR)
    image = surf.subsurface(handle_surf.get_clip())
    return image.copy()

def fill(surface, color):
    """Fill all pixels of the surface with color, preserve transparency."""
    w, h = surface.get_size()
    r, g, b = color
    for x in range(w):
        for y in range(h):
            a = surface.get_at((x, y))[3]
            surface.set_at((x, y), pygame.Color(r, g, b, a))

# Classes ---------------------------------------------------- #
class fontEngine():
    def __init__(self, path):
        self.spacing = 1
        self.character_order = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
        'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
        '.','-',',',':','+','\'','!','?','0','1','2','3','4','5','6','7','8','9','(',')','/','_','=','\\','[',']','*','"','<','>',';']
        font_img = pygame.image.load(path).convert_alpha()
        current_char_width = 0
        self.characters = {}
        character_count = 0
        for x in range(font_img.get_width()):
            c = font_img.get_at((x, 0))
            if c[0] == 127:
                char_img = clip(font_img, x - current_char_width, 0, current_char_width, font_img.get_height())
                self.characters[self.character_order[character_count]] = char_img.copy()
                character_count += 1
                current_char_width = 0
            else:
                current_char_width += 1
        self.space_width = self.characters['A'].get_width()

    def render(self, surf, text, color, scale_x, scale_y, spacing, loc):
        x_offset = 0
        for char in text:
            if char != ' ':
                fill(self.characters[char], color)
                if char == '.':
                    self.scaled = pygame.transform.scale(self.characters[char], (scale_x//2, scale_y))
                elif char == '!':
                    self.scaled = pygame.transform.scale(self.characters[char], (scale_x//2, scale_y))
                else:
                    self.scaled = pygame.transform.scale(self.characters[char], (scale_x, scale_y))

                surf.blit(self.scaled, (loc[0] + x_offset, loc[1]))
                if spacing == 'default':
                    x_offset += self.scaled.get_width() + self.spacing
                else:
                    x_offset += spacing + spacing
            else:
                if spacing != 'default':
                    x_offset += self.space_width + self.spacing + spacing + spacing
                

class gameEngine:
    def __init__(self):
        self.mainClock = pygame.time.Clock()
        pygame.init()
        self.screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)

    def get_clock(self):
        return self.mainClock

    def run(self, font_sml, font_big):
        # Loop ------------------------------------------------------- #
        running = True
        progress = 0
        color = (9, 112, 186)
        while running:
            
            # Background --------------------------------------------- #
            self.screen.fill((0,0,0))

            font_big.render(self.screen, 'DISCLAIMER!', (148, 0, 25), 60, 100, 40, (500, 100))
            font_big.render(self.screen, 'The following project is a prototype.', color, 30, 80, 20, (200, 320))
            font_big.render(self.screen, 'Everything presented in this game is', color, 30, 80, 20, (200, 410))
            font_big.render(self.screen, 'subject to change.', color, 30, 80, 20, (200, 500))
            
            font_big.render(self.screen, 'Please take note that your progress', color, 30, 80, 20, (200, 650))
            font_big.render(self.screen, 'will be', color, 30, 80, 20, (200, 740))
            font_big.render(self.screen, 'lost', (148, 0, 25), 30, 80, 20, (540, 740))
            font_big.render(self.screen, 'at the official release.', color, 30, 80, 20, (750, 740))
            
            pygame.draw.line(self.screen, (60, 60, 60), (530, 200), (1300, 200), 5)
            pygame.draw.line(self.screen, (60, 60, 60), (200, 900), (1700, 900), 5)

            # loading bar
            progress += 0.5
            pygame.draw.rect(self.screen, (60, 60, 60), pygame.Rect(0, 1070, 1920, 10))
            pygame.draw.rect(self.screen, (148, 0, 25), pygame.Rect(0, 1070, 1920//100 * progress, 10))

            if progress == 103:
                break

            # Buttons ------------------------------------------------ #
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
                        
            # Update ------------------------------------------------- #
            pygame.display.update()
            self.mainClock.tick(60)

    def config(self, settings, available_res):
        self.settings = settings
        self.available_res = available_res
    
    def reset_settings(self):
        self.settings = {"fps": 60, "default-width": 384, "default-height": 216, "fullscreen": False, "offline": True, "DEBUG": True}
    
    def update_resolution(self, tuple):
        self.settings["default-width"] = tuple[0]
        self.settings["default-height"] = tuple[1]
        self.screen = pygame.display.set_mode((self.settings["default-width"], self.settings["default-height"]), pygame.FULLSCREEN)