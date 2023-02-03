from pygame import mouse
from maintenance import load_image

class Button:
    def __init__(self, x, y, button_image, button_hover_image, hover_offset):
        self.x = x
        self.y = y
        
        self.image = load_image(button_image)
        self.hover = load_image(button_hover_image)
    
        self.active = self.image
        self.hover_offset = hover_offset

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.clicked = False

    def draw(self, screen):
        action = False
        # get mouse position
        pos = mouse.get_pos()

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            self.active = self.hover
            self.rect.topleft = (self.x, self.y - self.hover_offset)
            if mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        else:
            self.active = self.image
            self.rect.topleft = (self.x, self.y)

        if mouse.get_pressed()[0] == 0:
            self.clicked = False

        screen.blit(self.active, (self.rect.x, self.rect.y))
        return action