from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        ##self.shapesize(stretch_wid=2, stretch_len=2)
        self.penup()
        self.x=8
        self.y=8
        self.ballspeed= 0.05

    def move(self):
        new_x = self.xcor()+ self.x
        new_y = self.ycor()+ self.y
        self.goto(new_x,new_y)

    def bounce(self):
        self.y *= -1
        self.ballspeed*=0.9

    def hit(self):
        self.x *= -1

    def reset_pos(self):
        self.goto(0,0)
        self.x*=-1