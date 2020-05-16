import arcade
from Screens.Variables import *


class Menu(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):

        super().__init__(width, height, title)

        self.background = None
        self.arrow_pos=0

    def setup(self):
        self.background=[]
        self.background.append( arcade.load_texture(Menu_sprite_1) )
        self.background.append(arcade.load_texture(Menu_sprite_2))
        self.background.append(arcade.load_texture(Menu_sprite_3 ))

    def on_draw(self):
        arcade.start_render()
        # Draw the background texture
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background[self.arrow_pos])

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.W:
            print("Arriba")
            self.arrow_pos -= 1
            if self.arrow_pos < 0:
                self.arrow_pos = 2

        elif key == arcade.key.DOWN or key == arcade.key.S:
            print("Abajo")
            self.arrow_pos += 1
            if self.arrow_pos >= 3:
                self.arrow_pos = 0

        elif key == arcade.key.ENTER:
            print("Seleccion")