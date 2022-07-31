import time
from turtle import Turtle, Screen

screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong Game')

paddel = Turtle()
paddel.shape('square')
paddel.color('white')
paddel.shapesize(stretch_wid=5, stretch_len=1)
paddel.penup()


paddel.goto(385, 0)



def forward():
    y = paddel.ycor() + 20
    paddel.goto(paddel.xcor(), y)


def backward():
    y = paddel.ycor() - 20
    paddel.goto(paddel.xcor(), y)


screen.listen()
screen.onkeypress(forward, "Up")
screen.onkeypress(backward, "Down")

is_game_on = True

while is_game_on:
    screen.update()



screen.exitonclick()