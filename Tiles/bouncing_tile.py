import arcade
from arcade import PymunkPhysicsEngine
from pymunk import ShapeFilter
from Tiles.tile import Tile

class BouncingTile(Tile):
    def __init__(self, x, y, initial_velocity: list, physics_engine: arcade.PymunkPhysicsEngine):
        super().__init__(x, y, texture="Textures/moving_square.png")
        self.velocity_x = initial_velocity[0]
        self.velocity_y = initial_velocity[1]
        self.physics_engine = physics_engine
        #pymunk.ShapeFilter(group: int = 0, categories: int = 4294967295, mask: int = 4294967295)
        physics_engine.add_sprite(self,
                                        moment_of_inertia=PymunkPhysicsEngine.MOMENT_INF,
                                        collision_type="moving_tile",
                                        max_velocity=400)

    def on_update(self, delta_time):
        self.physics_engine.apply_impulse(self, [self.velocity_x, self.velocity_y])
    def hit_bouncy_tile(self):
        self.velocity_x *= -1
        self.velocity_y *= -1
    @classmethod
    def moving_tile_hits_tile(cls, tile, bouncing_tile, arbiter, space, data):
        if tile.bouncy:
            delta_x = abs(tile.center_x - bouncing_tile.center_x)
            delta_y = abs(tile.center_y - bouncing_tile.center_y)

            if delta_x > delta_y:
                bouncing_tile.velocity_y *= -1
            else:
                bouncing_tile.velocity_x *= -1
        return False