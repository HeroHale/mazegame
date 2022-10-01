import arcade
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
PLAYER_MOVE_FORCE = 100

class Player(arcade.Sprite):
    def __init__(self, starting_x, starting_y, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.center_x = starting_x
        self.center_y = starting_y

        self.width = PLAYER_WIDTH
        self.height = PLAYER_HEIGHT

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


    def draw(self):
        #first purple box/outline
        arcade.draw_rectangle_filled(
                            self.center_x,
                            self.center_y,
                            self.width, self.height, arcade.color.RED_DEVIL
                            )
                                    #black box in the middle