import arcade
from Tiles.tile import Tile

class BouncingTile(Tile):
    def __init__(self, x, y, initial_velocity: list, physics_engine: arcade.PymunkPhysicsEngine):
        super().__init__(x, y, texture="Textures/bullet.png")
        self.velocity_x = initial_velocity[0]
        self.velocity_y = initial_velocity[1]
        self.physics_engine = physics_engine
        physics_engine.add_sprite(self)

    def on_update(self, delta_time):
        self.physics_engine.apply_impulse(self, [self.velocity_x, self.velocity_y])

    def hit_bouncy_tile(self):
        self.velocity_x *= -1
        self.velocity_y *= -1
