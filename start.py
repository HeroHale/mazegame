from sqlite3 import Row
import arcade
import json
from Tile import Tile
from Level import Level
from constants import WIDTH, HEIGHT, TILESIZE

class GameWindow(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, "Maze Game")
        #create empty level
        
        self.level = Level()
        self.mouse_pressed = False

    def on_draw(self):
        self.clear()
        self.level.draw()
    def on_update(self, delta_time):
        pass
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
    def on_key_press(self, key, modifiers):
        if key == arcade.key.S:
            success = self.level.save()

            if success:
                print("Saved level to file.")
        elif key == arcade.key.L:
            success = self.level.load()

            if success:
                print("Loaded level from file.")
            else:
                print("Error loading level")        
            
            
my_window = GameWindow()
arcade.run()
