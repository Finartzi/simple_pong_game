# Simple Pong in Python 3 for beginners
# By @TokyoEdTech
# Part 2 : Game objects

import turtle

wn = turtle.Screen()
wn.title("Pong by  @TokyoEdTech")
wn.bgcolor("black")

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)


# Paddel B

# Ball



while True:
    wn.update()

