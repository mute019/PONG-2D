import turtle
import sys
import ctypes

def result_func(player, wn):
    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 0)
    pen.write("{} WINS".format(player), align="center", font=("Courier", 24, "normal"))
    


