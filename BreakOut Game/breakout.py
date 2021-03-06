import arcade
from paddle import Paddle
from ball import Ball
from targets import Target
from random import choice

class Pong(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.paddle = Paddle(250, 10)
        self.ball = Ball(10, 300, 4, -4, 1, self.width, self.height)

        #track user score
        self.score = 0
        
        
        # create targets at 5 levels
        self.targets = []
    def start_game(self):
        space = 0
        while len(self.targets) < 85:
            target1 = Target(10 + space, 300, arcade.color.SKY_BLUE)
            target2 = Target(10 + space, 320, arcade.color.ARMY_GREEN)
            target3 = Target(10 + space, 340, arcade.color.YELLOW_ORANGE)
            target4 = Target(10 + space, 360, arcade.color.AFRICAN_VIOLET)
            target5 = Target(10 + space, 380, arcade.color.TOMATO)
            self.targets.append(target1)
            self.targets.append(target2)
            self.targets.append(target3)
            self.targets.append(target4)
            self.targets.append(target5)
            space += 30
    

    # collision btn paddle and ball
    def collide(self, paddle, ball):
        if (paddle.center_x - 40 < ball.center_x < paddle.center_x + 40) and (paddle.center_y + 10  > ball.center_y > paddle.center_y - 10 ):
            ball.x_dir *= -1
            ball.y_dir *= -1

    # collision btn target and ball
    def ball_target_collision(self, target, ball):
        if (target.center_x - 15 < ball.center_x +10 and ball.center_x < target.center_x + 15) and (target.center_y + 10  > ball.center_y and ball.center_y > target.center_y - 10 ):
            if target.center_y == 300:
                self.score += 1 
            elif target.center_y == 320:
                self.score += 2
            elif target.center_y == 340:
                self.score += 3 
            elif target.center_y == 360:
                self.score += 4 
            elif target.center_y == 380:
                self.score += 5
            self.targets.remove(target)
            ball.x_dir *= choice([-1, -1.05])
            ball.y_dir *= choice([-1, -1.05])
            
            #increase speed if speed is below max speed
            if ball.speed < 5:
                ball.speed += 0.05
            
            
    # draw on arcade window
    def on_draw(self):
        self.clear()
        # display paddle
        self.paddle.on_draw()
        # display targets
        for target in self.targets:
            target.on_draw()
        #dispaly ball
        self.ball.on_draw()
        self.collide(self.paddle, self.ball)
        
        #target and ball collision
        if len(self.targets) > 0:
            for t in range(len(self.targets) -1, -1, -1):
                self.ball_target_collision(self.targets[t], self.ball)
                if len(self.targets) == 0:
                    break

        # display score
        arcade.draw_text("Your score is:" + " " + str(self.score), 200, 450)

        # reset game
        if self.ball.center_y < 0 or len(self.targets) == 0:
            self.score = 0
            self.targets = []
            self.start_game()
            self.ball.x_dir = 4
            self.ball.y_dir = -4
            self.ball.center_y = 250
            self.ball.speed = 1
            
            
    # move paddle by key press
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.LEFT:
            self.paddle.center_x -= 50
        elif symbol == arcade.key.RIGHT:
            self.paddle.center_x += 50


arcade.window = Pong(500, 500, "Erick' Breakout Game")
arcade.window.start_game()
arcade.run()

