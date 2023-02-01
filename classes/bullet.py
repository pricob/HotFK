from pygame import mouse, Surface, transform
from math import atan2, hypot, degrees

class Bullet:
    def __init__(self, x, y):
        self.pos = (x, y)
        mx, my = mouse.get_pos()
        self.dir = (mx - x, my - y)
        length = hypot(*self.dir)
        if length == 0.0:
            self.dir = (0, -1)
        else:
            self.dir = (self.dir[0]/length, self.dir[1]/length)
        angle = degrees(atan2(-self.dir[1], self.dir[0]))

        self.bullet = Surface((14, 4)).convert_alpha()
        self.bullet.fill((255, 255, 255))
        self.bullet = transform.rotate(self.bullet, angle)
        self.speed = 30

    def metadata(self, width, length, color, speed):
        self.bullet = Surface((width, length)).convert_alpha()
        angle = degrees(atan2(-self.dir[1], self.dir[0]))
        self.bullet.fill(color)
        self.bullet = transform.rotate(self.bullet, angle)
        self.speed = speed

    def update(self):
        self.pos = (self.pos[0]+self.dir[0]*self.speed, 
                    self.pos[1]+self.dir[1]*self.speed)

    def draw(self, surf):
        bullet_rect = self.bullet.get_rect(center = self.pos)
        surf.blit(self.bullet, bullet_rect)

    def get_rect(self):
        return self.bullet.get_rect(center = self.pos)