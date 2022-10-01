import sys
from sqlite3 import Row
import arcade
import json
from Tile import Tile
from Level import Level
from player import Player
from constants import WIDTH, HEIGHT, TILESIZE, PLAYER_VELOCITY, Key_Pressed, Key_Released, RED

class GameWindow(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, "Maze Game")
        #create empty level

        self.W_KEY = Key_Released
        self.S_KEY = Key_Released
        self.A_KEY = Key_Released
        self.D_KEY = Key_Released
        
        self.level = Level()# w,   h
        self.player = Player(242, 135)
        self.mouse_pressed = False
        self.levels = [
            "startinglevel",
            "mazelevel"
        ]
        

    def on_draw(self):
        arcade.draw_rectangle_filled(242, 135, 100, 100, arcade.csscolor.YELLOW)
        self.clear()
        self.player.draw()
        self.level.draw()
    def on_update(self, delta_time):
        if self.W_KEY == Key_Pressed:
            self.player.center_y += PLAYER_VELOCITY
        if self.S_KEY == Key_Pressed:
            self.player.center_y -= PLAYER_VELOCITY
        if self.A_KEY == Key_Pressed:
            self.player.center_x -= PLAYER_VELOCITY
        if self.D_KEY == Key_Pressed:
            self.player.center_x += PLAYER_VELOCITY

    def on_mouse_release(self, mouse_x, mouse_y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.mouse_pressed = False

    def on_mouse_press(self, mouse_x, mouse_y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.mouse_pressed = True
            coord_x = int(mouse_x/TILESIZE)
            coord_y = int(mouse_y/TILESIZE)
            self.level.place_tile(coord_x, coord_y)
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
            

       
    def on_key_press(self, key, modifiers):
        
        if key == arcade.key.O:
            success = self.level.save()

            if success:
                print("Saved level to file.")
        elif key == arcade.key.L:
            success = self.level.load()

            if success:
                print("Loaded level from file.")
            else:
                print("Error loading level")            

        elif key == arcade.key.W:
            self.W_KEY = Key_Pressed
        elif key == arcade.key.S:
            self.S_KEY = Key_Pressed
            # move down
        elif key == arcade.key.A:
            self.A_KEY = Key_Pressed
        elif key == arcade.key.D:
            self.D_KEY = Key_Pressed


        # elif key == arcade.key.UP:
        #     self.player.center_y += PLAYER_VELOCITY
        # elif key == arcade.key.DOWN:
        #     self.player.center_y -= PLAYER_VELOCITY
        #     # move down
        # elif key == arcade.key.LEFT:
        #     self.player.center_x -= PLAYER_VELOCITY
        # elif key == arcade.key.RIGHT:
        #     self.player.center_x += PLAYER_VELOCITY


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
[ "python", "./start.py", "startinglevel"]
[ "python", "./start.py"]

def process_inputs(window):
    if len(sys.argv) == 1:
        return
    if len(sys.argv) == 2:
        window.level.load(sys.argv[1])

my_window = GameWindow()
process_inputs(my_window)
arcade.run()
