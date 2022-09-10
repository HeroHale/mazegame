import arcade
from Objects.gameobject import GameObject
from constants import PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_MOVE_FORCE

class Player(GameObject):
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
        arcade.draw_rectangle_filled(
                                    self.center_x,
                                    self.center_y,
                                    self.width-50, self.height-50, arcade.color.BLACK
                                    )
                                    #left eye
        arcade.draw_rectangle_filled(
                                    self.center_x-50,
                                    self.center_y+50,
                                    self.width-275, self.height-275, arcade.color.PURPLE
                                    )
                                    #right eye
        arcade.draw_rectangle_filled(
                                    self.center_x+50,
                                    self.center_y+50,
                                    self.width-275, self.height-275, arcade.color.PURPLE
                                    )
                                    #start of smile - line
        arcade.draw_rectangle_filled(
                                    self.center_x,
                                    self.center_y-50,
                                    self.width-125, self.height-275, arcade.color.PURPLE
                                    )
                                    #start of smile - right smile
        arcade.draw_rectangle_filled(
                                    self.center_x-75,
                                    self.center_y-25,
                                    self.width-275, self.height-275, arcade.color.PURPLE
                                    )
                                    #start of smile - left smile
        arcade.draw_rectangle_filled(
                                    self.center_x+75,
                                    self.center_y-25,
                                    self.width-275, self.height-275, arcade.color.PURPLE
                                    )