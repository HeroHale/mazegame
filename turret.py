import arcade
import math
import time
from player import Player


class Turret(arcade.Sprite):
    cooldown_time = 5
    def __init__(self):
        super().__init__()
        self.cooldown = 0
        
    def shoot_at_player(self):
        pass

    def on_update(self, delta_time):
        self.cooldown += 1
        if self.cooldown == Turret.cooldown_time:
            self.shoot_at_player()
            self.cooldown = 0
        self.update_rotation()
    def update_rotation(self):
        Player().player.x

        print(self.player.x)
        #get the angle to the player
        #set self.angle to that angle
        pass


        
        
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