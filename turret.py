import arcade
import math
import time
from player import Player
from constants import TILESIZE

class Bullet(arcade.Sprite):
    def __init__(self, angle: float, center_x: int, center_y: int, physics_engine: arcade.PymunkPhysicsEngine):
        super().__init__("Textures/bullet.png", scale=(TILESIZE/32))

        self.center_x = center_x  
        self.center_y = center_y
        self.angle = angle
        self.physics_engine = physics_engine

        physics_engine.add_sprite(self, 
                                        #friction=0.01,
                                        moment_of_inertia=arcade.PymunkPhysicsEngine.MOMENT_INF,
                                        damping=1,
                                        collision_type="bullet",
                                        max_velocity=400)
        velocity = [0.0, 0.0]
        velocity[1] = math.sin(math.radians(self.angle))*-500
        velocity[0] = math.cos(math.radians(self.angle))*-500

        physics_engine.set_velocity(sprite=self, velocity=velocity)
    @classmethod
    def bullet_hits_wall(cls, bullet, tile, _arbiter, _space, _data):
        bullet.kill()
        print("bullet hit the wall")

    @classmethod
    def bullet_hits_player(cls, bullet, player, _arbiter, _space, _data):
        bullet.kill()
        print("Bullet Hit Player")

    def kill(self):
        #self.physics_engine.remove_sprite(self)
        self.remove_from_sprite_lists()
class Turret(arcade.Sprite):
    cooldown_time = 120
    def __init__(self, center_x, center_y, player, bullet_list, physics_engine):
        super().__init__("Textures/gun.png", scale=(TILESIZE/275))
        self.physics_engine = physics_engine
        self.bullet_list = bullet_list
        self.player = player
        #self.center_x = 500
        self.center_x = center_x
        self.center_y = center_y
        self.cooldown = 0

    def shoot_at_player(self):
        bullet = Bullet(self.angle, self.center_x,self.center_y, self.physics_engine)
        self.bullet_list.append(bullet)

    def on_update(self, delta_time):
        self.cooldown += 1
        if self.cooldown == Turret.cooldown_time:
            self.shoot_at_player()
            self.cooldown = 0
        self.update_rotation()
    def update_rotation(self):
        angle = math.atan2(self.center_y - self.player.center_y, self.center_x - self.player.center_x)
        #print(math.degrees(angle))  
        self.angle = math.degrees(angle)
    
    def gun_cooldown(self):
        Turret.cooldown += Turret.cooldown_time
        for i in range(Turret.cooldown_time):
            Turret.cooldown == 1
            print("Cooldown Time: ", Turret.cooldown_time)
            


    def encode(self):
        return ("turret")