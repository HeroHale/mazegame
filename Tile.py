import arcade
from constants import TILESIZE

class Tile(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__("square.png", scale=(TILESIZE/16))
        self.set_cords(x, y)

    def encode(self):
        return ("tile")

    def set_cords(self, x, y):
        self.center_x = (x * TILESIZE) + (TILESIZE/2)
        self.center_y = (y * TILESIZE) + (TILESIZE/2)