import _sqlite3
import turtle
import os
from pathlib import Path

def leaderboard():
    wn1 = turtle.Screen()
    wn1.screensize(600, 800)
    # wn1.setup(width = 1.0, height= 1.0, startx= 0, starty= 0)
    wn1.title("Scoreboard")
    wn1.bgcolor("black")
    wn1.tracer(0)

    if Path('Resources/Database/game.db').is_file():
        # header

        head = turtle.Turtle()
        head.speed(0)
        head.shape("square")
        head.color("white")
        head.penup()
        head.hideturtle()
        head.goto(0, 300)
        head.write("        NAME        SCORE", align="center", font=("Courier", 16, "normal"))

        x = 60
        y = 250
        conn = _sqlite3.connect('Resources/Database/game.db')
        c = conn.cursor()
        c.execute("SELECT * FROM gametab")
        result = c.fetchall()
        print(result)
        for i in result:
            # print(i[0])
            # print("\n")
            # print(i[1])
            pen = turtle.Turtle()
            pen.speed(0)
            pen.shape("square")
            pen.color("white")
            pen.penup()
            pen.hideturtle()
            pen.goto(x, y)
            pen.write("%-10s     %-2s"%(i[0],i[1]), align="center", font=("Courier", 16, "normal"))
            y = y - 40

    else:
        pen = turtle.Turtle()
        pen.speed(0)
        pen.shape("square")
        pen.color("white")
        pen.penup()
        pen.hideturtle()
        pen.goto(0, 0)
        pen.write("Nothing to show", align="center", font=("Courier", 24, "normal"))
        # print("nothing exists")

    wn1.update()
    wn1.mainloop()

def main():
    leaderboard()

