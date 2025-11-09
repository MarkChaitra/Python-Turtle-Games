import turtle
import time
import random

#Setup screen
window = turtle.Screen()
window.title("Astroid Dodge by @MarkChaitra")
window.bgcolor("black")
window.setup(width=500, height=500)
window.tracer(0)

#Ship
window.addshape("Astroid Dodge Game/rocketShip.gif")  # File must be in the same folder
Ship = turtle.Turtle()
Ship.shape("Astroid Dodge Game/rocketShip.gif")
Ship.shapesize(stretch_wid=0.5, stretch_len=0.5)
Ship.penup()
Ship.goto(0,-170)

Score = 0
highScore = 0

#ScoreBoard
ScoreBoard = turtle.Turtle()
ScoreBoard.speed(0)
ScoreBoard.color("white")
ScoreBoard.penup()
ScoreBoard.hideturtle()
ScoreBoard.goto(0, 220)
ScoreBoard.write("Score: {}   High Score: {}".format(Score, highScore), align="center", font=("Courier", 15, "normal"))

left = False
right = False

def go_left():
    global left
    left = True
def stop_left():
    global left
    left = False
def go_right():
    global right
    right = True
def stop_right():
    global right
    right = False
def move():
    global left, right
    if left == True and Ship.xcor() > -225:
        x = Ship.xcor()
        y = Ship.ycor()
        Ship.goto(x-5,y)
    elif right == True and Ship.xcor() < 225:
        x = Ship.xcor()
        y = Ship.ycor()
        Ship.goto(x+5,y)

AstroidList = []
    
window.listen()
window.onkeypress(go_left, "a")
window.onkeyrelease(stop_left, "a")
window.onkeypress(go_right, "d")
window.onkeyrelease(stop_right, "d")

while True:

    window.update()
    move()

    x = random.randint(1,100)

    if x < 5:
        Astroid = turtle.Turtle()
        Astroid.penup()
        Astroid.speed(0)
        Astroid.color("grey")
        Astroid.shape("square")
        Astroid.goto(random.randint(-220, 220), 250)
        AstroidList.append(Astroid)

    for a in AstroidList[:]:

        if a.ycor() < Ship.ycor()+54 and a.ycor() > Ship.ycor()-54 and a.xcor() < Ship.xcor()+25 and a.xcor() > Ship.xcor()-25:
            for a in AstroidList:
                a.goto(500,500)
            AstroidList.clear()

            Ship.goto(0,-170)


            highScore = Score if Score > highScore else highScore
            Score = 0
            ScoreBoard.clear()
            ScoreBoard.write("Score: {}   High Score: {}".format(Score, highScore), align="center", font=("Courier", 15, "normal"))

            continue

        if a.ycor() > -250:
            a.goto(a.xcor(), a.ycor()-3)
        else:
            Score += 1
            ScoreBoard.clear()
            ScoreBoard.write("Score: {}   High Score: {}".format(Score, highScore), align="center", font=("Courier", 15, "normal"))
            AstroidList.remove(a)
            del a


