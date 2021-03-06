import arcade
from random import randint

class Ball:
    def __init__(self, x, y, x_dir, y_dir, speed, width, height):
        self.center_x = randint(x, y)
        self.center_y = randint(x, y)
        self.x_dir = x_dir
        self.y_dir = y_dir
        self.speed = speed
        self.width = width
        self.height = height
        
    def on_draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, 10, arcade.color.GO_GREEN)
        self.center_x += self.x_dir * self.speed
        self.center_y += self.y_dir * self.speed
        if self.center_x < 0 or self.center_x > self.width:
            self.x_dir *= -1
        if self.center_y < 0  or self.center_y > self.height:
            self.y_dir *= -1

           

     
   
        


