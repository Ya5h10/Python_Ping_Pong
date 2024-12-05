from turtle import Screen
from extras import Paddle, Scoreboard
from ball import Ball
import time


screen=Screen()
score=Scoreboard()

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("pong game")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on= True
while game_is_on:
    time.sleep(ball.ballspeed)
    score.update()
    screen.update()
    ball.move()

    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce()

    if ball.xcor()>330 and ball.distance(r_paddle)<50 or ball.xcor()<-330 and ball.distance(l_paddle)<50:
        ball.hit()

    if ball.xcor()>390:
        ball.reset_pos()
        score.l_point()

    if ball.xcor()<-390:
        ball.reset_pos()
        score.r_point()

screen.exitonclick()