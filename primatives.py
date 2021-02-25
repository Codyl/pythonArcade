import arcade
import random

class Game(arcade.Window):
    def __init__(self):
        super().__init__(800,600,"Test")
        arcade.set_background_color(arcade.color.DARK_CERULEAN)
    def on_draw(self):
        arcade.start_render()
        texture = arcade.load_texture("./tile1.png")
        for tile in range(30):
            arcade.draw_scaled_texture_rectangle(10+(30*tile), 10, texture, 0.5, 0)
        arcade.draw_circle_filled(400,300, 90, arcade.color.YELLOW_ORANGE)
        # Draw a tree
        for tree in range(4):
            arcade.draw_rectangle_filled(100+(100*tree), 65, 20, 80, arcade.color.AUBURN)
            arcade.draw_ellipse_filled(100+(100*tree), 100, 80, 30, arcade.color.GREEN)
        # Draw the character
        texture = arcade.load_texture("./character.png")
        arcade.draw_scaled_texture_rectangle(450, 50, texture, 0.5, 0)

def main():
    window = Game()
    arcade.run()
main()