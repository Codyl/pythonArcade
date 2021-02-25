import arcade
class Tree:
    def __init__(self, x, y=25, width=80, height=100):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y+self.height/2, 10, self.height, arcade.color.AUBURN)
        arcade.draw_ellipse_filled(self.x, self.y+self.height, self.width, 30, arcade.color.GREEN)