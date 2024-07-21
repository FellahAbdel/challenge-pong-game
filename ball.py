from turtle import Turtle

MOVE_DISTANCE = 15

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1



    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """When y_cord is increasing, we decrease when the ball hits top wall, and we do the reverse as well when it
        hits the bottom wall"""
        self.y_move *= -1



    def increase_ball_speed(self):
        self.move_speed *= 0.9

    def bounce_x(self):
        self.x_move *= -1

    def reset_ball(self):
        self.home()
        self.bounce_x()
        self.move_speed = 0.1