import arcade
from constants import TILESIZE

class Tile(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__("square.png", scale=(TILESIZE/10))
        self.center_x = (x * TILESIZE) + (TILESIZE/2)
        self.center_y = (y * TILESIZE) + (TILESIZE/2)

    def encode(self):
        return ("tile")