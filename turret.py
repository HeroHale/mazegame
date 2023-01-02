import arcade
import math
import time
from player import Player
from constants import TILESIZE

class Bullet(arcade.Sprite):
    cooldown_time = 5
    def __init__(self, center_x, center_y, physics_engine):
        super().__init__("Textures/bullet.png", scale=(TILESIZE/32))
        
        self.center_x = center_x  
        self.center_y = center_y 

        physics_engine.add_sprite(self, 
                                        #friction=0.01,
                                        moment_of_inertia=arcade.PymunkPhysicsEngine.MOMENT_INF,
                                        damping=0.85,
                                        collision_type="bullet",
                                        max_velocity=400)
    
    @classmethod
    def bullet_hits_wall(cls, bullet, _tile, _arbiter, _space, _data):
        bullet.remove_from_sprite_lists()
        print("bullet hit the wall")

class Turret(arcade.Sprite):
    cooldown_time = 5
    def __init__(self, player, bullet_list, physics_engine):
        super().__init__("Textures/gun.png", scale=(TILESIZE/275))
        self.physics_engine = physics_engine
        self.bullet_list = bullet_list
        self.player = player
        #self.center_x = 500
        self.center_x = 350
        self.center_y = 510
        self.cooldown = 0

    def shoot_at_player(self):
        bullet = Bullet(self.center_x,self.center_y, self.physics_engine)
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
        
        


        #get the angle to the player
        #set self.angle to that angle
        


        
        
        #change x by: self.player.center_x
        #change y by: self.player.center_y
        # look_to_player = math.radians(self.angle, self.player)
        #     rot_turret_speed = .5
        #     self.angle += self.change_angle
        #     self.player().center_x += self.rot_turret_speed * math.sin(angle_rad)
        #     self.player().center_y += self.rot_turret_speed * math.cos(angle_rad)
        

            

    
    def gun_cooldown(self):
        Turret.cooldown += Turret.cooldown_time
        for i in range(Turret.cooldown_time):
            Turret.cooldown == 1
            print("Cooldown Time: ", Turret.cooldown_time)
            


        
            

        def fire():
            turret = 10
            turret.fire_at(self.player)


        #get_player_position
        #rotate to player
        #if cooldown = 0
            #shoot player
            #set cooldown to 10
        #cooldown -1
    #def rotate to player
        #do some triginomerty to figure out angle
    #def shoot player
        #make a new bulelt sprite
        #give it volocity towards player 


