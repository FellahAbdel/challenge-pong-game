from turtle import Turtle

class DashLine(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0, -300)
        self.setheading(90)
        self.color("white")
        self.pensize(5)


    def draw_dashed_line(self):
        for _ in range(15):
            self.forward(20)
            self.penup()
            self.forward(20)
            self.pendown()
