import turtle
import random
from result import *
import sql12
import ctypes
import winsound
import sys

# player ID
player1 = "player" + str(random.randint(100, 101))
player2 = "Bot Fred"
# paddle variables

# Functions
def paddle_a_up(paddle_a):
    y = paddle_a.ycor()
    y += 35
    paddle_a.sety(y)

def paddle_a_down(paddle_a):
    y = paddle_a.ycor()
    y -= 35
    paddle_a.sety(y)

def paddle_b_up(paddle_b):
    y = paddle_b.ycor()
    y += 15
    paddle_b.sety(y)

def paddle_b_down(paddle_b):
    y = paddle_b.ycor()
    y -= 15
    paddle_b.sety(y)

# Main game loop

def gameloop():
    user32 = ctypes.windll.user32
    height = user32.GetSystemMetrics(1)
    width = user32.GetSystemMetrics(0)
    wn = turtle.Screen()
    wn.title("Pong")
    wn.bgcolor("black")
    wn.setup(width=width, height=height-90, starty= 0 , startx= 0)
    wn.tracer(0)

    paddle_a = turtle.Turtle()
    paddle_b = turtle.Turtle()
    ball = turtle.Turtle()
    pen = turtle.Turtle()
    cred = turtle.Turtle()
    # bot direction booleans
    bot_up = False
    bot_down = False

    # Paddle A
    # paddle_a = turtle.Turtle()
    paddle_a.speed(0)
    paddle_a.shape("square")
    paddle_a.color("white")
    paddle_a.shapesize(stretch_wid=5, stretch_len=1)
    paddle_a.penup()
    paddle_a.goto(-(user32.GetSystemMetrics(0) / 2) + 90, 0)

    # Paddle B
    # paddle_b = turtle.Turtle()
    paddle_b.speed(0)
    paddle_b.shape("square")
    paddle_b.color("white")
    paddle_b.shapesize(stretch_wid=5, stretch_len=1)
    paddle_b.penup()
    paddle_b.goto((user32.GetSystemMetrics(0) / 2) - 90, 0)

    # Ball
    # ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("circle")
    ball.color("white")
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 2
    ball.dy = 2

    # Pen
    # pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, ((user32.GetSystemMetrics(1) / 2) - 130))
    pen.write("SCORE: 0 - SCORE: 0", align="center", font=("Courier", 24, "bold"))

    # Players IDs
    # cred = turtle.Turtle()
    cred.speed(0)
    cred.shape("square")
    cred.color("white")
    cred.penup()
    cred.hideturtle()
    cred.goto(0, ((user32.GetSystemMetrics(1) / 2) - 90))
    cred.write("{}      Vs      {}".format(player1, player2), align="center", font=("Courier", 24, "bold"))
    def pad_a_u():
        paddle_a_up(paddle_a)
    def pad_a_d():
        paddle_a_down(paddle_a)

    #player score
    score_a = 0
    score_b = 0
    while True:
        wn.update()
        # Keyboard bindings

        wn.listen()
        wn.onkeypress(pad_a_u, "Up")
        wn.onkeypress(pad_a_d, "Down")

        # Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Border checking
        # paddle_a
        if paddle_a.ycor() > ((height / 2) - 190):
            paddle_a.sety((height / 2) - 190)

        if paddle_a.ycor() - 100 < (-(height / 2)):
            paddle_a.sety(-(height / 2) + 100)
        # paddle_b

        if paddle_b.ycor() > ((height / 2) - 190):
            paddle_b.sety((height / 2) - 190)

        if paddle_b.ycor() - 100 < (-(height / 2)):
            paddle_b.sety((-(height / 2)) + 100)

        # Top and bottom
        if ball.ycor() > ((height/2)-150):
            ball.sety(((height/2)-150))
            ball.dy *= -1
            winsound.PlaySound("Resources\Sound\sfx.wav",winsound.SND_ASYNC)
    
        elif ball.ycor() < -((height/2)-50):
            ball.sety((-(height/2)+50))
            ball.dy *= -1
            winsound.PlaySound("Resources\Sound\sfx.wav",winsound.SND_ASYNC)

        # Left and right
        if ball.xcor() > ((width/2)-40):
            score_a += 1
            pen.clear()
            pen.write("SCORE: {} - SCORE: {}".format(score_a, score_b), align="center", font=("Courier", 24, "bold"))
            ball.goto(450, 0)
            ball.dx *= -1

        elif ball.xcor() < (-(width/2)+40):
            score_b += 1
            pen.clear()
            pen.write("SCORE: {} - SCORE: {}".format(score_a, score_b), align="center", font=("Courier", 24, "bold"))
            ball.goto(-450, 0)
            ball.dx *= -1

        # Paddle and ball collisions
        #paddle_a right side collison
        if ball.xcor() < (-(width/2)+110) and ball.ycor() < paddle_a.ycor() + 60 and ball.ycor() > paddle_a.ycor() - 60:
            ball.dx *= -1
            winsound.PlaySound("Resources\Sound\sfx.wav",winsound.SND_ASYNC)
        #paddle_b left side collision
        elif ball.xcor() > ((width/2)-110) and ball.ycor() < paddle_b.ycor() + 60 and ball.ycor() > paddle_b.ycor() - 60:
            ball.dx *= -1
            winsound.PlaySound("Resources\Sound\sfx.wav",winsound.SND_ASYNC)
            #paddle A top

        # bot direction and movement
        if ball.ycor() > paddle_b.ycor() + 40 and ball.xcor() > 0:
            bot_up = True
  
        elif ball.ycor() < paddle_b.ycor() - 40 and ball.xcor() > 0:
            bot_down = True
        else:
            bot_up = False
            bot_down = False

        if bot_up:
            paddle_b_up(paddle_b)
        elif bot_down:
            paddle_b_down(paddle_b)

        # result screen
        if score_a is 10 and score_a > score_b:

            return score_a, score_b, wn
        elif score_b is 10 and score_b > score_a:

            return score_a, score_b, wn
       

def main():

    score1, score2, wn = gameloop()
    sql12.main(score1, score2, player1, player2)
    if score1 is 10:
        result_func(player1, wn)
        
    elif score2 is 10:
        result_func(player2, wn)

