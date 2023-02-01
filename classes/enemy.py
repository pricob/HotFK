from pygame import image, transform

class Enemy:
    def __init__(self, x, y, type, health):
        self.x = x
        self.y = y
        self.vel = 3
        self.health = int(health)
        self.type = str(type)
        self.alive = True

        if type == "mage" or type == "Mage":
            # Mage sprites
            mage_left_base  = image.load('./resources/monsters/imp/imp_left.png').convert_alpha()
            mage_right_base = image.load('./resources/monsters/imp/imp_right.png').convert_alpha()
            mage_front_base = image.load('./resources/monsters/imp/imp_front.png').convert_alpha()
            mage_back_base  = image.load('./resources/monsters/imp/imp_back.png').convert_alpha()

            self.left  = transform.scale(mage_left_base, (64, 64))
            self.right = transform.scale(mage_right_base, (64, 64))
            self.front = transform.scale(mage_front_base, (64, 64))
            self.back  = transform.scale(mage_back_base, (64, 64))
 
            self.sprite = self.front

            # Cleanup
            del mage_left_base, mage_right_base, mage_front_base, mage_back_base

        if type == "knight" or type == "Knight":
            # Knight sprites
            knight_left_base  = image.load('./resources/monsters/knight/knight_left.png').convert_alpha()
            knight_right_base = image.load('./resources/monsters/knight/knight_right.png').convert_alpha()
            knight_front_base = image.load('./resources/monsters/knight/knight_front.png').convert_alpha()
            knight_back_base  = image.load('./resources/monsters/knight/knight_back.png').convert_alpha()

            self.left  = transform.scale(knight_left_base, (64, 64))
            self.right = transform.scale(knight_right_base, (64, 64))
            self.front = transform.scale(knight_front_base, (64, 64))
            self.back  = transform.scale(knight_back_base, (64, 64))

            self.sprite = self.front

            # Cleanup
            del knight_left_base, knight_right_base, knight_front_base, knight_back_base
    
    def update(self, screen):
        screen.blit(self.sprite, (self.x, self.y))
        

    def move(self):
        # TODO AI That moves in a close range
        pass

    def check_player(self):
        # TODO Check for player proximity for agro
        pass