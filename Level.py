import json
import arcade
from Tile import Tile
from constants import TILESIZE, HEIGHT, WIDTH


class LevelEncoder(json.JSONEncoder):

    def default(self, object):
        if isinstance(object, Tile):
            return object.encode()
        return json.JSONEncoder.default(self, object)

def level_decoder(dct):
    #base case
    if dct == "tile":
        return Tile(0, 0)
    elif isinstance(dct, list):
        #recursive case
        #collect any items in list that might be the base case 
        empty_list = []
        for item in dct:
            decoded_item = level_decoder(item)
            empty_list.append(decoded_item)
            #empty list now contains the decoded version of everything in dct
        return empty_list
    else:
        #this will only happen if dct is None
        return None
class Level():
    def __init__(self):
        self.contents = []
        self.tiles = arcade.SpriteList()
        #create empty colums
        for i in range(int(WIDTH/TILESIZE)):
            col = []
            for j in range(int(HEIGHT/TILESIZE)):
                # fill with empty tiles
                col.append(None)
            self.contents.append(col)

    def save(self):
        #try:
        with open("level.json", "w") as f:
            json.dump(self.contents, f, cls=LevelEncoder)
        return True
        #except:
            #return False

    def load(self, levelname: str):
        #try:
        if levelname == None:
            levelname = "level.json"
        else:
            levelname = f"Levels/{levelname}.json"
        with open(levelname, "r") as f:
            self.contents = level_decoder(json.load(f))
            
            self.sync_tiles() # fix tiles that get instantiated at 0,0
        return True
        #except:
            #return False

    def sync_tiles(self):
        self.tiles = arcade.SpriteList()
        for row_index, row in enumerate(self.contents):
            for col_index, tile in enumerate(row):
                if tile is None:
                    continue
                elif isinstance(tile, str):
                    raise Exception("that is not a tile")
                elif isinstance(tile, Tile):
                    pass
                else:
                    raise Exception("what? how?")

                tile.set_cords(row_index, col_index)
                self.tiles.append(tile) # add the new tile to the arcade list

    def place_tile(self, coord_x, coord_y):
        try:
            if self.contents[coord_x][coord_y] is not None:
                return

            new_tile = Tile(coord_x, coord_y)
            self.contents[coord_x][coord_y] = new_tile

            self.tiles.append(new_tile)
        except IndexError:
            return


    def draw(self):
        self.tiles.draw()