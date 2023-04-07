import json
import arcade
from arcade import PymunkPhysicsEngine
from Tiles.tile import Tile, End_Tile
from constants import TILESIZE, HEIGHT, WIDTH
from Tiles.turret import Turret


class LevelEncoder(json.JSONEncoder):

    def default(self, object):
        if isinstance(object, Tile) or (object == "None"):
            return Tile.encode_tile_or_none(object)
        elif isinstance(object, Turret):
            return object.encode()
        return super().default(self, object)

def level_decoder(dct):
    #base case
    if isinstance(dct, dict):
        if "tile" in dct:
            # this is a tile, return that
            decoded_tile = None
            if dct["tile"] == "end_tile":
                decoded_tile = End_Tile(0, 0)
            elif dct["tile"] == "None":
                return None
            else:
                decoded_tile = Tile(0, 0)
            
            decoded_tile.bouncy = dct["bouncy"]
            return decoded_tile
        # decode all the items in this dictionary (if its not a tile)
        decoded_dict = {}
        for key, value in dct.items():
            decoded_dict[key] = level_decoder(value)
        return decoded_dict
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
    def __init__(self, physics : arcade.PymunkPhysicsEngine):
        self.tiles = arcade.SpriteList()
        self.end_tiles = arcade.SpriteList()
        self.turrets = arcade.SpriteList()
        self.physics = physics
        self.clear()
    def save(self):
        #try:
        
        for row_number, row in enumerate(self.contents):
            for colum_number, tile in enumerate(row):
                if tile is None:
                    self.contents[row_number][colum_number] = {
                "tile" : "None",
                "bouncy": False
            }


        with open("level.json", "w") as f:
            json.dump(self.contents, f, cls=LevelEncoder)

            for row_number, row in enumerate(self.contents):
                for colum_number, tile in enumerate(row):
                    if isinstance(tile, dict):
                        if tile["tile"] == "None":
                            self.contents[row_number][colum_number] = None
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
            self.physics.add_sprite_list(self.tiles,
                                            #friction=0,
                                            collision_type="tile",
                                            body_type=PymunkPhysicsEngine.STATIC)
            self.physics.add_sprite_list(self.end_tiles,
                                            #friction=0,
                                            collision_type="end_tile",
                                            body_type=PymunkPhysicsEngine.STATIC)
        return True
        #except:
            #return False

    def clear(self):
        self.contents = []
        
        for i in range(int(WIDTH/TILESIZE)):
            col = []
            for j in range(int(HEIGHT/TILESIZE)):
                # fill with empty tiles
                col.append(None)
            self.contents.append(col)
        self.sync_tiles()
    def sync_tiles(self):
        current_tile = 0
        current_end_tile = 0
        for tile in self.tiles:
            self.physics.remove_sprite(self.tiles[current_tile])
            current_tile += 1
        for end_tile in self.end_tiles:
            self.physics.remove_sprite(self.end_tiles[current_end_tile])
            current_end_tile += 1
        self.tiles.clear()
        self.end_tiles.clear()
        for row_index, row in enumerate(self.contents):
            for col_index, tile in enumerate(row):
                if tile is None:
                    continue
                elif isinstance(tile, str):
                    raise Exception("that is not a tile")
                elif isinstance(tile, End_Tile):
                    self.end_tiles.append(tile) # add the new tile to the arcade list
                elif isinstance(tile, Tile):
                    self.tiles.append(tile) # add the new tile to the arcade list
                else:
                    raise Exception("what? how?")

                tile.set_cords(row_index, col_index)
                

    def place_tile(self, coord_x, coord_y, tile_class=Tile):
        try:
            if self.contents[coord_x][coord_y] is not None:
                return

            new_tile = tile_class(coord_x, coord_y)
            self.contents[coord_x][coord_y] = new_tile
            self.tiles.append(new_tile)


            if tile_class == End_Tile:
                self.end_tiles.append(new_tile)
                self.physics.add_sprite(new_tile,
                                            #friction=0,
                                            collision_type="end_tile",
                                            body_type=PymunkPhysicsEngine.STATIC)
            elif tile_class == Tile:
                self.physics.add_sprite(new_tile,
                                            #friction=0,
                                            collision_type="tile",
                                            body_type=PymunkPhysicsEngine.STATIC)
            return new_tile

        except IndexError:
            return

    def place_turret(self, coord_x, coord_y, player, bullet_list, physics_engine):
        
        try:
            # if self.contents[coord_x][coord_y] is not None:
            #     return

            new_turret = Turret(coord_x*TILESIZE, coord_y*TILESIZE, player, bullet_list, physics_engine)
            self.contents[coord_x][coord_y] = new_turret
            self.turrets.append(new_turret)
        except IndexError:
            return


    def draw(self):
        self.tiles.draw()
        self.end_tiles.draw()