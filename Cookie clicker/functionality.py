from pygame import *
from time import sleep


class Cookie():
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self, surface):
        draw.circle(surface, self.color, (self.x, self.y), self.radius)

    def is_pressed(self, pos):
        mx, my = pos
        if (mx - self.x) ** 2 + (my - self.y) ** 2 <= self.radius ** 2:
            print("Cookie clicked!")
            
    