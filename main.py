from turtle import Turtle, Screen
from paddle import Paddle
import time
from ball import Ball
from scoreboard import ScoreBoard
from dashine import DashLine

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

l_paddle = Paddle(-350, 0)
r_paddle = Paddle(350, 0)
ball = Ball()

dash_line = DashLine()
dash_line.draw_dashed_line()




scoreboard = ScoreBoard()


screen.listen()
screen.onkey(key="Up", fun=r_paddle.move_up)
screen.onkey(key="Down", fun=r_paddle.move_down)
screen.onkey(key="w", fun=l_paddle.move_up)
screen.onkey(key="s", fun=l_paddle.move_down)



ball.setheading(37)
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()


    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280 :
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 335 or ball.distance(l_paddle) < 50 and ball.xcor() < -335:
        ball.bounce_x()
        ball.increase_ball_speed()

    # Detect R paddle missed the ball
    if ball.xcor() > 390:
        ball.reset_ball()
        scoreboard.l_point()

     # Detect if L paddle missed the ball
    if ball.xcor() < -390:
        ball.reset_ball()
        scoreboard.r_point()

        # ball goes out of bounds



screen.exitonclick()







