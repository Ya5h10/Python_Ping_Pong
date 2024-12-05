from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        paddle = Turtle()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def go_down(self):
        self.goto(self.xcor(), self.ycor() - 20)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0

    def update(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score, align="center", font=("courier",40, "normal"))
        self.goto(100,200)
        self.write(self.r_score, align="center", font=("courier",40, "normal"))

    def r_point(self):
        self.r_score+=1

    def l_point(self):
        self.l_score+=1