import arcade
from constants import TILESIZE

class Tile(arcade.Sprite):
    def __init__(self, x, y, texture="Textures/square.png"):
        super().__init__(texture, scale=(TILESIZE/16))
        self.set_cords(x, y)
        self.bouncy = False

    def encode(self):
        return ("tile")

    def set_cords(self, x, y):
        self.center_x = (x * TILESIZE) + (TILESIZE/2)
        self.center_y = (y * TILESIZE) + (TILESIZE/2)

    @classmethod
    def encode_tile_or_none(cls, object):
        encoded = "None"
        bouncy = False

        if isinstance(object, cls):
            encoded = object.encode()
            bouncy = False
            
            return {
                "tile" : encoded,
                "bouncy": bouncy
            }

class End_Tile(Tile):
    def __init__(self, x, y):
        super().__init__(x, y, texture="Textures/end_square.png")

    def encode(self):
        return ("end_tile")

# class MovingTile(Tile):
#     def on_update(self, delta_time):
#         super().on_update(delta_time)

#         moving_up = True
#         moving_right = True

#     if y > number
#         moving_up = True
#     else y < number
#         moving_up = False




# function init() {
#   create_variable moving_up = true
# }

# function on_update() {
#   # SECTION 1---------------------------------------------------------------------
#   if (platform.y - (platform.height/2) < 0) and (!moving_up) {
#     moving_up = true
#   } else if (platform.y + (platform.height/2) > SCREEN_HEIGHT) and (moving_up) {
#     moving_up = false
#   }
  
#   # SECTION 2---------------------------------------------------------------------
#   if moving_up {
#     physics_engine.apply_impulse([0, 1])
#   } else {
#     physics_engine.apply_impulse([0, -1])
#   }
# }