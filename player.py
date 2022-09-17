import arcade
PLAYER_WIDTH = 15
PLAYER_HEIGHT = 15
PLAYER_MOVE_FORCE = 100

class Player():
    def __init__(self, starting_x, starting_y, *args, **kwargs):
        super().__init__(starting_x, starting_y, *args, **kwargs)

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
                            self.width, self.height, arcade.color.PURPLE
                            )
                                    #black box in the middle