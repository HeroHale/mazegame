import arcade
from constants import TILESIZE

class Tile(arcade.Sprite):
    def __init__(self, x, y, texture="Textures/square.png"):
        super().__init__(texture, scale=(TILESIZE/16))
        self.set_cords(x, y)

    def encode(self):
        return ("tile")

    def set_cords(self, x, y):
        self.center_x = (x * TILESIZE) + (TILESIZE/2)
        self.center_y = (y * TILESIZE) + (TILESIZE/2)
class End_Tile(Tile):
    def __init__(self, x, y):
        super().__init__(x, y, texture="Textures/end_square.png")

    def encode(self):
        return ("end_tile")