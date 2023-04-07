import sys
from sqlite3 import Row
from typing import Counter
import arcade
import time
from arcade import PymunkPhysicsEngine
import json

from pymunk import CollisionHandler
from Tiles.tile import End_Tile, Tile
from Level import Level
from player import Player
from Tiles.turret import Turret, Bullet
from Tiles.bouncing_tile import BouncingTile
from constants import WIDTH, HEIGHT, TILESIZE, PLAYER_FORCE, Key_Pressed, Key_Released

class GameWindow(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, "Maze Game")
        #create empty level
        self.player = Player(242, 201)
        self.bullet = arcade.SpriteList()
        self.moving_tiles = arcade.SpriteList()
        damping = 0.85
        gravity = (0, 0)
        self.physics_engine = PymunkPhysicsEngine(damping=damping,
                                                  gravity=gravity)
                        
    
        self.current_level = 0
        self.W_KEY = Key_Released
        self.S_KEY = Key_Released
        self.A_KEY = Key_Released
        self.D_KEY = Key_Released
        self.mouse_pressed = False
        self.bouncing_tile_key_pressed = Key_Released
        self.make_bouncy_key_pressed = Key_Released
        self.levels = [
            "fourthlevel",
            "startinglevel",
            "secondlevel",
            "thirdlevel"
        ]
         #Set the gravity. (0, 0) is good for outer space and top-down.
        

        # Create the physics engine
        
        def on_load_wraper(first_type, bruh, bruw, bruv, brue):
            self.load_level()
            ## CHANGE THIS FOR LEVEL TESTING
        # self.physics_engine.add_collision_handler(
        #     first_type = "player",
        #     second_type = "tile",
        #     post_handler = on_load_wraper
        #)
        self.physics_engine.add_collision_handler(
            first_type = "bullet",
            second_type = "player",
            post_handler = Bullet.bullet_hits_player

        )
        self.physics_engine.add_collision_handler(
            first_type = "bullet",
            second_type = "tile",
            post_handler = Bullet.bullet_hits_wall
            
            
        )
        self.physics_engine.add_collision_handler(
            first_type = "tile",
            second_type = "moving_tile",
            begin_handler = BouncingTile.moving_tile_hits_tile
            
            
        )
        self.level = Level(self.physics_engine)
        
        
        turret = Turret(350, 510, self.player, self.bullet, self.physics_engine)
        self.level.turrets.append(turret)
        
        
        self.physics_engine.add_sprite(self.player,
                                       #friction=0.01,
                                       moment_of_inertia=PymunkPhysicsEngine.MOMENT_INF,
                                       damping=damping,
                                       collision_type="player",
                                       max_velocity=400)


        self.load_level()
    def load_level(self):
        level_name = self.levels[self.current_level]

        # sets players location
        if level_name == "startinglevel":
            #self.player.center_x = 242
            #self.player.center_y = 201
            self.physics_engine.set_position(self.player, position=[242, 201])

        elif level_name == "secondlevel":
            #self.player.center_x = 181.5
            #self.player.center_y = 217.5
            self.physics_engine.set_position(self.player, position=[181.5, 217.5])
        elif level_name == "thirdlevel":
            #self.player.center_x = 242
            #self.player.center_y = 162.5
            # load the level
            self.physics_engine.set_position(self.player, position=[242, 162.5])
        elif level_name == "fourthlevel":
            #self.player.center_x = 242
            #self.player.center_y = 162.5
            # load the level
            self.physics_engine.set_position(self.player, position=[1709.2, 152.6])
        self.level.load(self.levels[self.current_level])

    def on_draw(self):
        self.clear()
        self.player.draw()
        self.level.draw()
        self.level.turrets.draw()
        self.bullet.draw()
        self.moving_tiles.draw()
    def on_update(self, delta_time):
        for turret in self.level.turrets:
            turret.on_update(delta_time)
        for bouncing_tile in self.moving_tiles:
            bouncing_tile.on_update(delta_time)
        if self.W_KEY == Key_Pressed:
            #self.player.center_y += PLAYER_FORCE
            self.physics_engine.apply_force(self.player, force=[0, PLAYER_FORCE])
        if self.S_KEY == Key_Pressed:
            self.physics_engine.apply_force(self.player, force=[0, -PLAYER_FORCE])
            #self.player.center_y -= PLAYER_FORCE
        if self.A_KEY == Key_Pressed:
            self.physics_engine.apply_force(self.player, force=[-PLAYER_FORCE, 0])
            #self.player.center_x -= PLAYER_FORCE
        if self.D_KEY == Key_Pressed:
            self.physics_engine.apply_force(self.player, force=[PLAYER_FORCE, 0])
            #self.player.center_x += PLAYER_FORCE
        if arcade.check_for_collision_with_list(self.player, self.level.end_tiles):
            self.current_level += 1
            self.load_level()
        self.physics_engine.step()
        

#colliding = arcade.check_for_collision(self.player, self.tile)

    def on_mouse_release(self, mouse_x, mouse_y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.mouse_pressed = False

    def on_mouse_press(self, mouse_x, mouse_y, button, modifiers):
        coord_x = int(mouse_x/TILESIZE)
        coord_y = int(mouse_y/TILESIZE)
        if button == arcade.MOUSE_BUTTON_LEFT:
            if self.bouncing_tile_key_pressed:
                bouncing_tile = BouncingTile(coord_x, coord_y, [0, 10], self.physics_engine)
                self.moving_tiles.append(bouncing_tile)
                print("bouncing tile placed")
            elif self.make_bouncy_key_pressed:
                target_tile = self.level.contents[coord_x][coord_y]
                if target_tile is None:
                    target_tile = self.level.place_tile(coord_x, coord_y, Tile)
                    # TODO: make getter and setter for the "bouncy" field
                target_tile.bouncy = True
                target_tile.texture = arcade.texture.load_texture("Textures/bouncy_tile.png")
            else:    
                self.mouse_pressed = True
                self.level.place_tile(coord_x, coord_y)
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            self.level.place_tile(coord_x, coord_y, End_Tile)
        elif button == arcade.MOUSE_BUTTON_MIDDLE:
            self.level.place_turret(coord_x, coord_y, self.player, self.bullet, self.physics_engine)
            #print(tile.bouncy)
        #if self.bouncing_tile = BouncingTile()

    def on_mouse_motion(self, mouse_x, mouse_y, dx, dy):
        if self.mouse_pressed:
            coord_x = int(mouse_x/TILESIZE)
            coord_y = int(mouse_y/TILESIZE)
            self.level.place_tile(coord_x, coord_y)
    def on_key_release(self, key: int, modifiers: int):
        if key == arcade.key.W:
             self.W_KEY = Key_Released
        elif key == arcade.key.S:
            self.S_KEY = Key_Released
             # move down
        elif key == arcade.key.A:
            self.A_KEY = Key_Released
        elif key == arcade.key.D:
            self.D_KEY = Key_Released
        elif key == arcade.key.N:
            self.bouncing_tile_key_pressed = Key_Released
        elif key == arcade.key.B:
             self.bouncing_tile_key_pressed = Key_Released
            

       
    def on_key_press(self, key, modifiers):
        if key == arcade.key.P:
            self.load_level()
            print("Level Reset")
        elif key == arcade.key.O:
            success = self.level.save()

            if success:
                print("Saved level to file.")

        elif key == arcade.key.B:
            self.make_bouncy_key_pressed = Key_Pressed

        elif key == arcade.key.C:
            self.level.clear()
            print("Cleared file.")
        elif key == arcade.key.L:
            #reloads the level
            success = self.load_level()

            if success:
                print("Loaded level from file.")
            else:
                print("Error loading level")

        elif key == arcade.key.N:
            self.bouncing_tile_key_pressed = Key_Pressed            

        elif key == arcade.key.W:
            self.W_KEY = Key_Pressed
            print(f"X: {self.player.center_x}\nY: {self.player.center_y}")
        elif key == arcade.key.S:
            self.S_KEY = Key_Pressed
            print(f"X: {self.player.center_x}\nY: {self.player.center_y}")
            # move down
        elif key == arcade.key.A:
            self.A_KEY = Key_Pressed
            print(f"X: {self.player.center_x}\nY: {self.player.center_y}")
        elif key == arcade.key.D:
            self.D_KEY = Key_Pressed
            print(f"X: {self.player.center_x}\nY: {self.player.center_y}")


        # elif key == arcade.key.UP:
        #     self.player.center_y += PLAYER_FORCE
        # elif key == arcade.key.DOWN:
        #     self.player.center_y -= PLAYER_FORCE
        #     # move down
        # elif key == arcade.key.LEFT:
        #     self.player.center_x -= PLAYER_FORCE
        # elif key == arcade.key.RIGHT:
        #     self.player.center_x += PLAYER_FORCE


    # LOOK IN PLAYER - this is in there and I am not sure if it should be here or in player so confirm that
    """
    def get_move_force(self, keys, dtime):
        forcex = 0
        forcey = 0
        if keys[arcade.key.W]:
            forcex += 0
            forcey += PLAYER_MOVE_FORCE * dtime 
        if keys[arcade.key.S]:
            forcex += 0
            forcey += -PLAYER_MOVE_FORCE * dtime

        if keys[arcade.key.D]:
            forcex = PLAYER_MOVE_FORCE * dtime
            forcey = 0
        if keys[arcade.key.A]:
            forcex = -PLAYER_MOVE_FORCE * dtime
            forcey = 0

        return (forcex, forcey)
    """
    
                        
args = sys.argv
# [ "python", "./start.py", "startinglevel"]
# [ "python", "./start.py"]

def process_inputs(window):
    if len(sys.argv) == 1:
        return
    if len(sys.argv) == 2:
        window.level.load(sys.argv[1])

my_window = GameWindow()
process_inputs(my_window)
arcade.run()
